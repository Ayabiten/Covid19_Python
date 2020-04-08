from urllib.request import urlopen
from urllib import response
import json

def json_to_array():
    jsonurl = urlopen("https://tram-production.com/covid-api/api.php?fbclid=IwAR2SCRJ69QhUrRsRTOjlep6Lf_-PMJoEgLIMUbFbskAddbThcKMVKJedQlE")
    data =json.loads(jsonurl.read())
    return data



#json_to_array()
def World():
    data = json_to_array()
    WorldCases = data["WORLD-CASES"]
    WORLDDEATHS = data["WORLD-DEATHS"]
    WORLDRECOVERED = data["WORLD-RECOVERED"]
    print("############################ World ###################################")
    print("WORLD-CASES: ",WorldCases)
    print("WORLD-DEATHS: ",WORLDDEATHS)
    print("WORLD-RECOVERED: ",WORLDRECOVERED)
    print("############################ World ###################################")



def Maroc_Today():
    data = json_to_array()
    MA_TODAY_CASES = data["MA-TODAY-CASES"]
    MA_TODAY_DEATHS = data["MA-TODAY-DEATHS"]
    print("############################ Maroc Today ###################################")
    print("MA_TODAY_CASES: ",MA_TODAY_CASES)
    print("MA_TODAY_DEATHS: ",MA_TODAY_DEATHS)
    print("############################ Maroc Today ###################################")

def Maroc_info():
    data = json_to_array()
    #MA first & last
    MA_FIRST_CASE = data["MA-FIRST-CASE"]
    MA_LAST_CASE = data["MA-LAST-CASE"]
    #MA CASES
    MA_CASES = data["MA-CASES"]
    MA_RECOVERED = data["MA-RECOVERED"]
    MA_DEATHS = data["MA-DEATHS"]
    MA_EXCLUDE = data["MA-EXCLUDE"]
    # Percentage
    MA_RECOVERED_PERCENTAGE = data["MA-RECOVERED-PERCENTAGE"]
    MA_DEATHS_PERCENTAGE = data["MA-DEATHS-PERCENTAGE"]
    print("############################ Maroc CASE ###################################")
    print("MA_FIRST_CASE: ",MA_FIRST_CASE)
    print("MA_LAST_CASE: ",MA_LAST_CASE)
    print("############################ Maroc CASE ###################################\n")
    print("############################ MA_CASES ###################################")
    print("MA_CASES: ",MA_CASES)
    print("MA_RECOVERED: ",MA_RECOVERED)
    print("MA_DEATHS: ",MA_DEATHS)
    print("MA_EXCLUDE: ",MA_EXCLUDE)
    print("############################ MA_CASES ###################################\n")
    print("############################ MA_PERCENTAGE ###################################")
    print("MA_RECOVERED_PERCENTAGE: ",MA_RECOVERED_PERCENTAGE)
    print("MA_DEATHS_PERCENTAGE: ",MA_DEATHS_PERCENTAGE)
    print("############################ MA_PERCENTAGE ###################################\n")

def Regions():
    data = json_to_array()
    Region = data["REGIONS"][0]
    print("************************* Regions ********************************")
    for key in Region :
        print ( key,": ", Region[ key ])
    print("************************* Regions ********************************")

def DATA_BY_REGION():
    data = json_to_array()
    DATA_Region = data["DATA_BY_REGION"]
    print("************************* Regions ********************************")
    for target in DATA_Region:
        print("\n************************* Region ********************************")
        for key in target :
            print ( key,":", target[ key ])
        print("************************* Region ******************************** \n")
    print("************************* Regions ********************************")

def Contact():
    data = json_to_array()
    CONTACTS = data["CONTACTS"]
    print("************************* CONTACTS ********************************")
    for target in CONTACTS:
        for key in target :
            print ( key,":", target[ key ])
        print(" \n")
    print("************************* Regions ********************************")



def COMMUNIQUES():
    data = json_to_array()
    COMMUNIQUES = data["COMMUNIQUES"]
    print("************************* COMMUNIQUES ********************************")
    for target in COMMUNIQUES:
        for key in target :
            print ( key,":", target[ key ])
    print("************************* COMMUNIQUES ********************************")





def Menu():
    print("1- World Cases")
    print("2- Maroc_Today")
    print("3- Maroc_info")
    print("4- Regions")
    print("5- DATA_BY_REGION")
    print("6- Contact")
    print("7- COMMUNIQUES")
    choix = int(input("Donner Votre choix:"))
    if choix == 1:
        World()
        Menu()
    if choix == 2:
        Maroc_Today()
        Menu()
    if choix == 3:
        Maroc_info()
        Menu()
    if choix == 4:
        Regions()
        Menu()
    if choix == 5:
        DATA_BY_REGION()
        Menu()
    if choix == 6:
        Contact()
        Menu()
    if choix == 7:
        COMMUNIQUES()
        Menu()
Menu()






