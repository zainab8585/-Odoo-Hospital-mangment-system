from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HmsLogout(models.Model):
    _name = 'hms.logout'
    _description = 'Logout Screen'
    _rec_name = 'Patient_Name'

    Patient_Name = fields.Many2one('hms.entry', 'Patient name')
    section_name = fields.Char(related='Patient_Name.section_id.name',string='Section name')
    # Patient_Address = fields.Many2one('medical.patient', 'Patient Address')
    # section_id = fields.Many2one('hms.section', 'Section select')
    floor_name = fields.Char(related='Patient_Name.floor_id.name',string='Floor name')
    room_name = fields.Char(related='Patient_Name.room_ids.name',string='Room name')
    beds_name = fields.Char(related='Patient_Name.beds_ids.code',string='Bed name')
    The_rest = fields.Integer("The_rest",related='Patient_Name.The_rest')

    date = fields.Datetime(string="Date of To day", default=lambda self: fields.Datetime.now())

    # sum = 0
    # no_of_patient_logout = fields.Integer("no of patient logout",default=sum)
    # beds_ids = fields.Many2one('hms.beds', 'Bed select',invisable=1)
#
    @api.model
    def create(self, vals):
        res = super(HmsLogout, self).create(vals)
        bed_obj = self.env['hms.beds'].search([('code', '=', res.beds_name)])
        room_obj = self.env['hms.rooms'].search([('name', '=', res.room_name)])
        print("room obj ---------",room_obj.mapped('code'))
        print("bed_obj----------------",bed_obj.mapped('code'))
        # if self.Patient_Name.The_rest == 0:
        for data in bed_obj:
            data.state ='free'
            print("yes")
        for rec in room_obj:
            rec.no_of_bed = rec.no_of_bed+1
            # if rec.no_of_bed==3:
            rec.state = 'free'
        # else:
        #     raise ValidationError("Please pay the full amount before checkout")

            # self.Patient_Name.room_ids.no_of_bed =  self.Patient_Name.room_ids.no_of_bed +1
#                 # bed_list.append(data.code)
#
#         # for i in self.beds_ids:
#         #     if i.beds_ids.code == self.beds_name:
#         #         i.state = 'free'
#         # # for i in self.Patient_Name:
#         #     if self. Patient_Name.beds_ids.code == self.beds_name:
#         #      self .Patient_Name.beds_ids.state = 'free'
#
#         # res.room_ids.no_of_bed = res.room_ids.no_of_bed - 1
#         # if res.room_ids.no_of_bed == 0:
#         #     res.room_ids.state = 'busy'
#         self.sum = res.no_of_patient_logout+1
#         res.no_of_patient_logout = self.sum
        # res.no_of_patient_logout = sum+1
        return res
#
