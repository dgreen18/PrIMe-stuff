#!/usr/bin/env python
# coding: utf-8

# catalogPath=""
# pre="s"

import urllib2
import re
import json
import cPickle as pickle
import rmgpy
import os
from importChemkin import ModelMatcher
from rdkit import Chem

def createURLIDs(html_content):
    urls=[]
    IDs=[]
    for i in range(len(html_content)):
        if html_content[i:i+5]=='HREF=':
            fullurl="http://warehouse.primekinetics.org"+html_content[i+6:i+47]
            urls.append(fullurl)
            IDs.append(html_content[i+34:i+43])
    urls.remove(urls[0])
    urls.remove(urls[0])
    IDs.remove(IDs[0])
    IDs.remove(IDs[0])
    pickle.dump(urls,open("save.urls","wb"))
    pickle.dump(IDs,open("save.IDs","wb"))
    return urls,IDs

def masterInchi():
    Inchid={}
    CASd={}
    urls=pickle.load(open("save.urls","rb"))
    urldict=pickle.load(open("save.urldict","rb"))
    for e in urls:
        request = urllib2.Request(e, None)
        specontent=urllib2.urlopen(request, timeout=999999).read()
        for i in range(len(specontent)):
            if specontent[i:i+6]=='InChI"':
                for n in range(0,105):
                    if specontent[i+7+n:i+7+n+6]=='</name':
                        k=n
                Inchid[urldict[e]]=specontent[i+7:i+7+k]
        if 'InChI"' not in specontent:
            CASd[urldict[e]]='&'
    pickle.dump(Inchid,open("save.Inchid","wb"))
    pickle.dump(CASd,open("save.CASd","wb"))
    
def CASlist():
    CASurl=[]
    CASd=pickle.load(open("save.CASd","rb"))
    revurldict=pickle.load(open("save.revurldict","rb"))
    for id in CASd.keys():
        CASurl.append(revurldict[id])
    pickle.dump(CASurl,open("save.CASurl","wb"))

def addCAS():
    fueld={}
    CASurl=pickle.load(open("save.CASurl","rb"))
    urldict=pickle.load(open("save.urldict","rb"))
    CASd=pickle.load(open("save.CASd","rb"))
    for e in CASurl:
        request = urllib2.Request(e, None)
        specontent=urllib2.urlopen(request, timeout=999999).read()
        for i in range(len(specontent)):
            if specontent[i:i+17]=='CASRegistryNumber':
                for n in range(0,19):
                    if specontent[i+19+n:i+19+n+6]=='</name':
                        k=n
                CASd[urldict[e]]=specontent[i+19:i+19+k]
        if 'CASRegistryNumber' not in specontent:
            fueld[urldict[e]]='&'
        for e in CASd.keys():
            if CASd[e]=='&':
                del CASd[e]
    pickle.dump(CASd,open("save.CASd","wb"))
    pickle.dump(fueld,open("save.fueld","wb"))
    
def CAStoInChI():
    CASd=pickle.load(open("save.CASd","rb"))
    Inchid=pickle.load(open("save.Inchid","rb"))
    for e in CASd:
#         print CASd[e]
        try:
            request = urllib2.Request('http://cactus.nci.nih.gov/chemical/structure/'+CASd[e]+'/stdinchi', None)
            stuff=urllib2.urlopen(request, timeout=999999).read()
            Inchid[e]=stuff
            CASd[e]='deadmeat'+CASd[e]
#         print CASd[e]
        except urllib2.URLError:
            pass
#     import ipdb; ipdb.set_trace()
    for e in CASd.keys():
        if 'deadmeat' in CASd[e]:
            del CASd[e]
    for id in Inchid:
        Inchid[id]=Chem.MolToInchi(Chem.MolFromInchi(Inchid[id]))
    pickle.dump(Inchid,open("save.Inchid","wb"))
    print Inchid
    pickle.dump(CASd,open("save.CASd","wb"))
    
def fuellist():
    fuelurl=[]
    fueld=pickle.load(open("save.fueld","rb"))
    revurldict=pickle.load(open("save.revurldict","rb"))
    for id in fueld.keys():
        fuelurl.append(revurldict[id])
    pickle.dump(fuelurl,open("save.fuelurl","wb"))
        
