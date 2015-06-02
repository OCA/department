# -*- coding: utf-8 -*-
##############################################################################
#
# This file is part of hours_block_department,
# an Odoo module.
#
# Authors: ACSONE SA/NV (<http://acsone.eu>)
#
# hours_block_department is free software:
# you can redistribute it and/or modify it under the terms of the GNU
# Affero General Public License as published by the Free Software
# Foundation,either version 3 of the License, or (at your option) any
# later version.
#
# hours_block_department is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with hours_block_department.
# If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields


class AccountHoursBlock(orm.Model):

    _inherit = "account.hours.block"

    def _get_hours_blocks_from_invoices(self, cr, uid, ids, context=None):
        # self is an instance of account.invoice here
        res = self.pool.get('account.hours.block').search(
            cr, uid, [('invoice_id', 'in', ids)], context=context)
        return res

    _columns = {
        'department_id': fields.related(
            'invoice_id', 'department_id',
            type='many2one', relation='hr.department',
            string='Department',
            store={
                'account.hours.block': (
                    lambda self, cr, uid, ids, c=None: ids,
                    ['invoice_id'], 10),
                'account.invoice': (
                    _get_hours_blocks_from_invoices,
                    ['department_id'], 10),
            },
            readonly=True),
    }
