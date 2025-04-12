{
    "name":"real_estate",
    'version': '1.0',
    "author":"Mah_Yousry",
    "description":"Real Estate Management System",
    'depends': [
        'base','sale','account','mail','contacts'
        ],
    "data" : [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/data.xml",
        "views/base_menu.xml",
        "views/property_view.xml",
        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
        "views/res_partner_view.xml",
        "views/building_view.xml",
        "views/property_history.xml",
        "views/account_move_view.xml",
        "wizard/change_state_wizard_view.xml",
        "reports/property_report.xml",
    ],
    "assets" : {
        "web.assets_backend" : [
            'real_estate/static/src/css/property.css',
            'real_estate/static/src/components/listView/listView.css',
            'real_estate/static/src/components/listView/listView.js',
            'real_estate/static/src/components/listView/listView.xml',
        ],
        "web.report_assets_common" : [
            'real_estate/static/src/css/font.css',
        ],
    },
    "application" : True,
    'odoo_version': '18.0', 
}