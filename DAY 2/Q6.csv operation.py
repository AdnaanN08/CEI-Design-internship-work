import pandas as pd
import requests as rq
import time as t

url = "http://api.open-notify.org/iss-now.json"

data_list = []

for i in range(10):
    
        response = rq.get(url)
        response.raise_for_status()
        req_data = response.json()
        
        timestamp = req_data['timestamp']
        latitude = req_data['iss_position']['latitude']
        longitude = req_data['iss_position']['longitude']
        
     
        data_list.append([timestamp, latitude, longitude])

        print(f"Data added for iteration {i}")
        
        t.sleep(1)  

data = pd.DataFrame(data_list, columns=['timestamp', 'latitude', 'longitude'])

data.to_csv('q6.csv', index=False)

print ("data added in csv")
