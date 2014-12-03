# -*- coding: utf-8 -*-
from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _get_my_department(self):
        my_user = self.env['res.users'].browse(self.env.uid)
        return my_user.employee_ids[0].department_id

    @api.cr_uid_context
    def _prepare_invoice(self, cr, uid, order, line_ids, context=None):
        result = super(PurchaseOrder, self)._prepare_invoice(cr, uid, order,
                                                             line_ids, context)
        return result

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    department_id = fields.Many2one(related='order_id.department_id',
                                    store=True)
