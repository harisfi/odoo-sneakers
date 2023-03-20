# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MasterDataProduct(models.Model):
    _name = "masterdata.product"
    _description = "Master Data Product"

    name = fields.Char(required=True,string='Name Product')
    idcode = fields.Char(required=True,string='Code')
    price = fields.Integer(required=True,string='Price Product')
    category_id = fields.Many2one('masterdata.category', string='Category')