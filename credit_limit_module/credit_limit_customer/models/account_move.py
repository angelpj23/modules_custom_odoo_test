# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'account.move'

    applied_credit_limit = fields.Float(string='Limite de credito', compute='update_credit_limit',
                                        help='Limite de credito establecido para este cliente')

    @api.onchange('partner_id')
    def update_credit_limit(self):
        if self.partner_id:
            if self.partner_id.credit_limit and self.partner_id.active_limit:
                for s in self:
                    s.applied_credit_limit = self.partner_id.credit_limit

                    if self.partner_id.block_SO == 0 and self.amount_total > self.applied_credit_limit or self.partner_id.block_SO == 0 and self.partner_id.total_debt >= self.applied_credit_limit:
                        return {'value': {},
                                'warning': {'title': 'Limite de credito',
                                            'message': 'El cliente excede el limite de credito establecido: {}'.format(
                                                s.applied_credit_limit)}}

                    elif self.partner_id.block_SO and self.amount_total > self.applied_credit_limit or self.partner_id.block_SO and self.partner_id.total_debt >= self.applied_credit_limit:
                        raise ValidationError(
                            _('No puede facturar \nEl cliente excede el limite de credito establecido: {}'.format(s.applied_credit_limit)))
            else:
                for s in self:
                    s.applied_credit_limit = 0
