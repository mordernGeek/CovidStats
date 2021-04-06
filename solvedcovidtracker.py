

#My first py
#Write a COVID-19 Statistics Tracker!

#necessary imports

#from datetime import datetime
import requests
import json

print("Hello, Stranger")
#Getting relevant data from guest
user_name = input('What is your Name?')
name = user_name.capitalize()
print ('Welcome,' + ' ' + name )

user_location = input ('What Country (in full, please) are you in now?')
country = user_location.capitalize() #edited
slug_country = country.strip().lower() #edited
slug_country = slug_country.replace(' ', '-') #edited
print (slug_country.capitalize())

print ('we are now going to update you on the coronavirus stats in the world and in' + ' '+ country )

#fetching Data - TotalDeaths TotalConfirmed TotalRecovered Date #ActiveCases - not available for this api


response = requests.get("https://api.covid19api.com/summary")
all = json.loads(response.text)
covid_stats = all.items()

#print (covid_stats)
print ('Global New Cases')
print(all['Global']['NewConfirmed'])
print ('Global Total Cases')
print(all['Global']['TotalConfirmed'])
print ('Global Total Deaths')
print(all['Global']['TotalDeaths'])

#print (country + ' New Cases')
#print(type(all['Countries']))
#print(len(all['Countries']))
count = 0
while count < len(all['Countries']):
    #print(all['Countries'][count]['Country'])
    
    
    if (all['Countries'][count]['Slug']) == slug_country:
        print(all['Countries'][count]['Country'])
        print (country + ' Total Cases')
        print(all['Countries'][count]['TotalConfirmed'])
        print (country + ' Total Deaths')
        print(all['Countries'][count]['TotalDeaths'])
        print (country + ' Recovered Cases')
        print(all['Countries'][count]['TotalRecovered'])
        
        archived_cases = int((all['Countries'][count]['TotalRecovered'])) + int((all['Countries'][count]['TotalDeaths']))
        active_cases = int((all['Countries'][count]['TotalConfirmed'])) - archived_cases
        print (country + ' Active Cases')
        print(active_cases)
        #count = count + 1
        count = 200 + count
    else:
        count = count + 1
    
 
        
print('#StaySafe, ' + name )
        
        
        





