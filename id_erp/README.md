# ID ERP

Frappe/ERPNext app to manage digital printing sales and production.

## Features

- Product configuration with dimensional fields
- Pricing rules based on product type and customer group
- Optional items with fixed or variable cost
- Data continuity across quotation, sales order and work orders
- Basic JavaScript hooks for form customization

## Installation

From your bench directory:

```bash
bench get-app id_erp /path/to/id-erp
bench --site yoursite install-app id_erp
```

## Update

```bash
bench --site yoursite reinstall --force
```

## Troubleshooting

Ensure the app directory is `apps/id_erp/id_erp/` with `__init__.py`, `hooks.py`, and `modules.txt` present.

## Uninstall

```bash
bench --site yoursite uninstall-app id_erp
```

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE).

