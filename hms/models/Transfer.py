from odoo import models, fields, api
#
#
# # from odoo.exceptions import ValidationError
# # Class entry
#
class Hmstransfer(models.Model):
    _name = 'hms.transfer'
    _description = 'transfer Screen'
    _rec_name = 'Patient_Name'
# #
    Patient_Name = fields.Many2one('hms.entry', 'Patient name')
    section_name = fields.Char(related='Patient_Name.section_id.name',string=' From Section ')
    # Patient_Address = fields.Many2one('medical.patient', 'Patient Address')
    # section_id = fields.Many2one('hms.section', 'Section select')
    floor_name = fields.Char(related='Patient_Name.floor_id.name',string='From Floor ')
    room_name = fields.Char(related='Patient_Name.room_ids.name',string='From Room')
    beds_name = fields.Char(related='Patient_Name.beds_ids.code',string='From Bed')

    Patient_Name = fields.Many2one('hms.entry', 'Patient name')
    # Patient_Address = fields.Many2one('medical.patient', 'Patient Address')
    section_id = fields.Many2one('hms.section', ' To Section ')
    floor_id = fields.Many2one('hms.floors', 'To Floor')
    room_ids = fields.Many2one('hms.rooms', 'To Room')
    beds_ids = fields.Many2one('hms.beds', 'To Bed')
    date = fields.Datetime(string="Date of To day", default=lambda self: fields.Datetime.now())


    # sum = 0
    # no_of_patient_logout = fields.Integer("no of patient logout",default=sum)
    # beds_ids = fields.Many2one('hms.beds', 'Bed select',invisable=1)

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

    @api.model
    def create(self, vals):
        res = super(Hmstransfer, self).create(vals)
        bed_obj = self.env['hms.beds'].search([('code', '=', res.beds_name)])
        room_obj = self.env['hms.rooms'].search([('name', '=', res.room_name)])
        print("room obj ---------",room_obj.mapped('code'))
        print("bed_obj----------------",bed_obj.mapped('code'))
        for data in bed_obj:
            data.state ='free'
            print("yes")
        for rec in room_obj:
            rec.no_of_bed = rec.no_of_bed+1
            # if rec.no_of_bed==3:
            rec.state = 'free'
        res.beds_ids.state = 'busy'
        res.room_ids.no_of_bed = res.room_ids.no_of_bed - 1
        if res.room_ids.no_of_bed == 0:
            res.room_ids.state = 'busy'
        return res


    #  @api.model
    # def create(self, vals):
    #         # for i in self.beds_ids:
    #         #     i.state = 'busy'
    #         # res = super(HmsEntry, self).create(vals)
    #         # return res
    #         # print('welcome',vals)
    #         # x = self.env['hms.beds'].browse(self.beds_ids).id
    #         # print('zainab')
    #         # print(type(x))
    #         #  for i in  self.beds_ids:
    #         #  #     print(i)
    #         #  i.state = 'busy'
    #         # # x.state = 'busy'
    #         #  # print(x)
    #         # res = super(HmsBeds,self).create(vals)
    #         res = super(Hmstransfer, self).create(vals)
    #         res.beds_ids.state = 'busy'
    #         res.room_ids.no_of_bed = res.room_ids.no_of_bed-1
    #         if res.room_ids.no_of_bed==0:
    #             res.room_ids.state = 'busy'
    #         return res

