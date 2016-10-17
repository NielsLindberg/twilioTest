from twilio.rest import TwilioRestClient

account_sid = "ACbeac55dacc75d069a773c33d9e4381ab" # Your Account SID from www.twilio.com/console
auth_token  = "2acd45094ff038a48f51f4d4f4c16e13"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    from_="+13375141841",    # Replace with your phone number
    to="+4527490778") # Replace with your Twilio number

print(message.sid)