import json
import requests

def test_oauth_api():

    token_url = "https://restful-booker.herokuapp.com/auth"

    data = {"username":"admin","password":"password123"}
    response = requests.post(token_url,data)
    print(response.text)

    

#Get_API_Hit

url = "https://restful-booker.herokuapp.com/booking"
response_code = requests.get(url)
print(response_code)
response_result = (json.dumps(response_code.json(),indent =4))
print(response_result)


#Create_booking

body = json.dumps({
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": "true",
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=body)
print(response.text)
print(response_code)
