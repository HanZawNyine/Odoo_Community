# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    reference = fields.Char(string='Reference', required=True, translate=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')],
                             default='draft', string="Status", tracking=True)
    responsible_id = fields.Many2one(comodel_name='res.partner', string='Responsible')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    @api.model
    def default_get(self, fields):
        result = super(HospitalPatient,self).default_get(fields)
        result['note'] = 'Set Default Gender Method'
        return result
