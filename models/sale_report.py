# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleReport(models.Model):
    _inherit = "sale.report"

    commission_subtotal = fields.Float(string="Commission Sub Total", readonly=True)
    commission_price = fields.Float(string="Commission Price", readonly=True)
    commission_total_line = fields.Float(string="Commission Total", readonly=True)
    price_unit = fields.Float('Unit Price', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['commission_price'] = ", l.commission_price as commission_price"
        fields['commission_subtotal'] = ", l.commission_subtotal as commission_subtotal"
        fields['commission_total_line'] = ", l.commission_total_line as commission_total_line"
        fields['price_unit'] = ", l.price_unit as price_unit"
        groupby += ", l.commission_price, l.commission_subtotal, l.commission_total_line, l.price_unit"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
