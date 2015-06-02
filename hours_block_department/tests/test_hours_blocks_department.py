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

import openerp.tests.common as common


class TestReplicateInvoiceDepartmentOnHoursBlock(common.TransactionCase):

    def setUp(self):
        super(TestReplicateInvoiceDepartmentOnHoursBlock, self).setUp()
        self.ai_model = self.registry('account.invoice')
        self.hb_model = self.registry('account.hours.block')

        self.ai1 = self.ref('analytic_hours_block.demo_invoice_4_hb')
        self.hb1 = self.ref('analytic_hours_block.demo_hb')
        self.hd1 = self.ref('hr.dep_ps')

        self.context = {}

    def test_change_period(self):
        cr, uid, context = self.cr, self.uid, self.context
        ai_model, hb_model = self.ai_model, self.hb_model

        ai = ai_model.browse(cr, uid, self.ai1, context=context)
        hb = hb_model.browse(cr, uid, self.hb1, context=context)

        # 1. Verify demo data
        self.assertFalse(ai.department_id.id,
                         "Wrong demo data: "
                         "test_invoice_1.department_id should be False")
        self.assertFalse(hb.department_id.id,
                         "Wrong demo data: "
                         "demo_hb_4_test_invoice_1.department_id "
                         "should be False")

        # 2. Change Invoice Department
        vals = {'department_id': self.hd1}
        ai.write(vals)
        hb = hb_model.browse(cr, uid, self.hb1, context=context)
        self.assertEqual(
            hb.department_id.id, self.hd1,
            "Replicate Department on Invoice fails: "
            "demo_hb_4_test_invoice_1.department_id "
            "should be %s" % self.hd1)

        # 3 Rollback the change
        vals = {'department_id': False}
        ai.write(vals)
        hb = hb_model.browse(cr, uid, self.hb1, context=context)
        self.assertFalse(
            hb.department_id.id,
            "Replicate Department on Invoice fails: "
            "demo_hb_4_test_invoice_1.department_id "
            "should be False")
        pass
