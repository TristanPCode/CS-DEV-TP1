"""Créé par Tristan POUILLY
Date: 25/09/2023
Fichier d'éxécutable de MainCode_TP1"""

import MainCode_TP1 as TP1
"""Annee Bissextile"""
print("Annee Bissextile \n")

res=TP1.AnneeBissextile(2013)
print("2013: False VS", res)
res=TP1.AnneeBissextile(2014)
print("2014: True VS", res)
#res=TP1.AnneeBissextile("hahaha")
#print("hahaha: False VS", res)
res=TP1.AnneeBissextile(2100)
print("2100: False VS", res)
res=TP1.AnneeBissextile(2400)
print("2400: True VS", res)
res=TP1.AnneeBissextile(1896)
print("1896: True VS", res)
print("\n")
# Verif OK

"""Jour dans le mois"""
print("Jour dans le mois \n")
res=TP1.NbJours(4,2023)
print("4,2023: 30 VS",res)
res=TP1.NbJours(10,2023)
print("10,2023: 31 VS",res)
res=TP1.NbJours(2,2023)
print("2,2023: 28 VS",res)
res=TP1.NbJours(2,2024)
print("2,2023: 29 VS",res)
#res=TP1.NbJours(14,2023)
#print("14,2023: Rien",res)
#res=TP1.NbJours(4,"Amogus")
#print("4,Amogus: Rien VS",res)
print("\n")

"""Date Valide"""
print("Date Valide \n")
#TP1.DateValide()

"""Exercice 3"""
print("Exercice 3: LES IMPÔÔÔTS!!!\n")
res=TP1.mesImpots(50000)
print("50 000: 8921 VS",res)
res=TP1.mesImpots(100000)
print("100 000:",res)
res=TP1.mesImpots(200000)
print("200 000:",res)

"""Exercice 4"""
print("Multiplication de matrices \n")
A=[[2,0,0],[0,2,0],[0,0,2]]
B=[[1,1,1],[1,1,1],[1,1,1]]
C=TP1.ProdMat(A,B)
print(C)