import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=ARIS&message='\nAccident Detected \n\n Vehicle No : TN 45 AA 5797 \n\n Date and Time: 17:07, 3 FEB 2020\n\n Location: Asthampatty,Salem,TamilNadu\n\n Spot (GPS Hashcode): tdpd6hk7qhsp'&language=english&route=p&numbers=7010406958"
headers = {'authorization': "jG6FRZkW9h0DoqUdAcsaIumEyBgbNlwTYrCMvHK3izP1x4V5JXGCNMdmAPV2le1QI03BjgUFOESviqHn",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)