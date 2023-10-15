from app.namespace.licence_plate.domain.de import LPlateDEv2310 as LPlateDE
from devtools import debug


lp_de = LPlateDE().load("eh.cd2211e@de")


debug(lp_de.slug())  # ->
# ehx.cd1419e @ de . licence-plate . ehoppe.com : 2310
# |__________| |__| |_____________| |__________| |____|
#      |        |          |             |         |
#      |      domain       |   namespace_provider* |
# licence_plate        subject*                version*
#
# *optional


debug(lp_de)  # ->
# LPlateDEv2310(
#     version=2310,
#     domain=<Domain.DE: 1>,
#     subject='licence-plate',
#     prefix='EH',
#     tld='ehoppe.com',
#     is_valid=True,
#     sep=<enum 'Separator'>,
#     suffix=['CD', '1419', 'E',],
# )

debug(lp_de.licence_plate())  # -> EH-CD1419E
