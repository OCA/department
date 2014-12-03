# -*- coding: utf-8 -*-
from openerp import models, fields, api


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    def _get_my_department(self):
        my_user = self.env['res.users'].browse(self.env.uid)
        return my_user.employee_ids[0].department_id


    @api.model
    def _prepare_purchase_order(self, requisition, supplier):
        """Propagate transport documents from tender to RFQ"""

        values = super(PurchaseRequisition, self
                       )._prepare_purchase_order(requisition, supplier)
        values['department_id'] = requisition.department_id.id
        return values

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)
