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
