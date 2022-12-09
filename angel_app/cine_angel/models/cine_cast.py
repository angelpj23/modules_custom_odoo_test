from odoo import fields, models


class CastMovie(models.Model):
    _name = 'cine.cast'
    _description = 'Module for cinema Cast'

    image = fields.Binary(string="Perfil")
    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo?")
    biography = fields.Char(string="Biografia")


class Director(models.Model):
    _name = 'cine.director'
    _description = 'Module for cinema director'

    image = fields.Binary(string="Perfil")
    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo?")
    biography = fields.Char(string="Biografia")