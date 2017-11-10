<<<<<<< HEAD
=======

>>>>>>> 639aaef86a9b879b60af04fa29f568e6a4f48dca
from flask import Flask,render_template,request, sessions, redirect, url_for
from .forms import SignupForm
from .models import db, User
from . import app

<<<<<<< HEAD
#postgres sql
=======
#postgres sql 
>>>>>>> 639aaef86a9b879b60af04fa29f568e6a4f48dca
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'
db.init_app(app)

#secretkey for login

app.secret_key = 'development-key'

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/signup" , methods = ['GET','POST'])
def signup():
	form = SignupForm()
	if request.method == "POST":
		if form.validate() == False:
			return render_template('signup.html',form = form)
		else:
			newuser = User(form.first_name.data, form.last_name.data , form.email.data, form.password.data)
<<<<<<< HEAD

=======
			
>>>>>>> 639aaef86a9b879b60af04fa29f568e6a4f48dca
			db.session.add(newuser)
			db.session.commit()

			#session['email'] = newuser.email
			return redirect(url_for('home'))
	elif request.method =="GET":

		return render_template('signup.html',form = form)


@app.route("/home")
def home():
	return render_template('index.html')

#create a room decorator by jack
@app.route("/create")
def create_page():
	return render_template("create_page.html")

@app.route("/browseComedy")
def browse_comedy():
	return render_template("search_comedy.html")

@app.route("/browseActing")
def browse_acting():
	return render_template("search_acting.html")

if __name__ == "__main__":
	app.run(debug=True)
<<<<<<< HEAD
=======
	
>>>>>>> 639aaef86a9b879b60af04fa29f568e6a4f48dca
