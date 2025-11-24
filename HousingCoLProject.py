import requests

## testing if the call function works

requests.get('https://open.er-api.com/v6/latest/USD')

# adding a header with an API key because i couldnt find any realestate sites that didnt use a key
# 00d522719ab351bcb0d85d4872407006
# update, attomdata does not allow the requesting of information for their free tier, so i need to find something similar that does
# though not fully what i was looking for. this exchange rate does provide lots of info that i can sort through
headers = {
    "Authorization": 'https://open.er-api.com/v6/latest/USD'
}


response = requests.get('https://open.er-api.com/v6/latest/USD')

data = requests.get('https://open.er-api.com/v6/latest/USD').json()

if response.status_code == 200:
    print (f'Success, code {response.status_code}')
    response.content

    #providing the type of decoder to decode the info from the site, im using UTF-8

    response.encoding = "utf-8"  

    response.json()
    #setting up the ability for the user to enter in a string for their currency

    userExchangeInput = input(str('Enter the three character currency name, such as USD '))

    input_rate = data["rates"][userExchangeInput]

    print (f'USD to',(userExchangeInput), input_rate)

    #print(str(response.json()))

  

elif response.status_code != 200:
    print (f'Non-success status code: {response.status_code}')




## got a 503 error, service available from the cat site, going to try another
# using the name.io site returned a 200 code which is good, the call works

