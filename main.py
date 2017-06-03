from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('interface.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	while True:
        bot_response = kernel.respond(message)
        return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)