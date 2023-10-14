from app.namespace.licence_plate.domain.de import LPlateDE

INPUT = "EH.CD1419@DE:2310"
licence_plate = LPlateDE(tld="ehoppe.com")
licence_plate.load(INPUT)
print(licence_plate.slug())
