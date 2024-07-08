import json 
import requests as rq
from datetime import datetime , timedelta 

date = "2024-07-07"
url = "https://vegetablemarketprice.com/api/dataapi/market/delhi/daywisedata?date="+str(date)+""

header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"en-US,en;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"_ga=GA1.1.1519398408.1720413849; JSESSIONID=61535A659930ABE1AA29E3BF135716FC; __gads=ID=061360f3159afb96:T=1720413849:RT=1720421494:S=ALNI_MYzlpuMrnRpLWVL16MVOf1P43EZ1A; __gpi=UID=00000e86a175ba29:T=1720413849:RT=1720421494:S=ALNI_MbbkgIPCSQUYjrdD1luIfyfewBrLg; __eoi=ID=5e2c15fc9eaf9e7f:T=1720413849:RT=1720421494:S=AA-AfjYsxfAiCWWhnoUuxAsqzvii; _ga_2RYZG7Y4NC=GS1.1.1720421494.2.1.1720421521.0.0.0; FCNEC=%5B%5B%22AKsRol92hPUKRBt2nrX6HGGbaEgt6-cUNLzj2WoVjUAPgVi-tWOu7sZGN-ygMeGiRw9YK7SglmYlZclAmXkZRQgUqQ52abMxUMNOARh1aHDDpD_fo95snS53ut4fOa2uLChEHq-Q4jcD-3tIpXfjG1M8E6szsebePA%3D%3D%22%5D%5D",
"Host":"vegetablemarketprice.com",
"Referer":"https://vegetablemarketprice.com/",
"Sec-Ch-Ua-Mobile":"?0",
"Sec-Ch-Ua-Platform":"Windows",
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-User":"?1",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

response = rq.get(url,headers=header)
print(response.text)
