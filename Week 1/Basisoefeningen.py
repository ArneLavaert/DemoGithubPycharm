# print("Hallo")
# print("nog eens hallo")
# x=3
# print(x)
# #dit betekent commentaar
# python interpreter gaat dit niet verwerken
#
# python GEEN declaratie van types
# bv. java
# int x = 3;
# python ontdekt wel type het is
# hoe?
# x = 3  #int, integer of geheel getal kan ook negatief -3
# y = 3.0 # float door het punt
# z = "3" # met een string
#
# # commando type
# print("x is van het type " , str(type(x)))
# print(type(y))
# print(type(z))
#
# # naam = input("Tik uw naam in ")
# # print("Hallo " + naam)
#
# print("een tekst met \"quotes\" rond")
#
# OEFENING 1
# print("Lavaert")
# print("Arne")
# print("arne.lavaert@student.howest.be")
#
# OEFENING 2
# print("Labo Basic Programming, \n\tLabo week 1\n\tKennismaking met \"Python\", \n\t\tWerken met variabelen. \nLabo Basic programming \n\tLabo week 2")
#
# OEFENING 3
# naam = input("Geef uw naam op: ")
# voornaam = input("Geef uw voornaam op: ")
# leeftijd = input("Geef uw leeftijd op: ")
#
# print("Welkom {0} {1}. U bent {2} jaar." .format(naam, voornaam, leeftijd)) #getallen formatteren en vraagt minder recources
#
# OEFENING 4
#
# OEFENING 5
# basis = float(input("Geef de basis van uw driehoek op: "))
# hoogte = float(input("Geef de hoogte van uw driehoek op: "))
# oppervlakte = float(basis) * float(hoogte)/2
# print("De oppervlakte van uw driehoek is gelijk aan {0}.".format(oppervlakte))
#
# OEFENING 6
# dagen = int(input("Geef het aantal dagen op: "))
# uren = int(input("Geef het aantal uren op: "))
# minuten = int(input("Geef het aantal minuten op: "))
# seconden = int(input("Geef het aantal seconden op: "))
# totaalseconden = dagen * 86400 + uren * 3600 + minuten * 60 + seconden
# print("Het totale aantal seconden bedraagt {0}." .format(totaalseconden))
#
# OEFENING 7
# totaal_seconden = int(input("Geef het totaal aantal seconden op: "))
# dagen = int(totaal_seconden / (24*60*60))
# rest = int(totaal_seconden % (24*60*60))
# uren = int(rest / 3600)
# rest2 = int(rest % 3600)
# minuten = int(rest2 /60)
# rest3 = int(rest2 % 60)
# seconden = int(rest3)
# print("d:u:m:s --> {0}:{1}:{2}:{3}".format(dagen, uren, minuten, seconden))
#
# OEFENING 8
# n = int(input("Geef een getal op: "))
# resultaat = n + n*n + n*n*n
# print("Het resultaat is {0}".format(resultaat))
#
# OEFENING 9
# x = int(input("Geef getal 1 op: "))
# y = int(input("Geef getal 2 op: "))
# resultaat = (x+y)*(x+y)
# print("Het resultaat is {0}.".format(resultaat))