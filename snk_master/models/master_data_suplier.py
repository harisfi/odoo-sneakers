# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MasterDataSuplier(models.Model):
    _name = "masterdata.suplier"
    _description = "Master Data Suplier"

    name = fields.Char(required=True,string='Name Suplier')
    idcode = fields.Char(required=True,string='Code')