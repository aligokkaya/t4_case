# import requests

# r=requests.get('http://127.0.0.1:8000/v1/t4/')

# print(r.text)

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="164.92.161.222",
#   user="root",
#   password="Challenge_t4"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)






###########  3. Madde
# import json
# import requests


# with open('MeetingData.json', 'r') as f:
#   data = json.load(f)

# js={'data':data}
# # print(js)
# res = requests.post("http://127.0.0.1:8000/v1/t4/upload/",data=json.dumps(js))


# print(res.content)
# print(res.status_code, res.json())


################ 4.Madde 1. Kısım
# import requests
# res = requests.post('http://127.0.0.1:8000/v1/t4/email',
#     headers = {
#         #'User-agent'  : 'Internet Explorer/2.0',
#         'Content-type': 'application/json'
#     },
#     json = {"email": "emma@acompany.com"},
# )
# #print(res.headers['content-type'])
# print(res.text)


################ 4.Madde 2. Kısım

# import requests
# res = requests.post('http://127.0.0.1:8000/v1/t4/meet',
#     headers = {
#         #'User-agent'  : 'Internet Explorer/2.0',
#         'Content-type': 'application/json'
#     },
#     json = {
#         "email": "douglas@acompany.com",
#         "date":"2022-5-6 10:00"
#     },
# )
# #print(res.headers['content-type'])
# print(res.text)

################### 5. Madde
import json
import requests


with open('AdditionalMeetingData.json', 'r') as f:
  data = json.load(f)

js={'data':data}
# print(js)
res = requests.post("http://127.0.0.1:8000/v1/t4/update/",data=json.dumps(js))