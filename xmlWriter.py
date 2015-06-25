#!/usr/bin/env python
# coding: utf-8

# from rmgpy.molecule import Molecule
# from rmgpy.species import Species

from lxml import etree

# mol = Molecule().fromSMILES('[OH]')
# spec = Species(molecule=[mol])
# import ipdb; ipdb.set_trace()
xmlns="http://purl.org/NET/prime/"
xsi="http://www.w3.org/2001/XMLSchema-instance"
primeID="s00010102"
schemaLocation="http://warehouse.primekinetics.org/schema/species.xsd"
NSMAP = {None: xmlns}
root = etree.Element('{' + xmlns + '}chemicalSpecies', nsmap=NSMAP)
root.attrib["{" + xsi + "}schemaLocation"] = schemaLocation
# root.attrib["{" + xmlns + "}xsi"] = xsi
root.attrib["primeID"] = primeID
child1=etree.SubElement(root,'copyright')
child1.text="primekinetics.org 2005"
bibliography="b00014319"
copyrighted="true"
source="NIST"
child2 = etree.SubElement(root, 'content')
child2.attrib["bibliography"] = bibliography
child2.attrib["copyrighted"] = copyrighted
child2.attrib["source"] = source
child2.text="\nElements attributed to NIST are part of a collection copyrighted by NIST.\n"
group="prime"
type="formula"
child3=etree.SubElement(root, 'preferredKey')
child3.attrib["group"]=group
child3.attrib["type"]=type
child3.text="OH"
child4=etree.SubElement(root, 'chemicalIdentifier')
type="CASRegistryNumber"
child41=etree.SubElement(child4, 'name')
child41.attrib["source"] = source
child41.attrib["type"]=type
child41.text="3352-57-6"
type="formula"
child42=etree.SubElement(child4, 'name')
child42.attrib["source"] = source
child42.attrib["type"]=type
child42.text="HO"
child43=etree.SubElement(child4, 'name')
child43.attrib["source"] = source
child43.text="&middot;OH"
child44=etree.SubElement(child4, 'name')
child44.attrib["source"] = source
child44.text="hydroxy radical"
child45=etree.SubElement(child4, 'name')
child45.attrib["source"] = source
child45.text="hydroxyl"
child46=etree.SubElement(child4, 'name')
child46.attrib["source"] = source
child46.text="hydroxyl radical"
child47=etree.SubElement(child4, 'name')
child47.attrib["source"] = source
child47.text="oh"
child48=etree.SubElement(child4, 'name')
child48.text="hidroksil"
child49=etree.SubElement(child4, 'name')
child49.text="hidroksi radikal"
type="InChI"
child410=etree.SubElement(child4, 'name')
child410.attrib["type"]=type
child410.text="InChI=1/HO/h1H"
child5=etree.SubElement(root, 'chemicalComposition')
atomdict={}
for atom in mol.atoms:
	symbol = atom.symbol
	if symbol in atomdict:
		atomdict[symbol]+=1
	else:
		atomdict[symbol]=1
symlist=[]
for k in atomdict.keys():
	symlist.append[k]
for sym in symlist:
	symbol=sym
	child51=etree.SubElement(child5, 'atom')
	child51.attrib["symbol"]=symbol
	child51.text=str(atomdict[sym])
# symbol="H"
# child51=etree.SubElement(child5, 'atom')
# child51.attrib["symbol"]=symbol
# child51.text="1"
# symbol="O"
# child52=etree.SubElement(child5, 'atom')
# child52.attrib["symbol"]=symbol
# child52.text="1"



print etree.tostring(root, pretty_print=True)





# XHTML = "{0}".format(xmlns)
# NSMAP = {None : xmlns,xmlns:xsi,None:primeID,xsi:schemaLocation}
# xhtml = etree.Element(XHTML + "html", nsmap=NSMAP)
# body = etree.SubElement(xhtml, XHTML + "body")
# body.text = "Hello World"
# print(etree.tostring(xhtml))

# root = etree.Element('chemicalSpecies')
# # root = etree.Element('<chemicalSpecies xmlns="http://purl.org/NET/prime/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" primeID="s00010102" xsi:schemaLocation="http://purl.org/NET/prime/ http://warehouse.primekinetics.org/schema/species.xsd">\n<copyright>©primekinetics.org 2005</copyright>')
# child1 = etree.SubElement(root, '<content bibliography="b00014319" copyrighted="true" source="©NIST">\nElements attributed to NIST are part of a collection copyrighted by NIST.\n</content>\n<preferredKey group="prime" type="formula">OH</preferredKey>')
# child2 = etree.SubElement(root, '<chemicalIdentifier>\n<name source="©NIST" type="CASRegistryNumber">3352-57-6</name>\n<name source="©NIST" type="formula">HO</name>\n<name source="©NIST">&middot;OH</name>\n<name source="©NIST">hydroxy radical</name>\n<name source="©NIST">hydroxyl</name>\n<name source="©NIST">hydroxyl radical</name>\n<name source="©NIST">oh</name>\n<name>hidroksil</name>\n<name>hidroksi radikal</name>\n<name type="InChI">InChI=1/HO/h1H</name>\n</chemicalIdentifier>')
# child3 = etree.SubElement(root, '<chemicalComposition>\n<atom symbol="H">1</atom>\n<atom symbol="O">1</atom>\n</chemicalComposition>\n</chemicalSpecies>')
# print root.tag
# # print "{0},{1},{2}".format(child1.tag,child2.tag,child3.tag)