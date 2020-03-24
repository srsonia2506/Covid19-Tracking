import requests
from bs4 import BeautifulSoup
import string

def parse():
    country = ""
    totalCases = ""
    totalDeaths = ""
    resultstring = ""
    
    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)

    # find the html page in question with the relevant data
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find(id="main_table_countries_today")

    # iterate through all table rows 'tr'
    countryData = data.find_all('tr')

    for countryData in countryData:
        indivData = countryData.find_all('td')

        for count,indivData in enumerate(indivData):
            #could implement a switch case but we'll use janky elifs
            if count==0:
                country = indivData.text
            elif count==1:
                totalCases = indivData.text
            elif count==2:
                newCases = indivData.text
            elif count==3:
                totalDeaths = indivData.text
            elif count==4:
                newDeaths = indivData.text
            elif count==5:
                totalRecovered = indivData.text
            elif count==6:
                activeCases = indivData.text
            elif count==7:
                seriousCritcal = indivData.text
            elif count==8:
                totalCasesPerOneMil = indivData.text
            else:
                #only 9 elements in this table so shouldn't get here.
                print("count went too high! breaking")
                # continue

        # Process the scraped data: remove punctuation and whitespace
        country.strip()
        country = country.translate(str.maketrans('', '', string.punctuation))
        totalCases = totalCases.strip()
        totalCases = totalCases.translate(str.maketrans('', '', string.punctuation))
        totalDeaths = totalDeaths.strip()
        totalDeaths = totalDeaths.translate(str.maketrans('', '', string.punctuation))

        # Process the text into integers for nice stuff for future processing.
        # perhaps can store into an array.
        if(totalCases.strip()==''):
            totalCasesInt=0
        else:
            totalCasesInt = int(totalCases)
        
        if(totalDeaths.strip()==''):
            totalDeathsInt=0
        else:
            totalDeathsInt = int(totalDeaths.strip())

        #Printing out data!
        if(totalCasesInt==0):
            resultstring +="In {}, there are currently no cases.\n".format(country)
        elif(totalDeathsInt==0):
            resultstring +="In {}, there are currently {} cases and no deaths.\n".format(country,totalCasesInt)
        else:
            resultstring +="In {}, there are currently {} cases and {} deaths.\n".format(country,totalCasesInt, totalDeathsInt)

    return resultstring


        
