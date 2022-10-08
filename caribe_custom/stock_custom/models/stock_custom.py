# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockCustom(models.Model):
    _inherit = 'product.template'
    _description = 'Stock App Custom'