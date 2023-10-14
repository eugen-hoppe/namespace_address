from licence_plate.domain.de import LPlateDE


INPUT = "B.CD1234@DE:2310"
licence_plate = LPlateDE(tld="ehoppe.com")
licence_plate.load(INPUT)
print(licence_plate.slug())
