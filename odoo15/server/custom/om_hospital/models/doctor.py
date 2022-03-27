# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, api


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"

    doctor_name = fields.Char(string='Name', required=True, translate=True, tracking=True)

    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    image = fields.Binary(string="Patient Image")


