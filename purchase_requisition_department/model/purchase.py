# -*- coding: utf-8 -*-
from openerp import models, fields


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    def _get_my_department(self):
        my_user = self.env['res.users'].browse(self.env.uid)
        return my_user.employee_ids[0].department_id

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)


class PurchaseRequisitionLine(models.Model):
    _inherit = 'purchase.requisition.line'

    department_id = fields.Many2one(related='requisition_id.department_id',
                                    store=True)
