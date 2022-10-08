# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'
    _description = 'Contacts Custom'

    updated = fields.Boolean()
    # diary = fields.Many2many('res.partner', 'name', string='Agenda')
    diary = fields.One2many('res.partner.number', 'client', string='Agenda')


class ResPartnerNumber(models.Model):
    _name = 'res.partner.number'
    _description = 'Saving numbers of contacts'
    _rec_name = 'client'

    client = fields.Many2one('res.partner', domain="[('customer','=', True)]", string='Cliente')
    save_number = fields.Char(string='Telefono')
    is_active = fields.Boolean(string='Activo')
    is_main = fields.Boolean(string='Principal')