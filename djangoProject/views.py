import requests
from django.shortcuts import render


def getData(request):
    data_list = []
    myVal = []
    usVal = []

    #initial year for table
    year = "2019"

    #check if user enter year for filter
    if 'year' in request.GET:
        year = request.GET['year']

    #API url
    url = 'https://apps.who.int/gho/athena/api/GHO/MH_12.json?profile=simple'

    #retrive the responses as JSON format
    response = requests.get(url)
    data = response.json()

    #Data Cleansing, filtering uncompleted data/ unwanted data
    for i in range(len(data['fact'])):
        if len(data['fact'][i]['dim']) == 6:
            # Data for Table
            if data['fact'][i]['dim']['YEAR'] == year:
                data_list.append(data['fact'][i])

            # Data for Chart, all the condition leads to only retriving MY and US
            if int(data['fact'][i]['dim']['YEAR']) >= 2010:
                if "COUNTRY" in data['fact'][i]['dim']:
                    if data['fact'][i]['dim']['SEX'] == "Both sexes":
                        if data['fact'][i]['dim']['COUNTRY'] == "Malaysia":
                            myVal.append(data['fact'][i]['Value'].split(" [", 1)[0])
                        elif data['fact'][i]['dim']['COUNTRY'] == "United States of America":
                            usVal.append(data['fact'][i]['Value'].split(" [", 1)[0])

    #Preparing data needed for chart
    title = 'Malaysia vs USA Suicide rates (per 100 000 population)'
    labels = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

    chart = {"title": title,
             "labels": labels,
             "usValue": usVal,
             "myValue": myVal}

    #return data for table and chart
    return render(request, 'data.html', {'data': data_list, 'chart': chart})
