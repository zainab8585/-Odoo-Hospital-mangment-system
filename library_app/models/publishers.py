from odoo import api, fields, models
from odoo.exceptions import Warning


class Publishers(models.Model):
    _name = 'library.publishers'
    _description = 'Publishers'
    name = fields.Char('Publishers')
    books_id = fields.One2many('library.book','publisher_id','Book')

    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    parent_id = fields.Many2one('res.partner', string='Related Company', index=True)
    type = fields.Selection(
        [('contact', 'Contact'),
         ('invoice', 'Invoice address'),
         ('delivery', 'Shipping address'),
         ('other', 'Other address'),
         ("private", "Private Address"),
        ], string='Address Type',
        default='contact',
        help="Used by Sales and Purchase Apps to select the relevant address depending on the context.")