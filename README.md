# ID ERP

**ID ERP** is a minimal Frappe/ERPNext application to manage digital printing workflows.

## Installation

From your bench directory run:

```bash
bench get-app id_erp https://github.com/haringk/id-erp.git
bench --site yoursite install-app id_erp
```

## Update

```bash
bench --site yoursite reinstall --force
```

## Troubleshooting

Ensure your bench environment is running ERPNext 14 and that `id_erp` exists in the `apps` directory.

## Uninstall

```bash
bench --site yoursite uninstall-app id_erp
```

## License

MIT
