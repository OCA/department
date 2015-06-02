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

{
    "name": "Hours Blocks Department Categorization",
    "version": "1.0",
    "category": "Generic Modules/Projects & Services",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    "description": """
Hours Blocks Department Categorization
======================================

Replicate Department from invoice to Hours Blocks.
Add it to corresponding tree, search and form views.

This module is a part (OCA/department side) of the fix related to
https://github.com/OCA/project-service/issues/33
""",
    "depends": [
        "invoice_department",
        "analytic_hours_block",     # OCA/project-service/analytic_hours_block
    ],
    "data": [
        "hours_block_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "active": True,
}
