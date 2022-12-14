from flask import Flask,render_template,request,redirect,session
from DataBase import Database
from MyApi import API
# Flask run on server,it sends HTML,CSS,JavaScript file to the client
# PyCharm - Server, Google Web-Site - Client
# All HTML files in flask should be in 'templates' Directory --- automatically some HTML code will be their & that is called 'Boilerplate code'
# 'render_templat e' --> to integrate anything which we are writing in HTML(i.e.,in login.html) in app.py(i.e.,in login page) ,Its work is to load HTML files.
# 'request' --> It is used to receive data which is coming from HTML
# 'redirect' --> Use to send control from one route to another
# 'session' --> It tell us whether the user is logged-in user or not. Its a kind of dictionary, where we store things
app = Flask(__name__)
app.secret_key = 'adewgvdfbyjnesbtgbzd'
dbo = Database()
apio = API()
# Routes are used to create URL
# Below code created a server on my machine whose URL is showing in result if we run this
# If someone put '/' at the end of my website URL the below function will be executed.
@app.route('/')
# Our task is when we put '/' on URL & press enter the it will show me refreshed login Page
# Function will return HTML,CSS files.
def index():
    return render_template('login.html')
# debug = True --> If we don't use this, then if we do some changes inside the function we need to run the code again-and-again, after using this if I can do some changes inside that function,then by refreshing the website we will get result.


@app.route('/register')
def register():
    return render_template('register.html')

# 'request' is used to receive data which is coming from HTML & use 'methods' to tell flask through which way data is coming
@app.route('/perform_registration',methods=["post"])
def perform_registration():
    # below code used to get that data
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    #Below code is used to give data to DataBase Module & DataBase Module will store that data into dictionary which is in users_data.json
    response = dbo.insert(name,email,password)
    if response:
        # After data is successfull saved in json, redirect page to login page
        # Sending 'login.html' and 'message' to client, & in HTML file we will write if the 'message' on client side received or not ---> writing Python in HTML
        return render_template('login.html',message="Registration Successful, Kindly Login to Proceed")
    else:
        return render_template('register.html',message='Email Already Exists')


@app.route('/perform_login',methods=['post'])
def perfrom_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email,password)

    if response:
        # If user have logged-in successfully, then we set 'logged_in' as key & '1' as value in 'session' which is a dictionary
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message="Incorrect Email/Password")


@app.route('/profile')
def profile():
    # We are checking whether any variable is in session or not
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


# This function will trigger when we click on 'Name Entity Recognition' in client side
@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')


@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = apio.ner(text)
        return render_template('ner.html',response=response)
    else:
        return redirect('/')


@app.route('/sentiment_analysis')
def sentiment_analysis():
    if session:
        return render_template('sentiment.html')
    else:
        return redirect('/')


@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    if session:
        text = request.form.get('sentiment_analysis_text')
        response = apio.sentiment_analysis(text)
        return render_template('sentiment.html',response=response)
    else:
        return redirect('/')


@app.route('/abuse_detection')
def abuse_detection():
    if session:
        return render_template('abuse.html')
    else:
        redirect('/')


@app.route('/perform_abuse_detection',methods=['post'])
def perform_abuse_detection():
    if session:
        text = request.form.get('abuse_detection_text')
        response = apio.abuse_detection(text)
        return render_template('abuse.html',response=response)
    else:
        return redirect('/')

app.run(debug=True)