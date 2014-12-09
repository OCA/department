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

        self.Requisition = self.env['purchase.requisition']

        self.requisition = self.Requisition.create({})
        self.supplier = self.browse_ref('base.res_partner_1')
        self.dep_rd = self.browse_ref('hr.dep_rd')

    def test_it_propagates_empty_department(self):

        order_data = self.Requisition._prepare_purchase_order(self.requisition,
                                                              self.supplier)
        self.assertFalse(order_data.get('department_id'))

    def test_it_propagates_a_department(self):

        self.requisition.department_id = self.dep_rd
        order_data = self.Requisition._prepare_purchase_order(self.requisition,
                                                              self.supplier)

        self.assertEqual(self.dep_rd.id, order_data.get('department_id'))
