# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MasterDataCategory(models.Model):
    _name = "masterdata.category"
    _description = "Master Data Category"

    name = fields.Char(required=True,string='Name')
    idcode = fields.Char(required=True,string='Code')