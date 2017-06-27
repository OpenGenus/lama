from flask import Flask, render_template, request, jsonify
import aiml
import os
from trigger import *
import brain.hi.trigger as HI

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/hi", methods=['POST'])
def hi():
	message = "Hi! <br>"
	image = str(HI.random())
	bbuu = '<img src="'+image+'" alt="ShinChan">'
	bot_response = message+bbuu
	return jsonify({'status':'OK','answer':bot_response})


@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("brain/aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = kernel.respond(message)
	        return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)
