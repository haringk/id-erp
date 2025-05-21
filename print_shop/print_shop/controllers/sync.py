import frappe


def copy_dimensions_from_quotation(doc, method):
    """Ensure custom dimension fields are copied from Quotation Item."""
    for item in doc.get("items", []):
        if item.get("prevdoc_docname") and item.get("prevdoc_detail_docname"):
            data = frappe.db.get_value(
                "Quotation Item",
                item.prevdoc_detail_docname,
                ["base", "altezza", "lunghezza"],
                as_dict=True,
            )
            if data:
                if not item.get("base"):
                    item.base = data.base
                if not item.get("altezza"):
                    item.altezza = data.altezza
                if not item.get("lunghezza"):
                    item.lunghezza = data.lunghezza