def addFuelIDs():
    extrad={}
    fuelurl=pickle.load(open("save.fuelurl","rb"))
    urldict=pickle.load(open("save.urldict","rb"))
    fueld=pickle.load(open("save.fueld","rb"))
    for e in fuelurl:
        request = urllib2.Request(e, None)
        specontent=urllib2.urlopen(request, timeout=999999).read()
        for i in range(len(specontent)):
            if specontent[i:i+6]=='FuelID':
                for n in range(0,10):
                    if specontent[i+8+n:i+8+n+6]=='</name':
                        k=n
                fueld[urldict[e]]=specontent[i+8:i+8+k]
        if 'FuelID' not in specontent:
            extrad[urldict[e]]='&'
        for e in fueld.keys():
            if fueld[e]=='&':
                del fueld[e]
    pickle.dump(extrad,open("save.extrad","wb"))
    pickle.dump(fueld,open("save.fueld","wb"))
    
def extralist():
    extraurl=[]
    extrad=pickle.load(open("save.extrad","rb"))
    revurldict=pickle.load(open("save.revurldict","rb"))
    for id in extrad.keys():
        extraurl.append(revurldict[id])
    pickle.dump(extraurl,open("save.extraurl","wb"))
        
def addformulas():
    extraurl=pickle.load(open("save.extraurl","rb"))
    urldict=pickle.load(open("save.urldict","rb"))
    extrad=pickle.load(open("save.extrad","rb"))
    for e in extraurl:
        request = urllib2.Request(e, None)
        specontent=urllib2.urlopen(request, timeout=999999).read()
        for i in range(len(specontent)):
            if specontent[i:i+18]=='ime" type="formula':
                for n in range(0,22):
                    if specontent[i+20+n:i+20+n+6]=='</pref':
                        k=n
                extrad[urldict[e]]=specontent[i+20:i+20+k]
    del extrad['s00010880']
    del extrad['s00010881']
    pickle.dump(extrad,open("save.extrad","wb"))
    
def addgasoline():
    gasolined={'s00010880':'RD387','s00010881':'C7H16'}
    pickle.dump(gasolined,open("save.gasolined","wb"))

def compileDicts():
    masterd={}
    Inchid=pickle.load(open("save.Inchid","rb"))
    CASd=pickle.load(open("save.CASd","rb"))
    fueld=pickle.load(open("save.fueld","rb"))
    extrad=pickle.load(open("save.extrad","rb"))
    gasolined=pickle.load(open("save.gasolined","rb"))
    for d in (Inchid,CASd,fueld,extrad,gasolined):
        masterd.update(d)
    inv_masterd={v: k for k, v in masterd.items()}
    pickle.dump(masterd,open("save.masterd","wb"))
    pickle.dump(inv_masterd,open("save.inv_masterd","wb"))
    
def importSmiles():
    smilesdict={}
    os.path.realpath(rmgpy.__file__.split('/rmgpy')[0])
    matcher = ModelMatcher()
    for folder in ['AramcoMech_1.3','Biomass','CombFlame2013/17-Malewicki','CombFlame2013/487-Schenk','CombFlame2013/853-Alzueta','CombFlame2013/1315-Chang','CombFlame2013/1541-Zhang','CombFlame2013/1609-Veloo','CombFlame2013/1907-Merchant','CombFlame2013/1939-Cai','CombFlame2013/1958-Zhao','CombFlame2013/2291-Somers','CombFlame2013/2319-Serinyel','CombFlame2013/2343-Hansen','CombFlame2013/2680-Vranckx','CombFlame2013/2693-Karwat','CombFlame2013/2712-Sarathy','CombFlame2014/65-Darcy','CombFlame2014/84-Wang','CombFlame2014/405-Cai','CombFlame2014/644-Man','CombFlame2014/657-Jin','CombFlame2014/711-Allen','CombFlame2014/748-Liu','CombFlame2014/798-Cai','CombFlame2014/818-Zhang','CombFlame2014/885-Xiong','CombFlame2014/898-Wagnon','CombFlame2014/1135-Dames','CombFlame2014/1146-Rotavera','CombFlame2014/1516-Xuan','Gasoline_2','Gasoline_Surrogate','GRI-17-species-mech','GRI-mech-3.0','IJCK2013/638-Metcalfe','JPCA2013/1371-Sirjean','MB-Dooley','MB-Farooq','MB-Fisher','n-Heptane','PCI2013/187-Wang','PCI2013/225-Somers','PCI2013/259-Labbe','PCI2013/269-Matsugi','PCI2013/289-Dagaut','PCI2013/297-Herbinet','PCI2013/325-Husson','PCI2013/335-Wang','PCI2013/353-Malewicki','PCI2013/361-Malewicki','PCI2013/401-Liu','PCI2013/411-Darcy','PCI2013/519-Zador','PCI2013/527-Sheen','PCI2013/599-Veloo','PCI2013/617-Zhang','Reduced-DRG-GRI-mech','USC_Mech_ii']:
        smilesdict["{0}".format(folder)]=matcher.loadKnownSpecies('/Users/dgreen18/Code/RMG-models/'+folder+'/SMILES.txt')
    pickle.dump(smilesdict,open("save.smilesdict","wb"))

