import requests
import pandas as pd
import sys

print("*"*20,"GITHUB TRACKER","*"*20)

nme = input("ENTER YOUR GITHUB USERNAME--> ")

try:
 responce = requests.get(f"https://api.github.com/users/{nme}")
 status = responce.status_code # to the see the server reaction 
# print(responce.headers['Content-Type']) # to see the format of the responce

 data = responce.json()


 if status != 200:
    print("BRO ERROR CAME ")
    sys.exit()

  
   
 clean_data = []


 repo = {"name":data['name'],
         "username":data['login'],
            "bio":data['bio'],
            'total repos':data['public_repos'],
            'followers':data['followers'],
            'following':data['following'],
            'G_date':data['created_at'][0:10],
            "location":data['location']
            }
 clean_data.append(repo)


 _ = pd.DataFrame(clean_data)
 _.to_excel("new.xlsx",index = False)
except:
  print("COULDN'T DO BRO")








