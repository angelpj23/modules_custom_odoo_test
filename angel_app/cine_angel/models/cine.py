from odoo import fields, models, api


class Cine(models.Model):
    _name = 'cine'
    _description = 'Module for cinema premier'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    image = fields.Binary(string="Portada")
    name = fields.Char("Nombre", tracking=True)  # tracking deja registro de los cambios en el chatter
    premiere = fields.Date(string='Fecha de estreno')
    description = fields.Char(string='Descripcion')
    category = fields.Many2one('cine.category', string="Categoria", domain=[("active", "=", True)])
    link_triller = fields.Char('URL')
    director = fields.Many2one('cine.director', string="Director", domain=[("active", "=", True)])
    image_director = fields.Binary(related='director.image', string="Perfil del director") # related trae el campo indicado dependiendo de otro
    cast = fields.Many2many('cine.cast', 'name', string="Elenco")
    state = fields.Selection([('draft', 'Proximamente'), ('posted', 'Publicado'), ('cancel', 'Cancelada')],
                             default='draft', tracking=True)
    calification = fields.Selection([('very_bad', 'Muy Mala'), ('bad', 'Mala'), ('good', 'Buena'), ('excelent', 'Excelente')])
    # store=True guarda data en la base de datos
    price = fields.Char(string="Precio", compute="add_price")

    def posted_movie(self):
        self.state = 'posted'

    def cancel_movie(self):
        self.state = 'cancel'

    def reload_movie(self):
        self.state = 'draft'

    # depends: se actualizara el campo en tiempo real
    @api.depends('price')
    def add_price(self):
        search_price = self.env['product.template'].search([('id', '=', 1)])
        for p in search_price:
            get_price = p.list_price
            # convirtiendo a String un numero para poder concatenar
            self.price = "$"+str(get_price)


    # Evitando que se creen registros duplicados
    #     nombre del constraint
    #     unique() los valores que no podran duplicarse
    #     mensaje de error
    #     Para desahibilitar esta accion se debe eliminar desde la base de datos

    _sql_constraints = [("name_unique", "unique(name)", "Este registro ya existe, no puede crear duplicados!")]
