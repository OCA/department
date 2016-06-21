# -*- coding: utf-8 -*-
# © 2016 KMEE - Luis Felipe Mileo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    department_id = fields.Many2one(
        'hr.department',
        'Department', readonly=True)

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + \
            ", sub.department_id as department_id"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + \
            ", ai.department_id as department_id"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + \
            ", ai.department_id"
