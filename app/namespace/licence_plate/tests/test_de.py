import pytest
from app.namespace.licence_plate.domain.de import LPlateDE
from app.models import Domain, ErrorSnippet, Separator

# Invalid
# =======
INVALID_DOMAIN = "b.ad123@yz:2310"
INVALID_VERSION = "b.ad123@de:1000"

# Valid
# =====
IO_KEY_AT_NAMESPACE = Separator.AT + "de:2310"
IO_TEST = {
    "go.od1234": "go.od1234",
    "go.od1234e": "go.od1234e",
    "goo.d1234": "goo.d1234",
    "o.ok1234": "o.ok1234",
    "o.k1234e": "o.k1234e",
}


def test_invalid_domain():
    lp = LPlateDE()
    with pytest.raises(ValueError) as excinfo:
        lp.load(INVALID_DOMAIN)
    assert str(excinfo.value) == ErrorSnippet.DOMAIN + Domain.DE.value


def test_invalid_version():
    lp = LPlateDE()
    with pytest.raises(ValueError) as excinfo:
        lp.load(INVALID_VERSION)
    assert str(excinfo.value) == ErrorSnippet.VERSION + str(lp.version)


@pytest.mark.parametrize("io_key, expected", IO_TEST.items())
def test_valid(io_key, expected):
    lp = LPlateDE()
    lp.load(io_key + IO_KEY_AT_NAMESPACE)
    expected = expected + lp.at_namespace()
    assert lp.slug() == expected
