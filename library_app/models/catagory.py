from odoo import api, fields, models
from odoo.exceptions import Warning


class Catagories(models.Model):
    _name = 'library.catagories'
    _description = 'Catagory'
    name = fields.Char('Catagory')
    book_limit = fields.Char('Book Limit')
    book_ids = fields.One2many('library.book','catagory_id','Book Catagor')