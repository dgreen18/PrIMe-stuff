###Reactions PrIMe protocol

from lxml import etree
xmlns="http://purl.org/NET/prime/"
xsi="http://www.w3.org/2001/XMLSchema-instance"
primeID="r00000011"
schemaLocation="http://warehouse.primekinetics.org/schema/reaction.xsd"
NSMAP = {None: xmlns}
root = etree.Element('{' + xmlns + '}reaction', nsmap=NSMAP)
root.attrib["{" + xsi + "}schemaLocation"] = schemaLocation
# root.attrib["{" + xmlns + "}xsi"] = xsi
root.attrib["primeID"] = primeID
child1=etree.SubElement(root,'copyright')
child1.text="primekinetics.org 2005"
child2=etree.SubElement(root,'reactants')
preferredKey="C10H11"
primeID="s00000275"
child21=etree.SubElement(child2,'speciesLink')
child21.attrib["preferredKey"]=preferredKey
child21.attrib["primeID"]=primeID
child21.text="-1"
primeID="s00000276"
child22=etree.SubElement(child2,'speciesLink')
child22.attrib["preferredKey"]=preferredKey
child22.attrib["primeID"]=primeID
child22.text="1"
print etree.tostring(root, pretty_print=True)