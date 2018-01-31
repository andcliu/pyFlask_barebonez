from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# just self preference
render = render_template
req = request

########################## routing ###########################

@app.route('/')
def index():
	return render('index.html')


######################## end routes #########################

# debug mode on
app.run(debug=True)