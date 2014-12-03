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
