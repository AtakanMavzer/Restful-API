#Requests is an HTTP library, written in Python, for human beings
import requests


url="http://127.0.0.1:5000/"

List=[
  {
    "name": "Parrish",
    "surname": "Pugh",
    "email": "parrishpugh@globoil.com"
  },
  {
    "name": "Anita",
    "surname": "Little",
    "email": "anitalittle@globoil.com"
  },
  {
    "name": "Raymond",
    "surname": "Maxwell",
    "email": "raymondmaxwell@globoil.com"
  },
  {
    "name": "Lupe",
    "surname": "Kidd",
    "email": "lupekidd@globoil.com"
  },
  {
    "name": "Ashley",
    "surname": "Sellers",
    "email": "ashleysellers@globoil.com"
  },
  {
    "name": "Hawkins",
    "surname": "Baird",
    "email": "hawkinsbaird@globoil.com"
  },
  {
    "name": "Simmons",
    "surname": "Mercer",
    "email": "simmonsmercer@globoil.com"
  },
  {
    "name": "Joyce",
    "surname": "Beck",
    "email": "joycebeck@globoil.com"
  },
  {
    "name": "Georgina",
    "surname": "Best",
    "email": "georginabest@globoil.com"
  },
  {
    "name": "Chelsea",
    "surname": "Santos",
    "email": "chelseasantos@globoil.com"
  },
  {
    "name": "Graciela",
    "surname": "Hampton",
    "email": "gracielahampton@globoil.com"
  },
  {
    "name": "Karen",
    "surname": "Pollard",
    "email": "karenpollard@globoil.com"
  },
  {
    "name": "Greer",
    "surname": "Hansen",
    "email": "greerhansen@globoil.com"
  },
  {
    "name": "Shannon",
    "surname": "Mcguire",
    "email": "shannonmcguire@globoil.com"
  },
  {
    "name": "Freida",
    "surname": "Dean",
    "email": "freidadean@globoil.com"
  },
  {
    "name": "Cecile",
    "surname": "Hardin",
    "email": "cecilehardin@globoil.com"
  },
  {
    "name": "Lydia",
    "surname": "Mays",
    "email": "lydiamays@globoil.com"
  },
  {
    "name": "Margaret",
    "surname": "Black",
    "email": "margaretblack@globoil.com"
  },
  {
    "name": "Alicia",
    "surname": "Franks",
    "email": "aliciafranks@globoil.com"
  },
  {
    "name": "Blair",
    "surname": "Vinson",
    "email": "blairvinson@globoil.com"
  },
  {
    "name": "Marcy",
    "surname": "Joyner",
    "email": "marcyjoyner@globoil.com"
  },
  {
    "name": "Anderson",
    "surname": "Meadows",
    "email": "andersonmeadows@globoil.com"
  },
  {
    "name": "Peggy",
    "surname": "Solis",
    "email": "peggysolis@globoil.com"
  }
]

#For adding whole list through the Post request.
for i in range(len(List)):
    response = requests.post(url+"UserRegistry/"+str(i),List[i])
    print(response.json())
input()

#For testing whether we can create new user on top of an existing one
response = requests.post(url+"UserRegistry/0",{"name":"test","surname":"tester","email":"req@hotmail"})
print(response.json())
input()

#Patch request
response=requests.patch(url+"UserRegistry/0",{"name": "Parrish","surname": "Pugh","email":"asdasdsaddsa@hotmail"})
print(response.json())
input()

#For testing the Patch and Get requests functionality.
response=requests.get(url+"UserRegistry/0")
print(response.json())
input()

#Put request
response=requests.put(url+"UserRegistry/0",{"name":"test","surname":"tester","email":"extra@@@@@gmail"})
print(response.json())
input()

#For testing the Put and Get requests functionality.
response=requests.get(url+"UserRegistry/0")
print(response.json())
input()

#Delete request
response=requests.delete(url+"UserRegistry/0")
print(response)
input()

#For testing the Delete and Get requests functionality.
response=requests.get(url+"UserRegistry/0")
print(response.json())
input()









