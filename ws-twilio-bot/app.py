from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *
from dateutil.parser import parse


app = Flask(__name__)
count=0

@app.route("/sms", methods=['POST'])
def reply():

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message = response.message() 
    responded =False
    words = incoming_msg.split('@')
    
    if "Hello" in incoming_msg:
        reply = "Hello! \nDo you want to set a reminder?"
        message.body(reply)
        responded = True
    
    if len(words) == 1 and "Yes" in incoming_msg:
        reminder_string = "Please provide date in the following format only.\n\n"\
        "*Date @* _type the message_"
        message.body(reminder_string)
        responded = True
    
    if len(words) == 1 and "No" in incoming_msg:
        reply = "Ok. Have a nice day!"
        message.body(reply)
        responded = True
    
    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()

        if input_type == "date":
            reply = "Please enter the reminder message in the following format only.\n\n"\
            "*Reminder @* _type the message_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True
        
        if input_type == "reminder":
            reply = "Your reminder is set!"
            set_reminder_body(input_string)
            message.body(reply)
            responded = True
    
    if not responded:
        message.body('Incorrect request format. Please enter in the correct format')
    
    return str(response)

def set_reminder_date(msg):
    p = parse(msg)
    date = p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0

def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0

if __name__ == "__main__":
    app.run(port=5000)




'''app = Flask(__name__)

@app.route("/")
    def hello():
    return "Hola, mundo!"

@app.route("/sms", methods=['POST'])
def bot():
    user_msg = request.form.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    if 'Hola' in user_msg:
        msg.body("Hola amigo! Como puedo ayudarte")
    
    elif 'Machine learning' in user_msg:
        msg.body("Machine Learning (ML) o aprendizaje automático, es un subcampo de la inteligencia artificial (IA) que se enfoca en desarrollar algoritmos y modelos que permiten a las computadoras aprender de datos y realizar tareas específicas sin ser programadas explícitamente para hacerlo.")
        msg.body('Puedes aprender Machine learning desde aqui https://www.youtube.com/watch?v=7ClLKBUvmRk&t=3s')
    
    elif'Image processing' in user_msg:
        msg.body("El procesamiento de imágenes se refiere al conjunto de técnicas y algoritmos utilizados para manipular y analizar imágenes digitales. El procesamiento de imágenes se utiliza en una amplia variedad de aplicaciones, como la visión artificial, la fotografía digital, la medicina, la seguridad y la robótica.")
    
    elif 'Natural language processing' in user_msg:
        msg.body("El Procesamiento de Lenguaje Natural (NLP, por sus siglas en inglés) es una rama de la inteligencia artificial que se enfoca en la interacción entre las computadoras y el lenguaje humano natural. El objetivo del NLP es permitir que las computadoras procesen, comprendan y generen lenguaje humano natural.")
    
    elif 'Quien' in user_msg:
        msg.body("Fui creado por GLM usando Python, Flask, NGRok y Twilio")

    elif 'Cita' in user_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'No he podido encontrar lo que solicitas en este momento'
        msg.body(quote)
    
    elif 'Gato' in user_msg:
        msg.media('https://cataas.com/cat')
    
    else:
        msg.body("Disculpe, No entendi lo que dijiste")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)'''


'''app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola, mundo!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    reply = fetch_reply(msg, phone_no)

    resp = MessagingResponse(reply)
    resp.message()

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)'''
    