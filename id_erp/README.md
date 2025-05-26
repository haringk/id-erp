# ID ERP

Custom app for Frappe/ERPNext 14 to manage digital printing sales and production.

## Installation
1. Navigate to your bench directory.
2. Get the app from this repository:
   ```bash
   bench get-app id_erp [REPO_URL]
   ```
3. Install the app on your site:
   ```bash
   bench --site yoursite.local install-app id_erp
   ```

## Update
```bash
bench --site yoursite.local update --patch && bench --site yoursite.local migrate
```

## Troubleshooting
- Check `bench --site yoursite.local logs` for errors.
- Run `bench migrate` after adding custom fields.

## Uninstall
```bash
bench --site yoursite.local uninstall-app id_erp
```

## Data Migration
If upgrading from an earlier version of id_erp, run:
```bash
bench --site yoursite.local migrate
```

## Dependencies
- Frappe >= 14
- ERPNext 14

This app copies custom item fields automatically between Quotation, Sales Order and Delivery Note.
