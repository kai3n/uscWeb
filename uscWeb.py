from flask import Flask, request, render_template, url_for, redirect, session
from passlib.hash import sha1_crypt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dash/')
def dash():
    return render_template("dash.html")


@app.route('/test2/<username>')
def test2(username):
    return '<h2>%s</h2>' % username


@app.route('/test3/<int:idn>')
def test3(idn):
    return '<h2>%s</h2>' % idn


@app.route('/test4', methods=['GET','POST'])
def test4():
    if request.method == 'GET':
        return "GET"
    else:
        return "POST"


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


@app.route('/login/', methods=['GET','POST'])
def login_page():

    error = ""
    print(1)
    try:
        print(2)
        if request.method == "POST":
            print(3)
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            print(4)
            if attempted_username == "root" and attempted_password == "root":
                print(5)
                return redirect(url_for('dash', name=attempted_username))
            else:
                error = "Invalid credentials. Try Again."
        return render_template('login.html', error=error)
    except Exception as e:
        print(e)
        return render_template('login.html', error=error)


#@app.route('/register/', methods=['GET','POST'])
#def register_page():
#    try:
#        #db_connection
#        password = sha256_crypt.encrypt(pass))
#    except Exception as e:
        return(str(e))

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