def SmilestoInChI():
    inchidict={}
    smilesdict=pickle.load(open("save.smilesdict","rb"))
    for file in smilesdict.keys():
        inchidict[file]={}
        for formula in smilesdict[file].keys():
            stripped=smilesdict[file][formula].strip('triplet')
            stripped=stripped.strip('singlet')
            inchidict[file][stripped]=Chem.MolToInchi(Chem.MolFromSmiles(stripped))
    pickle.dump(inchidict,open("save.inchidict","wb"))
    print inchidict

def inchiMatch():
    inchimatch={}
    Inchid=pickle.load(open("save.Inchid","rb"))
    print Inchid['s00010127']
    inv_Inchid={v: k for k, v in Inchid.items()}
    inchidict=pickle.load(open("save.inchidict","rb"))
    for file in inchidict.keys():
        inchimatch[file]={}
        for smile in inchidict[file].keys():
            if inchidict[file][smile] in inv_Inchid.keys():
                inchimatch[file][smile]=inv_Inchid[inchidict[file][smile]]
                print inv_Inchid[inchidict[file][smile]]
            else:
                inchimatch[file][smile]='no InChI match'
    pickle.dump(inchimatch,open("save.inchimatch","wb"))

def newPrimeID(species):
    inv_masterd=pickle.load(open("save.inv_masterd","rb")) #might have to be Inchid, depending on how we end up specifying distinct species (sort out CAS, fuelIDs, formulas...)
    if species.identifier in inv_masterd.keys():
        return inv_masterd[species.identifier]      
    else:
        maxID=1
        for id in masterd.keys():
            idstripped=id.lstrip('s0')
            if int(idstripped)>maxID:
                maxID=int(idstripped)
        maxID=maxID+1
        while len(str(maxID))<8:
            maxID='0'+str(maxID)
        maxID='s'+maxID
        return maxID
    
def getAvailablePrimeID(catalogPath, pre):
#     html_content = urllib2.urlopen('http://warehouse.primekinetics.org/depository/species/catalog/').read()
#     urls,IDs=createURLIDs(html_content)
#     urldict=dict(zip(urls,IDs))
# #     document.write(urldict.s00000017)
#     revurldict=dict(zip(IDs,urls))
#     pickle.dump(urldict,open("save.urldict","wb"))
#     pickle.dump(revurldict,open("save.revurldict","wb"))
#     masterInchi()
# #     import ipdb; ipdb.set_trace()
#     CASlist()
#     addCAS()
#     CAStoInChI()
#     fuellist()
#     addFuelIDs()
#     extralist()
#     addformulas()
#     addgasoline()
#     compileDicts()
#     masterd=pickle.load(open("save.masterd","rb"))
#     inputSmiles()
#     SmilestoInChI()
    inchiMatch()
    

getAvailablePrimeID("","s")

#     import string
#     IDnum=[]
#     for e in IDs:
#         IDnum.append(e[8])
# #         for num in e:
# #             if num in string.digits and num!=0:
# #                 k=e.find(num)
# #         IDnum.append(e[k:])
#     longdig=string.digits*12000
#     for i in range(len(IDnum)):
#         if IDnum[i]==longdig[i]:
#             print ""
#         else:
#             print i

