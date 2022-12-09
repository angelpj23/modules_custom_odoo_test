from odoo import fields, models


class CategoryMovie(models.Model):
    _name = 'cine.category'
    _description = 'Module for cinema premier'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo?")
