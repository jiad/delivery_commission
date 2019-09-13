# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    commission_rate = fields.Float(string="Commission Rate", default=1)
    commission_fixed = fields.Float(string="Commission Fixed")

    @api.one
    @api.constrains('commission_rate')
    def check_commission_rate(self):
        if self.commission_rate <= 0:
            raise ValidationError('Commission Rate must be greater then 0!!')