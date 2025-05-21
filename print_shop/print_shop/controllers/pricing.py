import frappe

PRODUCT_TYPE_MQ = "Mq"
PRODUCT_TYPE_ML = "Ml"
PRODUCT_TYPE_PIECE = "Pezzo"
PRODUCT_TYPE_ABBIGLIAMENTO = "Abbigliamento"


def copy_dimensions_from_quotation(doc, method):
    """Ensure dimensional fields are carried over from the originating Quotation."""
    for item in doc.items:
        if (getattr(item, "prevdoc_doctype", None) == "Quotation" and
                getattr(item, "prevdoc_detail_docname", None)):
            try:
                q_item = frappe.get_doc("Quotation Item", item.prevdoc_detail_docname)
            except frappe.DoesNotExistError:
                continue
            for field in ("base", "altezza", "lunghezza"):
                if not getattr(item, field, None) and hasattr(q_item, field):
                    setattr(item, field, getattr(q_item, field))



def validate_sales_order(doc, method):
    for item in doc.items:
        config = frappe.get_doc("Product Configuration", item.item_code)
        optional_items = get_optionals(item)
        item.base_price = calculate_price(config, item, optional_items)
        enforce_minimums(doc.customer_group, item)


def get_optionals(item):
    optionals = []
    if hasattr(item, "optional_items"):
        for row in item.optional_items:
            optionals.append(frappe.get_doc("Optional Item", row.optional_item))
    return optionals


def calculate_price(config, item, optionals):
    quantity = item.qty or 1
    base_price = 0

    if config.tipo_prodotto == PRODUCT_TYPE_MQ:
        area = (item.base or 0) * (item.altezza or 0) / 10000
        base_price = area * config.prezzo_base * quantity
    elif config.tipo_prodotto == PRODUCT_TYPE_ML:
        base_price = (item.lunghezza or 0) / 100 * config.prezzo_base * quantity
    elif config.tipo_prodotto == PRODUCT_TYPE_PIECE:
        base_price = config.prezzo_base * quantity
    elif config.tipo_prodotto == PRODUCT_TYPE_ABBIGLIAMENTO:
        base_price = config.prezzo_base * quantity

    for opt in optionals:
        base_price += opt.costo_fisso or 0
        if opt.costo_variabile:
            base_price += opt.costo_variabile * quantity
        if opt.minimo and base_price < opt.minimo:
            base_price = opt.minimo

    return base_price


def enforce_minimums(customer_group, item):
    rule = frappe.get_all(
        "Customer Group Rule",
        filters={"customer_group": customer_group},
        fields=["min_qty_m2", "min_value"],
        limit=1
    )
    if not rule:
        return

    rule = rule[0]

    if rule.min_qty_m2 and item.base_price < rule.min_qty_m2:
        item.base_price = rule.min_qty_m2
    if rule.min_value and item.base_price < rule.min_value:
        item.base_price = rule.min_value
