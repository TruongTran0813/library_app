{
    "name": "Library Management 3",
    "summary": "Test21",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing" "/Odoo-14-Development-Essentials",
    "version": "14.0.1.0.0",
    "category": "Services/Library",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
        "reports/library_book_report.xml",
        "reports/library_publisher_report.xml",
    ],
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml",
    ],
    "application": True,
}
