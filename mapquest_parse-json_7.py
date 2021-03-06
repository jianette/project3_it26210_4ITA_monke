import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "p3soK7umyiPxI5c9cPsRGEWFHbWcqd55"
while True:
    orig = input ("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input ("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        #Statement for the Toll Gate
        if json_data["route"]["hasTollRoad"] == True:
            print("The road that you will go through will have a toll gate so ready your cash.")
        else:
            print("The road that you will go through will not have a toll gate.")
        #Statement for the Bridge
        if json_data["route"]["hasBridge"] == True:
            print("The road that you will go through will have a bridge so be safe when driving.")
        else:
            print("The road that you will go through will not have a bridge.")
        #Statement for the Tunnel
        if json_data["route"]["hasTunnel"] == True:
            print("The road that you will go through will have a tunnel so make sure your lights are working.")
        else:
            print("The road that you will go through will not have a tunnel.")
        #Statement for the Cross Country
        if json_data["route"]["hasCountryCross"] == True:
            print("You need to go to another country to reach your destination.")
        else:
            print("You don't have to go to another country to reach your destination.")

        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        #Added a time in each legs of the route
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " With a distance of " + str("{:.2f}".format((each["distance"])*1.61) + " km") + " and estimated time of "+ (each["formattedTime"]))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")