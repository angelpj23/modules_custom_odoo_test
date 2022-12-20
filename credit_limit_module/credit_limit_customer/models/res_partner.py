# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    active_limit = fields.Boolean(string='Activar credito')
    credit_limit = fields.Float(
        string='Limite de credito',
        invisible="[('active_limit', '=', False)]",
        help='Establezca el limite de credito para este cliente',
    )
    block_SO = fields.Boolean(
        string='Bloquear ventas',
        help='Bloquear las ventas cuando exceda el limite de credito',
    )
    total_debt = fields.Float(
        compute='update_debit', invisible="[('active_limit', '=', False)]"
    )

    @api.onchange('total_debt')
    def update_debit(self):
        for contact in self:
            customer = contact.id
            invoices = self.env['account.invoice'].search(
                [
                    ('partner_id.id', '=', customer),
                    ('journal_id', '=', 1),
                    ('state', 'in', ['posted', 'in_payment']),
                ]
            )
            contact.total_debt = sum(invoices.mapped('amount_total_signed'))