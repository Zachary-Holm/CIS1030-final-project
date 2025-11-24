import requests

url = "https://open.er-api.com/v6/latest/USD"
response = requests.get('https://open.er-api.com/v6/latest/USD')

data = requests.get(url).json()
response.json()

# setting up a user input using 
userExchangeInput = input(str('Enter the three character currency name, such as USD '))
input_rate = data["rates"][userExchangeInput]
sek_rate = data['rates']['SEK']



# trying to set up a list display of the avalible currencies to the user so they can pick

avalibleCurList = []

avalibleCurList.append()



# printing the result of the users input
#print(str(response.json()))
print (f'USD to',(userExchangeInput), input_rate)
print ('USD to SEK ', sek_rate)