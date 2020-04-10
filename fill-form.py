import requests
url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSd5NX1jRwPFu1h8ZQz2UAwYA__ihYr0XcwmPafbJjztuuZb6g/formResponse"
data = {
    "entry.1564564753": "Amartya Mondal", #Your name
    "entry.45339518": "1801ME07", #Your roll number
    "entry.1286705147": "8967570983", #Your phone number
    "entry.1381581746": "1801me07@iitp.ac.in", #Your email
    "entry.618759938": "HS202 - Introductory Macroeconomics", #Course name
    "entry.365693181": "100%",  #Q.1. Compared to in-class, satisfaction with respect to online content delivery is:
    "entry.2105058604": "100%",  #Q.2. Compared to in-class, satisfaction with respect to ease of understanding is :
    "entry.612816140": "100%",  #Q3 Q.3. Compared to in-class, satisfaction with respect to the speed at which topics are covered is: *
    "entry.1150798786": "Excellent",  # Q4: Internet connectivity in your locality
    "entry.207978893": "Yes",  #Q.5. Would you like to continue the online teaching mode (during this pandemic situation?)
}

response = requests.post(url, data)
print(response)