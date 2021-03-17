{'name': 'Library Management Application',
 'description': 'Library books, members and book borrowing.',
 'author': 'Daniel Reis',
 'depends': ['base'],
 'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/book_view.xml',
    'views/publishers.xml',
    'views/catagories.xml',
    'views/book_list_template.xml',
     'data/booksequanse.xml',
    # 'report/book_profile.xml',
    # 'report/book_report.xml'

 ],
 'application': True,
 'installable': True,
 }
