# -*- coding: utf-8 -*-
from openerp import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _get_my_department(self):
        my_user = self.env['res.users'].browse(self.env.uid)
        return my_user.employee_ids[0].department_id

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)
