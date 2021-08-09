#!/usr/bin/env python
import sys, json, requests
from datetime import datetime

#district 04012 = Bremerhaven
url = "https://api.corona-zahlen.org/districts/04012"
r = requests.get(url)
data = r.json()

date1=data1['meta']['lastUpdate']
cases1=data1['data']['04012']['cases']
deaths1=data1['data']['04012']['deaths']
casesPerWeek1=data1['data']['04012']['casesPerWeek']
deathsPerWeek1=data1['data']['04012']['deathsPerWeek']
recovered1=data1['data']['04012']['recovered']
weekIncidence1=data1['data']['04012']['weekIncidence']
casesPer100k1=data1['data']['04012']['casesPer100k']
deltacases1=data1['data']['04012']['delta']['cases']
deltadeaths1=data1['data']['04012']['delta']['deaths']
deltarecovered1=data1['data']['04012']['delta']['recovered']

def telegram_bot_sendtext(bot_message):
   bot_token = 'INSERT_YOUR_BOT_TOKEN_HERE'
   bot_chatID = 'INSERT_YOUR_CHAT_ID_HERE'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()
   
text = telegram_bot_sendtext("BREMERHAVEN" + str(datetime.now()) + "\n\nweek incidence: " + str(weekIncidence1) + "\n\ncases: " + str(cases1) + "\ndeaths: " + str(deaths1) + "\n\ncases per week: " + str(casesPerWeek1) + "\ndeaths per week: " + str(deathsPerWeek1) + "\nrecovered: " + str(recovered1) + "\ncases per 100k: " + str(casesPer100k1) + "\n\ndelta cases: " + str(deltacases1) + "\ndelta deaths: " + str(deltadeaths1) + "\ndelta recovered: " + str(deltarecovered1) + "\n\ndata from: " + date1 + "\n\n powered by: https://fachinformatiker.app")
