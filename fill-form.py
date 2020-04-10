import requests
url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSd5NX1jRwPFu1h8ZQz2UAwYA__ihYr0XcwmPafbJjztuuZb6g/formResponse"
data = {
    "entry.1564564753": "Your name", #Your name
    "entry.45339518": "Your roll number", #Your roll number
    "entry.1286705147": "your phone number", #Your phone number
    "entry.1381581746": "your institute email id", #Your email
    "entry.618759938": "Subject name. U can get this from the from", #Course name
    "entry.365693181": "100%",  #Q.1. Compared to in-class, satisfaction with respect to online content delivery is:
    "entry.2105058604": "100%",  #Q.2. Compared to in-class, satisfaction with respect to ease of understanding is :
    "entry.612816140": "100%",  #Q3 Q.3. Compared to in-class, satisfaction with respect to the speed at which topics are covered is: *
    "entry.1150798786": "Excellent",  # Q4: Internet connectivity in your locality
    "entry.207978893": "Yes",  #Q.5. Would you like to continue the online teaching mode (during this pandemic situation?)
}

response = requests.post(url, data)
print(response)