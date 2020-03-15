#!/usr/bin/python3


import requests
import json
import os
import datetime
import readline
import arrow
import time
import dateutil.parser
from progress.bar import PixelBar
from time import sleep



url = 'http://phisix-api4.appspot.com/stocks/'

while True:

    
    print()
    a = input(u' Stock/Ticker Code: ')  # add u for it to work
    print()

    if a == 'exit':
     break
    elif a == 'clear':
        os.system('clear')
        continue  # reload the page    
    b = '.json'

    with PixelBar(' Fetching Data ...') as bar:   # bar progress
        for i in range(100):
            sleep(0.03)
            bar.next()
            





    try:
        final = url + a + b
        pse = requests.get(final).json()
      # print(pse)



        print()        #datetime
        pse_asof = pse['as_of']
        d = dateutil.parser.parse(pse_asof)
        print(' Date:  ' + d.strftime('%m/%d/%Y'))  # goods na ito 
        oras=(d.strftime('%H:%M'))
        oras1 = datetime.datetime.strptime(oras,'%H:%M').strftime('%I:%M %p') # goods narin ito 
        
        
        print(' As of: ' + oras1)
        
        print()


        # stock name na ito 

        pse_name = pse['stock'][0]['name']
        print(' Company name: ' + pse_name)

        pse_symbol = pse['stock'][0]['symbol']
        print(' Symbol: ' + pse_symbol)

        pse_currency = pse['stock'][0]['price']['currency']
       #  print(' Currency: ' + json.dumps(pse_currency))

        pse_amount = pse['stock'][0]['price']['amount']
        print(u' Amount: ' + '\u20B1 ' + json.dumps(pse_amount)) # \u20B1  # dumps will take all kind of format and value

        pse_pc = pse['stock'][0]['percent_change']
        aa = float(pse_pc)

        if aa < 0 :
            print(u' Percent Change: ' + '\u001b[31m' + json.dumps(aa) + '\u001b[0m' + '%')
        elif aa == 0:
            print(u' Percent Change: ' + json.dumps(aa) + '%')   
        else:
             print(u' Percent Change: ' + '\u001b[32m' + json.dumps(aa) + '\u001b[0m' + '%')
       

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




  

      
      


