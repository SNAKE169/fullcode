from  flask import Flask, request
# from Chatbot.chatbot import my_supreme_bot,FACEBOOK_URL
from chatbot import my_supreme_bot, FACEBOOK_URL
app = Flask(__name__)
import json
import requests


page_token = "EAAEUWPZAwhEsBALB2gvCmD2NEmHQizwnbwNcenjo4CTBoSLBbLn6LZCDZA3PHHnHIBbYKiv3Bo4LV4ZA3DXBQhzZCGFbEFc9MZAvEzfu5ByWCSh9YQ3MmX0lZCScGSe76jwyW91XGZCwipLe1fsUoT3g1oAbVvgcb2vkHO6BqnGlFQfCzEUBnqmJi1ZCrXag0Kd0ZD"
my_bot = my_supreme_bot(page_token)
my_bot.send_image_to_cloud()
@app.route('/',methods=["GET","POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challange = request.args.get("hub.challenge")
        if token == "secret":
            return challange
        return "400"

    #handle post request
    else:
        message_data = request.get_json()
        print(message_data)
        messaging_events = message_data["entry"][0]["messaging"]
        #loop throgh all mess -event
        for message in messaging_events:
            user_id = message["sender"]["id"]

            #handle post-back req
            if message.get("postback"):
                my_bot.send_image_from_cloud(user_id, idol_name = message.get("postback").get("payload"))

            #handle text-based mess req
            if message.get("message") and message.get("message").get("text"):

                user_info = requests.get("https://graph.facebook.com/v8.0/",  params = {"id":user_id,"access_token":page_token} )
                user_data = user_info.json()

                user_name = user_data["first_name"]
                my_bot.send_message(user_id,"Hi {}\nWhich JAV Idol you wanna watch?".format(user_name))
                my_bot.send_buttons(user_id)



        return "200"

if __name__ == "__main__":
    app.run(debug=True)