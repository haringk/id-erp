# id-erp

This repository contains a prototype Frappe app named **Print Shop** used to manage digital printing products and workflows.

The `print_shop` directory includes a minimal implementation of DocTypes and pricing logic.


Frappe/ERPNext app to manage digital printing sales and production.

## Features

- Product configuration with dimensional fields
- Pricing rules based on product type and customer group
- Optional items with fixed or variable cost
- Data continuity across quotation, sales order and work orders
- Basic JavaScript hooks for form customization
- Automatic creation of Work Milestones for progress tracking

## Installation

1. Clone this repository inside your Frappe bench `apps` folder.
2. Run `bench --site your_site_name install-app print_shop`.

