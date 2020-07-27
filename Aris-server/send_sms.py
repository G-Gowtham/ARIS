import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message='YOUR VECHICLE MAY BE accidented \n please verify'&language=english&route=p&numbers=7094024150,7397196487"
headers = {'authorization': "jG6FRZkW9h0DoqUdAcsaIumEyBgbNlwTYrCMvHK3izP1x4V5JXGCNMdmAPV2le1QI03BjgUFOESviqHn",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
