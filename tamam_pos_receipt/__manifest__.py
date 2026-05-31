{
    "name": "Tamam POS Receipt",
    "summary": "Customize the POS receipt layout for Tamam",
    "version": "19.0.1.0.4",
    "category": "Sales/Point of Sale",
    "author": "Baraka",
    "license": "LGPL-3",
    "depends": ["pos_restaurant"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "tamam_pos_receipt/static/src/app/screens/receipt_screen/receipt/tamam_order_receipt.xml",
            "tamam_pos_receipt/static/src/app/screens/receipt_screen/receipt/tamam_order_receipt.scss",
        ],
    },
    "installable": True,
    "application": False,
}
