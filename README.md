# id-erp

This repository contains a prototype Frappe app named **Print Shop** used to manage digital printing products and workflows.

The `print_shop` directory holds the Frappe app code.  Key features implemented so far:

- Product configuration with dimensional fields and pricing per type (m², m/l, piece, apparel)
- Rules for minimum quantities or order values per customer group
- Optional items with fixed or variable costs
- Automatic pricing during Sales Order validation
- Creation of an initial **Work Milestone** document when the order is submitted
