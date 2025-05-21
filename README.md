# Print Shop

This repository contains a prototype Frappe app named **Print Shop** for ERPNext.
It manages digital printing products and workflows.

## Features

- Product configuration with dimensional fields
- Pricing rules based on product type and customer group
- Optional items with fixed or variable cost
- Data continuity across quotation, sales order and work orders
- Basic JavaScript hooks for form customization

## Installation

From your bench instance, install the app:

```bash
bench get-app /path/to/this/repository
bench --site your_site install-app print_shop
```
