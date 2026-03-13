

import xmltodict
with open('pyscripts/r1.xml') as file:
    xml_data = file.read()

data = xmltodict.parse(xml_data)
print(data)
