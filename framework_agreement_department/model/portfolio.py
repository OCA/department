# Author: Leonardo Pistone
# Copyright 2015 Camptocamp SA (http://www.camptocamp.com)
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

from openerp import models, fields


class Portfolio(models.Model):
    _inherit = 'framework.agreement.portfolio'

    def _get_my_department(self):
        employees = self.env.user.employee_ids
        return (employees and employees[0].department_id or
                self.env['hr.department'])

    department_id = fields.Many2one('hr.department', 'Department',
                                    default=_get_my_department)

    _sql_constraints = [
        ('uniq_portfolio',
         'unique(supplier_id, company_id, department_id)',
         'There can be only one portfolio '
         'per supplier, department and company.'),
    ]
