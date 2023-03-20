# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalesOrders(models.Model):
    _name = "simple_sales.orders"
    _description = "Sales Order"

    idcode = fields.Char(required=True,string='Code')
    product_id = fields.Many2one('masterdata.product', string='Choose Product')
    qty_order = fields.Integer(string='Qty order',required=True)
    price = fields.Integer(string='Price',related='product_id.price',required=True)
    remark = fields.Char(string='Remark')
    amount = fields.Integer(string='Amount',store=True)

    @api.onchange('qty_order')
    def _onchange_qty_order(self):
        self.amount = self.qty_order*self.product_id.price

    # name = fields.Char(string='Account Type', required=True, translate=True)
    # include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
    # type = fields.Selection([
    #     ('other', 'Regular'),
    #     ('receivable', 'Receivable'),
    #     ('payable', 'Payable'),
    #     ('liquidity', 'Liquidity'),
    # ], required=True, default='other',
    #     help="The 'Internal Type' is used for features available on "\
    #     "different types of accounts: liquidity type is for cash or bank accounts"\
    #     ", payable/receivable is for vendor/customer accounts.")