# -*- coding: utf-8 -*-

from odoo import fields, models


class OSInvoiceInvoice(models.Model):
    _name = 'os_invoice.invoice'
    _rec_name = 'name'

    name = fields.Char("Name")
