from twilio.rest import Client 
from test import send_msg

account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='nice',      
                              to='whatsapp:+94711870149' 
                          ) 
 
print(message.sid)
