{
    'name': "Backend SBA debranding",
    'version': '1.0.0',
    'author': 'SBA Glukhov',
    'license': 'GPL-3',
    'category': 'Debranding',
    'website': 'https://sba-group.ru',
    'depends': ['web', 'share', 'disable_openerp_online', 'mail_delete_sent_by_footer'],
    'qweb': [
        'theme_templ.xml',
        ],
    'auto_install': False,
    'installable': True
}
