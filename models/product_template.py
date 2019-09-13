# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    commission_price_template = fields.Float('Commission Price', default=1.0, digits=dp.get_precision('Product Price'))
    commission_price_product = fields.Float('Commission Price', related='commission_price_template', readonly=False, digits=dp.get_precision('Product Price'))
