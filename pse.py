#!//usr/bin/python3.6

import requests
import json
import os
import datetime


url = 'http://phisix-api4.appspot.com/stocks/'

while True:
    print()
    a = input(' Stock/Ticker Code: ')  # add u for it to work
    if a == 'exit':
     break
    elif a == 'clear':
        os.system('clear')
        continue  # reload the page
    b = '.json'


    try:
        final = url + a + b
        pse = requests.get(final).json()
      # print(pse)

        print()        #datetime
        pse_asof = pse['as_of']
        print(' Date as of: ' + pse_asof.replace('T', '   Time:' ))

        print()

        pse_name = pse['stock'][0]['name']
        print(' Company name: ' + pse_name)

        pse_symbol = pse['stock'][0]['symbol']
        print(' Symbol: ' + pse_symbol)

        pse_currency = pse['stock'][0]['price']['currency']
       #  print(' Currency: ' + json.dumps(pse_currency))

        pse_amount = pse['stock'][0]['price']['amount']
        print(' Amount: ' + json.dumps(pse_amount) + " " + pse_currency)   # dumps will take all kind of format and value

        pse_pc = pse['stock'][0]['percent_change']
        print(' Percent Change: ' + json.dumps(pse_pc) + '%')

        pse_vol = pse['stock'][0]['volume']
        print(' Volume: ' + json.dumps(pse_vol))

        print()
        print(u' Please Type \u001b[32mexit\u001b[0m to close this program or\u001b[0m Type \u001b[32mclear\u001b[0m to clear the screen.')




    except Exception as e:

        print('')
        print('')
        print('{0}{1}'.format(u' Error Occurred !!\u001b[31m \n Either not found or Error With Connectivity. \n ' ,e ))  # string format with catch
        print(u'\u001b[37m Please try again ..\u001b[37m\n')
        print()
