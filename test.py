# from lxml import etree
# xmlns="http://purl.org/NET/prime/"
# xsi="http://www.w3.org/2001/XMLSchema-instance"
# primeID="s00010102"
# schemaLocation="http://warehouse.primekinetics.org/schema/species.xsd"
# NSMAP = {None: xmlns}
# root = etree.Element('{' + xmlns + '}chemicalSpecies', nsmap=NSMAP)
# root.attrib["{" + xsi + "}schemaLocation"] = schemaLocation
# # root.attrib["{" + xmlns + "}xsi"] = xsi
# root.attrib["primeID"] = primeID
# 
# 
# child5=etree.SubElement(root, 'chemicalComposition')
# atomdict={}
# molatoms=['C','H','H','O','F','H','Ar']
# for symbol in molatoms:
# # 	symbol = atomsymbol
# 	if symbol in atomdict:
# 		atomdict[symbol]+=1
# 	else:
# 		atomdict[symbol]=1
# symlist=[]
# for k in atomdict.keys():
# 	symlist.append(k)
# symvariables={}
# for n in range(len(symlist)):
# 	symbol=symlist[n]
# 	symvariables["child5_{0}".format(n)]=etree.SubElement(child5, 'atom')
# 	symvariables["child5_{0}".format(n)].attrib["symbol"]=symbol
# 	symvariables["child5_{0}".format(n)].text=str(atomdict[symlist[n]])
# print etree.tostring(root, pretty_print=True)

# import urllib, urllib2
# id=["CC"]
# smilelist=[]
# for identifier in id:
#     url = "http://cactus.nci.nih.gov/chemical/structure/{0}/cas".format(urllib.quote(identifier))
#     f = urllib2.urlopen(url, timeout=5)
#     cas = f.read()
#     smilelist.append(cas)
# print smilelist

# id=["CC"]
# namelist=[]
# for identifier in id:
#     url = "http://cactus.nci.nih.gov/chemical/structure/{0}/names".format(urllib.quote(identifier))
#     f = urllib2.urlopen(url, timeout=5)
#     names = f.read()
#     iprev=0
# #     import ipdb; ipdb.set_trace()   
#     for i in range(len(names)):
#         if names[i:i+1]=="\n":
#             name=names[iprev:i]
#             namelist.append(name)
#             iprev=i+1
# #     import ipdb; ipdb.set_trace()
#     for n in namelist:
#         if '[' in n or '(' in n or ',' in n or '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n or '8' in n or '9' in n or len(n)<=3:
#             namelist.remove(n)
#             print n
# print namelist

# Ethane is logged as Neomycin trisulfate salt hydrate, there are lots of similar issues- any of these names points to all the other ones (lumping!)

# ReactionsWriter
from lxml import etree
# rmgMol = rmgSpecies.molecule[0]
# import ipdb; ipdb.set_trace()
# xmlns="url"
# xsi="url.xsi"
# primeID="[insert primeID]"
# schemaLocation="url.xsd"
# NSMAP = {None: xmlns, 'xsi': xsi}
# root = etree.Element('{' + xmlns + '}chemicalSpecies', nsmap=NSMAP)
# #root.attrib["{" + xmlns + "}xsi"] = xsi
# root.attrib["{" + xsi + "}schemaLocation"] = schemaLocation
# root.attrib["primeID"] = primeID
# child1=etree.SubElement(root,'copyright')
# child1.text="[Richard West is awesome 2015]"
# child2=etree.SubElement(root,'reactants')
# #get species involved in reaction in list form, use the dictionary way to make child2_1 change to other children
# for spec in specieslist:
# 	preferredKey=spec.getFormula()
# 	primeID=specprimeID
# 	child2_1==etree.SubElement(child2,'speciesLink')
# 	child2_1.attrib["preferredKey"]=preferredKey
# 	child2_1.attrib["primeID"]=primeID
# 	child2_1.text="-1 (reactant) or 1 (product)"
	
# preferredKey="[insert preferredKey1]"
# primeID="s00000275"
# child21=etree.SubElement(child2,'speciesLink')
# child21.attrib["preferredKey"]=preferredKey
# child21.attrib["primeID"]=primeID
# child21.text="-1"
# primeID="s00000276"
# child22=etree.SubElement(child2,'speciesLink')
# child22.attrib["preferredKey"]=preferredKey
# child22.attrib["primeID"]=primeID
# child22.text="1"
# print etree.tostring(root, pretty_print=True)

import urllib2
# stuff=urllib2.urlopen('http://cactus.nci.nih.gov/chemical/structure/69642-59-7/stdinchi').read()
# print stuff

import rmgpy
import os
os.path.realpath(rmgpy.__file__.split('/rmgpy')[0])
from importChemkin import ModelMatcher
matcher = ModelMatcher()
matcher.loadKnownSpecies('/Users/dgreen18/Code/RMG-models/Gasoline_Surrogate/SMILES.txt')
smileslist=matcher.smilesDict
print smileslist