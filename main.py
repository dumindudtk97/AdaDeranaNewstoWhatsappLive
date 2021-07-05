from twilio.rest import Client 
from test import send_msg

account_sid = 'ACc9a93827120de9e22ecaccd21610c94d' 
auth_token = '678b849a15cf4d0631e901a2f6af5a97' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='nice',      
                              to='whatsapp:+94711870149' 
                          ) 
 
print(message.sid)
