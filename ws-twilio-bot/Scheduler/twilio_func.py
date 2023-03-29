from twilio.rest import Client
account_sid = 'ACfcc631f81b3586fb7f430f86b7a64504' #Add your Twilio Account's SID
auth_token = 'b2117613b75f769d7d19428e666f5238' #Add your Twilio Account's Auth Token
client = Client(account_sid, auth_token)

def send_rem(date, rem):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='*REMINDER* '+date+'\n'+rem,
        to='whatsapp:+584246768282' #Add your WhatsApp No. here
    )
    print(message.sid)