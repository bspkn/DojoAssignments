# We'll need the session object to manage session variables
# render_template to render html content from templates
# url_for to extract the url for a given view/route
# request to access the GET data request for the form view
# redirect to perform redirects to different routes
from flask import Flask, session, render_template, url_for, request, redirect

app = Flask(__name__)

# Sessions variables are stored client side, on the users browser
# the content of the variables is encrypted, so users can't
# actually see it. They could edit it, but again, as the content
# wouldn't be signed with this hash key, it wouldn't be valid
# You need to set a scret key (random text) and keep it secret
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def index():

    if "number" not in session:
        session['number'] = randint(0,100)
    print session['number'], "This is the number"
    return render_template('index1.html')

@app.route('/guess', methods=['POST'])
def numberGuess():
    guess = int(request.form['guess'])
    print type(guess)
    if guess < session['number']:
        print "in low if"
        session['guess'] = "low"
    elif guess > session['number']:
        print "in high elif"
        session['guess'] = "high"
    else:
        print 'in match'
        session['guess'] = "match"
    return redirect('/')

@app.route('/reset')
def newGame():
    session.clear()
    return redirect('/')

app.run(debug=True)
