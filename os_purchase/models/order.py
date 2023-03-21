# -*- coding: utf-8 -*-

from odoo import api, fields, models

class OSPurchaseOrder(models.Model):
    _name = 'os_purchase.order'
    _description = "Sneaker Purchase Order"

    name = fields.Char(string='Name')
    ref = fields.Char(required=True,string='Reference')
    product_id = fields.Many2one('masterdata.product', string='Choose Product',required=True)
    price = fields.Integer(string='Price',readonly=True)
    qty = fields.Integer(string='Qty',required=True)
    notes = fields.Char(string='Notes')

    @api.onchange("product_id")
    def _onchange_product_id(self):
        self.price = self.product_id.price
