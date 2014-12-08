# -*- coding: utf-8 -*-
# Author: Leonardo Pistone
# Copyright 2014 Camptocamp SA (http://www.camptocamp.com)
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

from openerp.tests.common import TransactionCase


class TestPropagateDepartment(TransactionCase):
    def setUp(self):
        super(TestPropagateDepartment, self).setUp()

        self.PO = self.env['purchase.order']

        self.po = self.PO.new({
            'company_id': self.browse_ref('base.main_company')
        })
        self.dep_rd = self.browse_ref('hr.dep_rd')

    def test_it_propagates_empty_department(self):
        invoice_data = self.PO._prepare_invoice(self.po, [])

        self.assertFalse(invoice_data.get('department_id'))

    def test_it_propagates_a(self):
        self.po.department_id = self.dep_rd
        invoice_data = self.PO._prepare_invoice(self.po, [])

        self.assertEqual(self.dep_rd.id, invoice_data.get('department_id'))
