from flask import Flask, redirect, render_template, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)
app.config['DEBUG'] = True


    



@app.route("/")
def index():
    template = jinja_env.get_template('base.html')
    return render_template('base.html', username='', username_error='', password='', password_error='', verify_password='', verify_password_error='', email='', email_error='')
    

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or username == '' or ' ' in username:
        username_error = "Please enter a valid username" 
        username = ''

    if len(password) < 3 or len(password) > 20 or password == '' or ' ' in password: 
        password_error = "Please enter a valid password"
        password = ''

    if not verify_password == password:
        verify_password_error = "Your passwords don't match"
        verify_password = ''

    if len(email) < 3 or len(email) > 20 or '@' not in email or '.' not in email:
        email_error = "Please enter a valid email address"
        email = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        #success!
        template = jinja_env.get_template('welcome.html')
        return render_template('welcome.html', username=username)
    
    else:
        template = jinja_env.get_template('base.html')
        return render_template(username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, verify_password=verify_password, email=email)



@app.route("/welcome", methods=['POST'])
def welcome():
    username=request.form['username']
    template = jinja_env.get_template('welcome.html')
    return render_template('welcome.html', username=username)


app.run()