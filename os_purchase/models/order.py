# -*- coding: utf-8 -*-

from odoo import fields, models


class OSPurchaseOrder(models.Model):
    _name = 'os_purchase.order'
    _rec_name = 'name'

    name = fields.Char("Name")
