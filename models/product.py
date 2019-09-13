# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp


class Product(models.Model):
    _inherit = 'product.product'

    @api.depends('commission_price_template', 'price_extra')
    def _compute_product_commission_price(self):
        to_uom = None
        if 'uom' in self._context:
            to_uom = self.env['uom.uom'].browse([self._context['uom']])

        for product in self:
            if to_uom:
                commission_price_template = product.uom_id._compute_price(product.commission_price_template, to_uom)
            else:
                commission_price_template = product.commission_price_template
            product.commission_price_product = commission_price_template + product.price_extra

    def _set_product_commission_price(self):
        for product in self:
            if self._context.get('uom'):
                value = self.env['uom.uom'].browse(self._context['uom'])._compute_price(product.commission_price_product, product.uom_id)
            else:
                value = product.commission_price_product
            value -= product.price_extra
            product.write({'commission_price_template': value})

    commission_price_product = fields.Float(compute='_compute_product_commission_price', digits=dp.get_precision('Product Price'), inverse='_set_product_commission_price', string='Commission Price')
