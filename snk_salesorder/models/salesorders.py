# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SalesOrders(models.Model):
    _name = "simple_sales.orders"
    _description = "Sales Order"

    idcode = fields.Char(string='Code', required=True, copy=False, readonly=True, 
                          default=lambda self: _('New'))
    product_id = fields.Many2one('masterdata.product', string='Choose Product')
    qty_order = fields.Integer(string='Qty order',required=True)
    price = fields.Integer(string='Price',related='product_id.price',required=True)
    remark = fields.Char(string='Remark')
    amount = fields.Integer(string='Amount',store=True)

    @api.onchange('qty_order')
    def _onchange_qty_order(self):
        self.amount = self.qty_order*self.product_id.price

    @api.model
    def create(self, vals):
        if vals.get('idcode', _('New')) == _('New'):
            vals['idcode'] = self.env['ir.sequence'].next_by_code('simple_sales.orders') or _('New')
        res = super(SalesOrders, self).create(vals)
        return res