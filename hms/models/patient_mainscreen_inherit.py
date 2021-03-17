from odoo import models, fields, api


# from odoo.exceptions import ValidationError


# class hms section
class patient_mainscreen_inherit(models.Model):
    _inherit = 'medical.patient'
    # _rec_name = 'full_name'
    patient_id = fields.Many2one('res.partner', domain=[('is_patient', '=', True)], string="Patient first name",
                                 required=True)
    # patient_id = fields.Many2one(string='First name')
    patient_second_name = fields.Char(string='Second name', help=" patient Second Name", required=True)
    patient_third_name = fields.Char(string='Third name', help="Third Name", required=True)
    patient_fourth_name = fields.Char(string='Fourth name', help="Fourth Name", required=True)
    name = fields.Char(string='ID Patient', readonly=True)

    # name = fields.Char(string="Full Name",compute="get_patient_name")

#     update the name
    @api.multi
    def name_get(self):
        res = super(patient_mainscreen_inherit, self).name_get()
        data = []
        for patient in self:
            display_value = ''
            display_value += patient.patient_id.name or ""
            display_value += ' '
            display_value += patient.patient_second_name or ""
            display_value += ' '
            display_value += patient.patient_third_name or ""
            display_value += '   '
            display_value += patient.patient_fourth_name or " "
            # display_value += '   '
            # display_value += '   '
            display_value += '['
            display_value += patient.name
            display_value += ']'

            data.append((patient.id, display_value))
        return data
# ----------------------------------------------------------------------
# @api.one
# # @api.depends('patient_second_name','patient_third_name')
# def get_patient_name(self):
#     txt = self.patient_second_name+"."+self.patient_third_name
#     x = str(txt)
#     self.name = x
#     pass
#     # self.name = self.patient_id.name+ " "+self.patient_second_name+" "+self.patient_third_name
#     # How know who called the method?
#     # print(self.full_name)
# -----------------------------------------------------------------------

# @api.one
# # @api.depends('patient_second_name','patient_third_name','patient_id.name')
# def get_patient_name(self):
#     # for rec in self:
#     # """
#     # function to calculate the full name for the patient
#     # """
#         self.name =self.patient_id.name+" "+self.patient_second_name+" "+self.patient_third_name
#         print(self.name)
#         print(self.full_name)
#         print(str(self.full_name))
#         return self.name

# str(self.name)
# self.name = self.patient_id.name+' '+self.patient_second_name+' '+self.patient_third_name

# ------------------------------------------------------------------------------------------------


# @api.constrains('patient_id.name')
# def _size_code(self):
#     for x in self:
#         x = self.patient_id.name
#         text = str(x)
#         maxsplit = 3
#         txt_list = text.split(" ",maxsplit)
#         if len(txt_list)!=maxsplit+1:
#             raise ValidationError("Please enter your name trilogy")
#     # self.patient_id.name
# @api.one
# def get_patient_name(self):
#     """
#     function to calculate the full name for the patient
#     """
#     self.name = self.patient_id.name+" "+self.patient_second_name+" "+self.patient_third_name
#     str(self.name)
#     # self.name = self.patient_id.name+' '+self.patient_second_name+' '+self.patient_third_name
