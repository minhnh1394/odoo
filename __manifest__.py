{    
    'name': 'Student Management',    
    'description': 'Manage student\'s general infomation.',    
    'author': 'NHM',
    'website':'https://github.com/minhnh1394/student_app.git',
    'depends': ['base'],  
    'license':'AGPL-3',
    'data': [
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/student_menu.xml',
        'views/info_view.xml',
    ],  
    'application': True, 
    'installable':True,
} 