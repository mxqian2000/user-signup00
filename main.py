
from flask import Flask, request, redirect, render_template
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

@app.route("/", methods = ['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username)<3 or len(username)>20:
        username_error = 'This is not a valid username'
    if len(password)<3 or len(password)>20:
        password_error = 'This is not a valid password'  
    if verify != password:
        verify_error = "Password and verify do not match"  
    if len(email) < 3 or len(email) > 20:
        email_error = "That's not a valid email"
    if ' ' in email or '@' not in email or '.' not in email:
        email_error = "That's not a valid email"
    
    if not username_error and not password_error and not verify_error and not email_error:    
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('form.html', username = username, username_error = username_error, password_error = password_error, 
         verify_error = verify_error, email = email, email_error = email_error)

@app.route("/welcome", methods = ['POST', 'GET'] )
def welcome_page():
    username = request.args.get('username')
    return render_template("welcome.html", username = username) 
    
app.run()
