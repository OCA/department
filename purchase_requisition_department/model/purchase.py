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


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    def _get_my_department(self):
        employees = self.env.user.employee_ids
        return (employees[0].department_id if employees
                else self.env['hr.department'])

    @api.model
    def _prepare_purchase_order(self, requisition, supplier):
        """Propagate transport documents from tender to RFQ"""

        values = super(PurchaseRequisition, self
                       )._prepare_purchase_order(requisition, supplier)
        values['department_id'] = requisition.department_id.id
        return values

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)
