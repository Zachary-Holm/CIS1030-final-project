import requests
import pycountry

#===============================================================================================================
# def function for the 'translation' of json info from a STR to a Float=========================================
#===============================================================================================================

def toFloat(value):
    if value is None:
        return None
    try:
        cleaned = str(value).replace('$', '').replace(',', '').strip()
        return float(cleaned)
    except ValueError:
        return None
    
#===============================================================================================================
# def function to convert cityCurrency to targetCurrency========================================================
#===============================================================================================================

def convert(value):
    if value is None:
        return None
    value_in_usd = value / cityRateTwo         
    final_value = value_in_usd * inputRate      
    return round(final_value, 2)

#===============================================================================================================
# welcome message===============================================================================================
#===============================================================================================================

userName = (input('Whats Your Name? '))

print ('#' * 60 )
print (f' Welcome {userName}, This Is An International Cost Of Living Calculator')
print (' As The Program Progresses, You Will Be Given Steps To Follow')
print ('#' * 60 )

#===============================================================================================================
# currency API requests and output==============================================================================
#===============================================================================================================

userExchangeInput = input(str('Enter The Three Character Name For Your Currency. NOTE, This Currency Must Allign With Your Location, \n Of Which Will Be Determined In The Next Question: \n '))
# Request from the currency API
urlCur = 'https://open.er-api.com/v6/latest/USD'
responseCuR = requests.get('https://open.er-api.com/v6/latest/USD')
data = requests.get(urlCur).json()
responseCuR.json()
# currency calculations
inputRate = data ['rates'][userExchangeInput]

# currency output data
print (f'USD to',(userExchangeInput), inputRate)
# remove the SEK test variable 
#sek_rate = data ['rates']['SEK']
#print ('USD to SEK ', sek_rate) 

#===============================================================================================================
# first city to compare=========================================================================================
#===============================================================================================================

userCityInputOne = input('Enter A City Name, This City Must Match The Currency Used i.e Seattle & USD or Sydney & AUD:\n').strip().lower().replace(' ', '-')
#userCitySelectionOne = input('Enter currency code (e.g., usd): ').strip().lower()
print ('You Are Prompted To Enter An Item, This Could Be Anything \n from "Beer", "Gas" or even "Combo Meal At McDonalds: ')
search_item = input('Item to search for: ').strip().lower()

#urlCoL = 'http://localhost:3000/:Denver?USD'
urlCoL = f'http://localhost:3000/:{userCityInputOne}?currency={userExchangeInput}'
ResponseCoL = requests.get(urlCoL)
#dataCoL = requests.get(urlCoL).json()


if ResponseCoL.status_code == 200:
    dataCoL = ResponseCoL.json()
    #print(ResponseCoL.text)  # raw response
    
    
    # Example: print item, cost, range, low, high for each entry (adjust based on actual data structure)
    for entry in dataCoL.get('costs', []):
        item_name = entry.get('item', '').lower()
        if search_item in item_name:  # substring match

            usdCost = toFloat (entry.get('cost'))
            usdLow = toFloat (entry.get('range',{}).get('low'))
            usdHigh =toFloat (entry.get('range',{}).get('high'))

            convCost = round(usdCost * inputRate, 2) if usdCost else None
            convLow = round(usdLow * inputRate, 2) if usdLow else None
            convHigh = round(usdHigh * inputRate, 2) if usdHigh else None

            print(f"Item: {entry.get('item')}")
            print(f'This Is The Average Cost In ({userExchangeInput}): {convCost}')
            print(f'This is The Low Cost in ({userExchangeInput}): {convLow}')
            print(f'This Is The High Cost In ({userExchangeInput}): {convHigh}')
            print('---')
            print(ResponseCoL.status_code)

else:
    print('Failed to get data.')

#================================================================================================================
# second city to compare=========================================================================================
#================================================================================================================

userCityInputTwo = input('Enter Another City Name To Compare Entry One With: \n').strip().lower().replace(' ', '-')
userCitySelectionTwo = input('Enter Currency Code, Reminder, The Code Must Allign With The Country: \n').strip().lower()
print ('You Are Prompted To Enter An Item, This Could Be Anything \n from "Beer", "Gas" or even "Combo Meal At McDonalds: \n')
search_itemTwo = input('Enter An Item: ').strip().lower()

#urlCoL = 'http://localhost:3000/:Denver?USD'
urlCoLTwo = f'http://localhost:3000/:{userCityInputTwo}?currency={userCitySelectionTwo}'
ResponseCoLTwo = requests.get(urlCoLTwo)
#dataCoL = requests.get(urlCoL).json()

cityRateTwo = data['rates'][userCitySelectionTwo.upper()]




if ResponseCoLTwo.status_code == 200:
    dataCoLTwo = ResponseCoLTwo.json()
    #print(ResponseCoL.text)  # raw response
    
    
    # Example: print item, cost, range, low, high for each entry (adjust based on actual data structure)
    for entry in dataCoLTwo.get('costs', []):
        item_name = entry.get('item', '').lower()
        if search_itemTwo in item_name:  # substring match

            curTwo = toFloat (entry.get('cost'))
            lowCurTwo = toFloat (entry.get('range',{}).get('low'))
            highCurTwo =toFloat (entry.get('range',{}).get('high'))

            convCostTwo = convert(curTwo)
            convLowTwo = convert(lowCurTwo)
            convHighTwo = convert(highCurTwo)


            print(f"Item: {entry.get('item')}")
            print(f'This Is The Average Cost In ({userExchangeInput}): {convCostTwo}')
            print(f'This Is The Low Cost In ({userExchangeInput}): {convLowTwo}')
            print(f' This Is The High Cost In ({userExchangeInput}): {convHighTwo}')
            print('---')
            print(ResponseCoL.status_code)

else:
    print('Failed to get data.')

#================================================================================================================

