# -*- coding: utf-8 -*-
# Author: Leonardo Pistone
# Copyright 2014-2015 Camptocamp SA (http://www.camptocamp.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public Lice
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _get_my_department(self):
        employees = self.env.user.employee_ids
        return (employees[0].department_id if employees
                else self.env['hr.department'])

    @api.cr_uid_context
    def _prepare_invoice(self, cr, uid, order, line_ids, context=None):
        result = super(PurchaseOrder, self)._prepare_invoice(cr, uid, order,
                                                             line_ids, context)
        result['department_id'] = order.department_id.id
        return result

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    department_id = fields.Many2one(related='order_id.department_id',
                                    store=True)
