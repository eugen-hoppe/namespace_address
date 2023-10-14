from app.namespace.licence_plate.domain.de import LPlateDE
from devtools import debug

INPUT = "EHX.CD1419E@DE.licence-plate:2310"
licence_plate = LPlateDE(tld="ehoppe.com")
licence_plate.load(INPUT)

debug(licence_plate.slug())
# ehx.cd1419e@de.licence-plate.ehoppe.com:2310
# |_________||__||___________| |________||____|
#      |      |        |           |        |
#      |    domain     | namespce_provider* |
# licence_plate   subject*               version*
#
# *optional

debug(licence_plate)

