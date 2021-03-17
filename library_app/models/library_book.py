from odoo import api, fields, models
from odoo.exceptions import Warning


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    sequence = fields.Char('Book Sequence',requrid='True',index='True', copy='False',default='New')
    # isbn = fields.Char('ISBN')
    # active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
    catagory_id = fields.Many2one('library.catagories','Book Catagory')
    pageno = fields.Integer('Page Number')
    language = fields.Char('Language')
    # language = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang)
    book_type = fields.Selection(
        [('paper', 'Paperback'),
         ('hard', 'Hardcover'),
         ('electronic', 'Electronic'),
         ('other', 'Other')],
        'Type')

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('library.book')
        return super(Book, self).create(vals)