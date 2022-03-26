# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointments"

    name = fields.Char(string='Order Reference', required=True, translate=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient', required=True)
    age = fields.Integer(string='Age', related="patient_id.age", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male', required=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')],
                             default='draft'
                             , string="Status", tracking=True)
    note = fields.Text(string='Description', tracking=True)
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Checkup")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        # print("success override create method")
        if not vals.get("note"):
            vals["note"] = 'New Appointment'
        if vals.get('name', _('New')) == _("New"):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
            else:
                self.note = ''
        else:
            self.gender = ''
