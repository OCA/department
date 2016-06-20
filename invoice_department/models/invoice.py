# -*- coding: utf-8 -*-
# Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def _get_default_department(self):
        department_id = self.env['hr.department']
        for employee in self.env.user.employee_ids:
            if employee and employee.department_id:
                department_id = employee.department_id
                break
        return department_id

    department_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department',
        default=_get_default_department,
    )
