from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

### ~~~ Money Input Validation for Text ~~~ ###
### ~~~ Programmed by Mo Hisham Hussain ~~~ ###
def validate(inp): # Validate money Format
    valid = True
    decimal = None
    decimalPlaces = -1
    
    for i in list(inp):
        if (i.isnumeric() == False) and (i != "."):
            valid = False # Return false if not digit 0-9
            
        if i == ".":
            decimal = True
            
        if decimal is not None: # When decimal is True, start counting dp
            decimalPlaces += 1 #Increment 1
            
    if (valid is True) and ((decimalPlaces == -1) or (decimalPlaces == 2)):
        return True # Either integer or two decimal places for currence
    else:
        return False # Not compatible currency format!
    
def scrapeInflation():
    #url = 'https://www.ons.gov.uk/economy/inflationandpriceindices'
    url = 'https://www.bankofengland.co.uk/'
    page = requests.get(url) # Request elements
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the parent element of the inflation value
    parent_element = soup.find('div', class_='home-stats')

    # find the inflation value by navigating the HTML tree based on the pattern
    # #<span class="home-stat-number">10.4%</span> what I am trying to scrap
    inflation_element = parent_element.find('a', href='/monetary-policy/inflation')
    inflation = inflation_element.find('span', class_='home-stat-number').text

    '''#<p class="stand-out"> 9.2 % </p> What I am trying to scrape
    inflation = soup.find("span", {"class": "home-stat-number"}).text.strip()'''
    inflation = inflation.replace("\n", "")
    return(inflation)

def scrapeInterest():
    url = 'https://www.bankofengland.co.uk/'
    page = requests.get(url) # Request elements
    soup = BeautifulSoup(page.content, 'html.parser')

    #<span class="home-stat-number">4.25%</span> Scraped Element
    interest = soup.find("span", {"class": "home-stat-number"}).text.strip()
    interest = interest.replace("\n", "")
    return(interest)



'''
def interestChart():
    # Open the JSON file and load its contents
    with open('/BDS/Charts/BoE-Database_export.json', 'r') as f:
        data = json.load(f)

    # Extract the relevant data from the JSON object
    jsonData = []
    for item in data:
        jsonData.append({
            'x': item['Date'],
            'y': item['Bank Rate']
        })



def interestChart():
    url = "https://www.bankofengland.co.uk//boeapps/database/ShowChart.asp?html.x=yes&Datefrom=-180&Dateto=&SeriesCodes=IUDBEDR&UsingCodes=Y&VPD=Y&VFD=N&label1=Bank%20Rate&label2=&label3=&label4=&label5=&frequency=DD&axis=Bank%20Rate%20%" # replace with your URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    interestChart = soup.prettify()
    #interestChart = soup.prettify("div", {"class": "amcharts-main-div"})
    return interestChart

def scrapeInflation(request):
    # Scrape inflation data from website
    url = 'https://www.bankofengland.co.uk/monetary-policy/inflation/inflation-calculator-and-data'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    inflation_rate = soup.find('div', {'class': 'boe-chart__rate'}).text.strip()

    # Render template with inflation data
    context = {'inflation_rate': inflation_rate}
    return render(request, 'inflation.html', context)
    url = 'https://www.ons.gov.uk/economy/inflationandpriceindices'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_element = soup.find("div", {"class": "flex stretch flex-wrap-wrap content-space-between margin-bottom--2"})
    print(div_element.text)
'''