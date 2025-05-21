import builtins
import types

import pytest

import print_shop.controllers.pricing as pricing


def test_calculate_price_simple():
    config = types.SimpleNamespace(
        tipo_prodotto=pricing.PRODUCT_TYPE_PIECE,
        prezzo_base=10,
    )
    item = types.SimpleNamespace(qty=2, base=None, altezza=None, lunghezza=None)
    price = pricing.calculate_price(config, item, [])
    assert price == 20
