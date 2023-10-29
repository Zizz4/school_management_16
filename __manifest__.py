{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Arkana Final Task: School Management',
    'description': 'School Management',
    'category': 'Productivity',
    'author': 'Muhamad Syahril Aziz',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/security_school_access.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/gedung.xml',
        'views/kelas.xml',
        'views/murid.xml',
        'views/guru.xml',
        'views/pelajaran.xml',
        'views/absensi.xml'
    ],
    'demo': [
        'demo/school_management_demo_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}