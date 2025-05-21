# id-erp

This repository contains a prototype Frappe app named **Print Shop** used to manage digital printing products and workflows.

The `print_shop` directory is the application root. Place it inside the `apps` folder of your bench instance and run:

```bash
bench --site your_site install-app print_shop
```

The app provides DocTypes for product configuration, optional items and customer rules along with pricing controllers.

To run the basic test suite:

```bash
pytest -q
```

This project is released under the [MIT License](LICENSE).


