import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-department",
    description="Meta package for oca-department Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-analytic_base_department',
        'odoo8-addon-analytic_department',
        'odoo8-addon-crm_department',
        'odoo8-addon-framework_agreement_department',
        'odoo8-addon-invoice_department',
        'odoo8-addon-project_department',
        'odoo8-addon-project_issue_department',
        'odoo8-addon-project_task_department',
        'odoo8-addon-purchase_department',
        'odoo8-addon-purchase_requisition_department',
        'odoo8-addon-sale_department',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
