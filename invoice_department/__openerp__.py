# -*- coding: utf-8 -*-
# Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Invoices with Department Categorization',
    'version': '8.0.1.0.0',
    'category': 'Generic Modules/Sales & Purchases',
    'author': "Camptocamp,"
              "Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'depends': [
        'account',
        'hr'
    ],
    'data': [
        'views/invoice_view.xml',
        'report/account_invoice_report_view.xml',
    ],
    'installable': True,
}
