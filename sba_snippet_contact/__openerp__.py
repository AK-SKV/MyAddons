# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
# and module copyright (C) 2016 SBA (<http://sba-group.ru>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "SBA Contact Snippet",
    'summary': """SBA Contact Snippet""",
    'description': """Provide custom contact snippet""",
    'author': "bloopark systems GmbH & Co. KG & SBA",
    'website': "http://sba-group.ru",
    'license': 'AGPL-3',
    'category': 'Modal',
    'version': '1.0',

    'depends': [
        'website_partner',
        'crm'
    ],
    'data': [
        'views/form.xml'
    ],

}
