# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "print_shop"
app_title = "Print Shop"
app_publisher = "Your Company"
app_description = "Digital printing management"
app_email = "info@example.com"
app_license = "MIT"

# Includes
doctype_js = {
    "Sales Order": "public/js/sales_order.js",
}

doc_events = {
    "Sales Order": {
        "validate": "print_shop.controllers.pricing.validate_sales_order",
    },
}
