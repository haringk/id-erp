# Autore: idstudio AI
# Email: ai@idstudio.org
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "id_erp"
app_title = "ID ERP"
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
        "validate": "id_erp.controllers.pricing.validate_sales_order",
    },
}
