# -*- coding: utf-8 -*-

from odoo import models, fields, api


class covid_19(models.Model):
    _name = 'covid_19.covid_19'
    _order = 'id desc'

    source = fields.Char("Source", required=True)
    date = fields.Datetime(default=lambda self:fields.Datetime.now())

    country_id = fields.Many2one("res.country", required=True)
    infected = fields.Integer("Number of infected", required=True, default=0)
    recovered = fields.Integer("Number of recovered", required=True, default=0)
    deceased = fields.Integer("Number of deceased", required=True, default=0)
    total_infected = fields.Integer("Total infected"
                                     , compute='set_total_infected', required=True, default=0)
    total_recovered = fields.Integer("Total recovered"
                                     , compute="set_total_recovered", required=True, default=0)
    total_deceased = fields.Integer("Total deceased "
                                     , compute="set_total_deceased", required=True, default=0)

    @api.depends('infected')
    def set_total_infected(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            # print(self.date)
            records = self.search(domain)
            print('records')
            print(records)
            Infected = records.mapped('infected')
            print("Infected.....")
            print(Infected)
            print(sum(Infected))
            data.total_infected = sum(Infected) + data.infected

    @api.depends('recovered')
    def set_total_recovered(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            records = self.search(domain)
            print('records')
            print(records)
            Recovered = records.mapped('recovered')
            print("Recovered.....")
            print(Recovered)
            print(sum(Recovered))
            data.total_recovered = sum(Recovered) + data.recovered

    @api.depends('deceased')
    def set_total_deceased(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            records = self.search(domain)
            print('records')
            print(records)
            Deceased = records.mapped('deceased')
            print("Deceased.....")
            print(Deceased)
            print(sum(Deceased))
            data.total_deceased = sum(Deceased) + data.deceased
