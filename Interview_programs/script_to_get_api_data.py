import requests
import json
dist =[{'dest_type':"city",'dest_id':20126394},
       {'dest_type':"district",'dest_id':3160},
       {'dest_type':"airport",'dest_id':125},
       {'dest_type':'landmark','dest_id':261403},
       {'dest_type':'city','dest_id':-1556558}]
number = 0
numval = 0
results = []
for val in dist:
    url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"
    querystring = {"offset":"0","arrival_date":'2023-08-25',
        "departure_date":'2023-08-26',"guest_qty":"1","dest_ids":val['dest_id'],"room_qty":"1",
        "search_type":val['dest_type'],"children_qty":"2",
        "children_age":"5,7","languagecode":"en-us"
    }
    headers = {
        "X-RapidAPI-Key": "ded369cee6mshfc54fe5c1f28843p15a929jsn5db40c4b1d78",
        "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    value = data['result']
    results.append(value)
    file = open('rapid_hotels_data.json','w')
    for r in value:
        json.dump(r, file, indent = 6)
        #file.write(r)
    file.close()
    
print("results....................................",results)
