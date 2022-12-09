from odoo import fields, models


class WidgetsCustom(models.Model):
    _name = 'widgets.custom'
    _description = 'Module for add widgets'

    widget1 = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    widget2 = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    widget3 = fields.Selection(
        [('very_bad', 'Muy Mala'), ('bad', 'Mala'), ('good', 'Buena'), ('excelent', 'Excelente')])
    widget4 = fields.Boolean()
    widget5 = fields.Float()
    widget6 = fields.Selection(
        [('very_bad', 'Muy Mala'), ('bad', 'Mala'), ('good', 'Buena'), ('excelent', 'Excelente')])
    widget7 = fields.Selection(
        [('very_bad', 'Muy Mala'), ('bad', 'Mala'), ('good', 'Buena'), ('excelent', 'Excelente')])
