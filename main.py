from flask import Flask,render_template,request,redirect,session
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1",user="root",password="@Svlad2305",database="login",auth_plugin='mysql_native_password')
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
    query = "SELECT * FROM `user` WHERE `email` LIKE %s and `password` LIKE %s"
    cursor.execute(query,(email,password))
    users = cursor.fetchall()
    #return "The email is {} and the password is {}".format(email,password )
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('login.html')
    #print(users)

    #return "Hello"
#@app.route('/home')
#def home():
#    return render_template('home.html')
@app.route('/add_user',methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    query = 'INSERT INTO user VALUES(3,name,email,password)'
    cursor.execute(query)
    conn.commit()
    return "User registered Successfully"
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)