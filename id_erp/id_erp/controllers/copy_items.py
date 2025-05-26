# Autore: idstudio AI
# Email: ai@idstudio.org
import frappe


def get_default_fieldnames():
    if not hasattr(get_default_fieldnames, 'cache'):
        df = frappe.get_all('DocField', filters={'parent': 'Item'}, fields=['fieldname'])
        get_default_fieldnames.cache = {d.fieldname for d in df}
    return get_default_fieldnames.cache


def copy_custom_fields(source_doctype, source_name, target_item):
    """Copy custom fields from a source item to the given target item."""
    default_fields = get_default_fieldnames()
    source_item = frappe.get_doc(source_doctype, source_name)
    for fieldname, value in source_item.get_valid_dict().items():
        if fieldname not in default_fields and fieldname in target_item.as_dict():
            target_item.set(fieldname, value)


def copy_from_quotation(sales_order, method=None):
    """Ensure custom fields are copied from Quotation Items when creating a Sales Order."""
    for item in sales_order.items:
        if not item.get('prevdoc_docname'):
            continue
        copy_custom_fields('Quotation Item', item.prevdoc_docname, item)


def copy_from_sales_order(delivery_note, method=None):
    """Copy custom fields from Sales Order Items to Delivery Note Items."""
    for item in delivery_note.items:
        if not item.get('so_detail'):
            continue
        copy_custom_fields('Sales Order Item', item.so_detail, item)
