from odoo import models, fields, api


# from odoo.exceptions import ValidationError
# Class entry

class HmsEntry(models.Model):
    _name = 'hms.entry'
    _description = 'Reception Screen to record the date'
    _rec_name = 'Patient_Name'

    Patient_Name = fields.Many2one('medical.patient', 'Patient name')
    # Patient_Address = fields.Many2one('medical.patient', 'Patient Address')
    section_id = fields.Many2one('hms.section', 'Section select')
    floor_id = fields.Many2one('hms.floors', 'Floor select')
    room_ids = fields.Many2one('hms.rooms', 'Room select')
    beds_ids = fields.Many2one('hms.beds', 'Bed select')

    Service = fields.Selection([('reveal', 'Reveal'), ('consultation', 'Consultation'), ('urgent', 'Urgent')])
    Reservation_type = fields.Selection([('room', 'Room'), ('bed', 'Bed')])
    price = fields.Integer(string='Price', related='room_ids.price', default=0)
    total = fields.Integer("Total", compute='_calculate_total')
    paid_up = fields.Integer("Paid up", default=0)
    The_rest = fields.Integer("The_rest", default=0, compute='_calculate_The_rest')
    date = fields.Datetime(string="Date of To day", default=lambda self: fields.Datetime.now())
    # ------------------------------------------------------------------------------------------------------------
    @api.one
    @api.depends("price")
    def _calculate_total(self):
        # for rec in self:
        #    rec.total = int(rec.room_ids.price + (rec.room_ids.price)/4)
        self.total = int(self.price + (self.price) / 4)

# -----------------------------------------------------------------------------------------------------------
    @api.one
    @api.depends("total","paid_up")
    def _calculate_The_rest(self):
        # for rec in self:
        #     rec.The_rest = rec.total + rec.paid_up
         self.The_rest = self.total - self.paid_up


# ----------------------------------------------------------------------
    @api.onchange('section_id')
    def _onchange_section_id(self):
        floor_obj = self.env['hms.floors'].search([('section_id.name', '=', self.section_id.name)])
        print("1----- ", floor_obj, "---->", floor_obj.mapped('name'))
        floor_list = []
        for data in floor_obj:
            floor_list.append(data.name)
        res = {}
        res['domain'] = {'floor_id': [('name', 'in', floor_list)]}
        return res

    @api.onchange('floor_id')
    def _onchange_room_ids(self):
        room_obj = self.env['hms.rooms'].search([('floor_id.name', '=', self.floor_id.name)])
        print("2----- ", room_obj, "---->", room_obj.mapped('name'))
        room_list = []
        for data in room_obj:
            if data.state == 'free':
                room_list.append(data.name)
        res = {}
        res['domain'] = {'room_ids': [('name', 'in', room_list)]}
        return res
    # --------------------------------------------------------------------------------------------
    # onchang beds

    @api.onchange('room_ids')
    def _onchange_bed_ids(self):
        bed_obj = self.env['hms.beds'].search([('room_id.name', '=', self.room_ids.name)])
        print("3---- ", bed_obj, "---->", bed_obj.mapped('code'))
        bed_list = []
        for data in bed_obj:
             if data.state == 'free':
                bed_list.append(data.code)
        #         name
        res = {}
        res['domain'] = {'beds_ids': [('code', 'in', bed_list)]}
        return res


    # ----------------------------------------------------------------------------------------------------
    @api.model
    def create(self, vals):
        # for i in self.beds_ids:
        #     i.state = 'busy'
        # res = super(HmsEntry, self).create(vals)
        # return res
        # print('welcome',vals)
        # x = self.env['hms.beds'].browse(self.beds_ids).id
        # print('zainab')
        # print(type(x))
        #  for i in  self.beds_ids:
        #  #     print(i)
        #  i.state = 'busy'
        # # x.state = 'busy'
        #  # print(x)
        # res = super(HmsBeds,self).create(vals)
        res = super(HmsEntry, self).create(vals)
        res.beds_ids.state = 'busy'
        res.room_ids.no_of_bed = res.room_ids.no_of_bed-1
        if res.room_ids.no_of_bed==0:
            res.room_ids.state = 'busy'
        return res

    # --------------------------------------------------------------------------------------

# @api.onchange('Patient_Name')
# def _onchange_patient(self):
#     self.Patient_Address = self.Patient_Name
# # @api.multi
# # def write(self,values):
# #         hmsBed_write = super(HmsEntry,self).write(values)
# #         return hmsBed_write
