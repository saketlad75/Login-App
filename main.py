from flask import Flask,render_template,request
import mysql.connector
conn = mysql.connector.connect(host="%",user="saket",password="@Svlad2305",database="login")
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/register')
def reg():
    return render_template('register.html')
@app.route('/login_validation',methods=['POST'])
#Whenever we use form us use POST Method,the data is stored in the requests
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE{} AND `password` LIKE {}""".format(email,password))
    users = cursor.fetchall()
    #return "The email is {} and the password is {}".format(email,password )
    return users
#@app.route('/home')
#def home():
#    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)