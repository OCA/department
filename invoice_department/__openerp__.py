# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Invoices with Department Categorization',
    'version': '8.0.1.0.0',
    'category': 'Generic Modules/Sales & Purchases',
    'description': """
Add the department on Invoices as well as the related
 filter and button in the search form.""",
    'author': "Camptocamp,Odoo Community Association (OCA)",
    'website': 'http://camptocamp.com',
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
