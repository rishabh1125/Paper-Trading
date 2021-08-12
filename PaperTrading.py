import datetime     # for current time
import thread    # for multiple thread
import json          
import requests     
import stockclass 


def premarket():
    currtime = datetime.now().strft('%H:%M')
    if currtime >= '09:15' and currtime < '09:30':
        return True
    else:
        return False

def markethour():
    currtime = datetime.now().strft('%H:%M')
    if currtime >= '09:30' and currtime < '15:30':
        return True
    else:
        return False

domain = 'https://api-fxpractice.oanda.com/v20/'                        
access_token = '4IKvDuPZBZaxd8Zlu5z79i9M'
account_id = "101-004-16885108-001"

def get_lvp(share):
    response = requests.get(url = domain+'prices', params = {'instruments':share.id()})
    file = open(share.id()+'.json','w')
    json.dump(response,file,indent = 4)
    file.close()
    return jsonify(response)

def place_order(share,signal,sl):
    response = requests.post(url = domain+'accounts/'+account_id+'/orders',
                           params = {'instruments':share.id(),
                                     'units': 2,
                                     'side':signal,
                                     'type':'market',
                                     'stopLoss':sl})
    print('Order placed for'+signal+' at'+datetime.now().strft('%H:%M'))

    return jsonify(response)
def transaction(share):
    lvp = get_lvp(share)
    if not share.status():
        if lvp >= share.orh():
            place_order(share,'BUY',share.orl())
            share.status_update('BUY')
        elif lvp <= share.orl():
            place_order(share,'SELL',share.orh())
            share.status_update('SELL')
    else:  
        # stop loss is hit
        if ( share.status() == 'BUY' and lvp < share.orl() ) or ( share.status() == 'SELL' and lvp > share.orh() ):
            share.status_update('')



if __name__ == "__main__":
    # mentioning 3 stocks 
    t1 = stock('id')
    while premarket():
        thread.start_new_thread( t1. update_or, get_lvp(t1)) 
       # t1.update_or(get_lvp(t1))
    while markethour()
        transaction(t1)
    

