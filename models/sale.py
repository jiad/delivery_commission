# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission_total = fields.Float(string="Commission Total", compute="_get_commission_total", store=True)

    @api.depends('order_line.commission_subtotal')
    def _get_commission_total(self):
        for rec in self:
            rec.commission_total = sum([line.commission_subtotal for line in rec.order_line]) + rec.partner_id.commission_fixed

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    commission_price = fields.Float(string="Commission Price")
    commission_subtotal = fields.Monetary(compute='_get_commission_subtotal', string='Commission Subtotal', readonly=True, store=True)
    commission_total_line = fields.Float(compute='_get_commission_subtotal', string="Commission Total", readonly=True, store=True)

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        for rec in self:
            rec.commission_price = rec.product_id.commission_price_product
        return res

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        res = super(SaleOrderLine, self).product_uom_change()
        for rec in self:
            rec.commission_price = rec.product_id.commission_price_product
        return res

    @api.multi
    @api.depends('product_uom_qty', 'commission_price', 'order_partner_id')
    def _get_commission_subtotal(self):
        for rec in self:
            if rec.product_uom_qty <= 0:
                rec.commission_price = 0
            rec.commission_subtotal = rec.product_uom_qty * rec.commission_price * rec.order_partner_id.commission_rate
            if len(rec.order_id.order_line) > 0:
                fixed_price = round(rec.order_partner_id.commission_fixed/float(len(rec.order_id.order_line)), 3)
            else:
                fixed_price = rec.order_partner_id.commission_fixed
            rec.commission_total_line = rec.commission_subtotal + fixed_price