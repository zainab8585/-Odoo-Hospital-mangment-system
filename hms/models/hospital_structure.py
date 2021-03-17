# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# class hms section
class HmsSection(models.Model):
    _name = 'hms.section'
    _order = 'code'
    _description = "Outpatient Clinic Department"

    name = fields.Char(help="Clinic Name")
    code = fields.Char("Code", help='Code of department', default="0")

    _sql_constraints = [('code', 'unique(code)',
                         'This  code is already assigned to other section please enter another code')]

    # @api.constrains('code')
    # def _check_duplicate_code(self):
    #     codes = self.search([])
    #     for c in codes:
    #         if self.code.lower() == c.code.lower() and self.id != c.id:
    #             raise ValidationError("Error: code must be unique")

    @api.constrains('name')
    def _check_duplicate_code(self):
        codes = self.search([])
        for c in codes:
            if self.name.lower() == c.name.lower() and self.id != c.id:
                raise ValidationError("Error: Section name must be unique")

    @api.constrains('code')
    def _size_code(self):
        for x in self:
            if len(self.code) < 5:
                raise ValidationError(" The code must be equal 5 chars")
# -------------------------------------------------------------------------------------------------------------

# class hms floors
class HmsFloors(models.Model):
    _name = 'hms.floors'
    # _rec_name = 'name'
    _description = 'hospital floors'
    _order = 'code'

    code = fields.Char("Code", help='Code of Floor', default="0")
    name = fields.Char(help='name of Floor')
    section_id = fields.Many2one('hms.section', string='Clinic Name')
    # add constrain
    # _sql_constraints = [('name', 'unique(name)',
    #                      'This  name is already assigned to other section, please enter another name')]
    _sql_constraints = [('code', 'unique(code)',
                 'This  Code is already assigned to other floor, please enter another code')]

    @api.constrains('name')
    def _check_duplicate_code(self):
        codes = self.search([])
        for c in codes:
            if self.name.lower() == c.name.lower() and self.id != c.id:
                raise ValidationError("Error: Floor name must be unique")

    @api.constrains('code')
    def _size_code(self):
        for x in self:
            if len(self.code) > 1:
                raise ValidationError(" The code must be equal 1 chars")

# -------------------------------------------------------------------------------------------------------------------
# class hms room
class HmsRooms(models.Model):
    _name = 'hms.rooms'
    # _rec_name = 'name'
    _description = 'hospital rooms'
    _order = 'code'

    code = fields.Char("Code ", help='Code of Rooms', default="0")
    name = fields.Char(help='name of the room')
    floor_id = fields.Many2one('hms.floors', string='Floor Name')
    # department_id = fields.Char(related='floor_id.section_id.name')
    state = fields.Selection([('free', 'Free'), ('busy', 'Busy')], default='free')
    price = fields.Integer(help='Price of the room', default=0)
    type = fields.Char(help='Type of room', string='The type')
    no_of_bed = fields.Integer(help='capcity of the room', string='Number of the beds', default=3)
    notes = fields.Text(help='Add your  of notes', string='Notes')

    # add constrain
    # _sql_constraints_rname = [('name', 'unique(name)',
    #                      'This  name is already assigned to other section, please enter another name')]
    _sql_constraints = [('code', 'unique(code)',
                              'This  Code is already assigned to other room, please enter another code')]

    @api.constrains('name')
    def _check_duplicate_code(self):
        codes = self.search([])
        for c in codes:
            if self.name.lower() == c.name.lower() and self.id != c.id:
                raise ValidationError("Error: Room name must be unique")

    @api.constrains('code')
    def _size_code(self):
        for x in self:
            if len(self.code) >3:
                raise ValidationError(" The code must be equal 1 chars")
