# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    active_limit = fields.Boolean(string='Activar credito')
    credit_limit = fields.Float(string='Limite de credito', help='Establezca el limite de credito para este cliente')
    block_SO = fields.Boolean(string='Bloquear ventas', help='Bloquear las ventas cuando exceda el limite de credito')
    total_debt = fields.Float(compute='update_debit')

    @api.onchange('total_debt')
    def update_debit(self):
        for contact in self:
            customer = contact.id
            invoices = self.env['account.move'].search(
                [('partner_id.id', '=', customer), ('state', '=', 'posted'),
                 ('payment_state', 'in', ['not_paid', 'partial'])])
            contact.total_debt = (sum(invoices.mapped('amount_total_signed')))