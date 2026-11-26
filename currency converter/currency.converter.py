import requests

import requests

url = "https://api.frankfurter.dev/v2/rate/USD/INR"

response = requests.get(url)

output=response.json()

while True:
   
 y= output["rate"]

 x = float(input("enter dollor : "))
 if x == 0:
   break
 def conv(x,y):
   print(x*y,"rupee")

 conv(x,y) 