# ----------------------------------------------------------------------------------------------------
# class beds
class HmsBeds(models.Model):
    _name = 'hms.beds'
    # _rec_name = 'code'
    _order = 'code'
    _description = 'hospital beds'
    code = fields.Char("Code ", help='Code of Rooms', default="0")
    name = fields.Char(help='name of Beds')
    room_id = fields.Many2one('hms.rooms', string='Room Name')
    state = fields.Selection([('free', 'Free'), ('busy', 'Busy')], default='free')

    # add constrain
    # _sql_constraints_bname = [('name', 'unique(name)',
    #                     'This  name is already assigned to other section, please enter another name')]
    _sql_constraints_ = [('code', 'unique(code)',
                              'This  Code is already assigned to other Bed, please enter another code')]
    # update rec name
    @api.multi
    def name_get(self):
        res = super(HmsBeds, self).name_get()
        data = []
        for beds in self:
            display_value = ''
            display_value += beds.code + " "
            display_value += '('
            display_value += beds.name or ""
            display_value += ')'
            data.append((beds.id, display_value))
        return data

    # ------------------------------------------------------------------
    # @api.multi
    # def name_get(self):
    #             for data in self:
    #                 data.name = data.name+" "+data.code
    #         # display_name = []
    #         # res.append(data.name+" "+ data.code)
    #     # return res
    # -------------------------------------------------------------------------------------------------------------------
    # @api.constrains('name')
    # def _check_duplicate_code(self):
    #     codes = self.search([])
    #     for c in codes:
    #         if self.name.lower() == c.name.lower() and self.id != c.id:
    #             raise ValidationError("Error: name must be unique")

    @api.constrains('code')
    def _size_code(self):
        for x in self:
            if len(self.code) >3:
                raise ValidationError(" The code must be equal 1 chars")
# --------------------------------------------------------------------------------------------------------------------

# Class entry
# class HmsEntry(models.Model):
#     _name = 'hms.entry'
#     _description = 'hospital entry'
#     _rec_name = 'Patient_Name'
#
#     Patient_Name = fields.Many2one('medical.patient', 'Patient name')
#     Patient_Address = fields.Many2one('medical.patient', 'Patient Address')
#     section_id = fields.Many2one('hms.section', 'Section select')
#     floor_id = fields.Many2one('hms.floors', 'floor select')
#     room_ids = fields.Many2one('hms.rooms', 'room select')
#     beds_ids = fields.Many2one('hms.beds', 'Bed select')
#     price = fields.Integer(default=0)
#     # ----------------------------------------------------------------------
#     @api.onchange('section_id')
#     def _onchange_section_id(self):
#         floor_obj = self.env['hms.floors'].search([('section_id.name','=',self.section_id.name)])
#         print("1----- ",floor_obj,"---->",floor_obj.mapped('name'))
#         floor_list  =[]
#         for data in floor_obj:
#             floor_list.append(data.name)
#         res = {}
#         res['domain'] = {'floor_id': [('name', 'in', floor_list)]}
#         return res
#
#         # # res = {}
#         # # res['domain'] = {'floor_id': [('section_id', '=', self.floor_id.section_id)]}
#         # # return res
#         #     record = self.env['hms.floors'].search([('section_id.name','=',self.section_id.name)])
#         #     x = record.mapped('name')
#         #     print(record,x)
#
#     # ----------------------------------------------------------------------------------------------------
#
#     # onchang room
#
#     @api.onchange('floor_id')
#     def _onchange_room_ids(self):
#         room_obj = self.env['hms.rooms'].search([('floor_id.name','=',self.floor_id.name)])
#         print("2----- ",room_obj,"---->",room_obj.mapped('name'))
#         room_list = []
#         for data in room_obj:
#             room_list.append(data.name)
#         res = {}
#         res['domain'] = {'room_ids': [('name', 'in',room_list)]}
#         return res
#     # --------------------------------------------------------------------------------------------
#     # onchang beds
#
#     @api.onchange('room_ids')
#     def _onchange_bed_ids(self):
#         bed_obj = self.env['hms.beds'].search([('room_id.name', '=', self.room_ids.name)])
#         print("3---- ",bed_obj, "---->", bed_obj.mapped('code'))
#         bed_list = []
#         for data in bed_obj:
#             if data.state == 'free':
#                 bed_list.append(data.name)
#         res = {}
#         res['domain'] = {'beds_ids': [('name', 'in',bed_list )]}
#         return res
#  #----------------------------------------------------------------------------------------------------
#     @api.model
#     def create(self, vals):
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
#         res = super(HmsEntry, self).create(vals)
#         res.beds_ids.state = 'busy'
#         return res
# # --------------------------------------------------------------------------------------
#
# @api.onchange('Patient_Name')
# def _onchange_patient(self):
#     self.Patient_Address = self.Patient_Name
# # @api.multi
# # def write(self,values):
# #         hmsBed_write = super(HmsEntry,self).write(values)
# #         return hmsBed_write
