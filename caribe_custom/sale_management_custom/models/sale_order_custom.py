# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Custom'

    sale_type = fields.Selection([
        ('rec', 'Grabada'),
        ('sign', 'Firmados')
    ], string="Tipo de venta")

    call_id = fields.Char(string="ID de llamada", help='Id de llamada registrada')