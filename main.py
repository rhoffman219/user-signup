from flask import Flask, redirect, render_template, request



app = Flask(__name__)
app.config['DEBUG'] = True


    



@app.route("/")
def index():
    return render_template('base.html')

@app.route("/", methods=['POST'])
def validate():
    username = ''
    password = ''
    verify_password = ''
    email = ''
    if len(username) < 3 or len(username) > 20 or username == '' or '' in username:
        return "Please enter a valid username"
    else: 
        return username 

    if len(password) < 3 or len(password) > 20 or password == '' or '' in password: 
        return "Please enter a valid password"
    else:
        return password

    if verify_password == password:
        return verify_password
    else:
        return "Please enter a valid password"

    if len(email) < 3 or len(email) > 20 or '@' not in email or '.' not in email:
        return "Please enter a valid email address"
    else:
        return email


@app.route("/welcome", methods=['POST'])
def welcome():
    return render_template('welcome.html')


app.run()