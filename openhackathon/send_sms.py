import africastalking

# TODO: Initialize Africa's Talking

username='sandbox'
api_key='142b215addce4ea72af35e4b520ddd92458d607d6215971a09c8e6f7c00793ed'
africastalking.initialize(username, api_key)


class send_sms():
    sms = africastalking.SMS

    def sending(self):
        # Set the numbers in international format
        recipients = ["+254745606530"]
        # Set your message
        message = "Hello. An investor is interested in your project."
        # Set your shortCode or senderId
        sender = "17179"
        try:
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print (f'Houston, we have a problem: {e}')