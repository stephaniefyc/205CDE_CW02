from flask import Flask, render_template, request, session, redirect, url_for, send_file
import pymysql

app = Flask(__name__)
app.secret_key = 'development key'

db = pymysql.connect("localhost", "stephanie", "123456789a", "m_edu")

#home page
@app.route("/home")
@app.route("/")
def home():
	return render_template('CW02/home.html')

#later news page
@app.route("/news")
def news():
	return render_template('CW02/news.html')

# join free trial - register page
@app.route("/signup")
def student():
	return render_template('CW02/signup.html')

@app.route('/insert', methods=["POST", "GET"])
def result():
	if request.method == "POST":
		stname = request.form["stname"]
		pwd = request.form["password"]
		tel = request.form["tel"]

		cursor = db.cursor()
		cursor.execute("""insert into user (stname, password, tel) values (%s, %s, %s)""", (stname, pwd, tel))
		
		try:
			db.commit();
			msg = "Congratulations! You have successfully registered for our free trial. Our staff will contact you as soon as possible."
		except Exception as e:
			db.rollback();

		return render_template("CW02/signup_msg.html", msg = msg)			

#free trial login page
@app.route("/materials")
def materials():
	return render_template('CW02/login.html/')
	

# download the file
@app.route('/download_file_p1')
def download_file_p1():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p1.pdf')

@app.route('/download_file_p2')
def download_file_p2():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p2.pdf')

@app.route('/download_file_p3')
def download_file_p3():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p3.pdf')

@app.route('/download_file_p4')
def download_file_p4():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p4.pdf')

@app.route('/download_file_p5')
def download_file_p5():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p5.pdf')

@app.route('/download_file_p6')
def download_file_p6():
	return send_file('/home/stephanie/205CDE/static/uploads/freetrial_ex_p6.pdf')

# login page
@app.route("/loginPage", methods=['POST', 'GET'])
def login():
	error = ''
	msg = ''
	if request.method == 'POST':
		stname = request.form["stname"]
		pwd = request.form["password"]

		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		cursor.execute('SELECT stname, password FROM user WHERE stname = %s AND password = %s', (stname,pwd))
		users = cursor.fetchone()

		if users:
			session['stname'] = stname
			session['password'] = pwd

			return redirect(url_for("uploadmaterials"))
		else:
			error = 'Your password or student name is not true, please try again!'
			return render_template("CW02/login.html", error = error)
		
	return render_template("CW02/login.html")
	db.close()

# logout
@app.route("/logout")
def layout():
	return redirect(url_for("login"))

# course - K2~K3 page
@app.route("/kind")
def kind():
	return render_template('CW02/kind.html')

# course - P1~P3
@app.route("/junior")
def junior():
	return render_template('CW02/junior.html')

# course - P4~P6
@app.route("/senior")
def senior():
	return render_template('CW02/senior.html')

# exercise page
@app.route("/meterials")
def exercise():
	return render_template('CW02/meterials.html')

# reservation page
@app.route("/reservation")
def reservation():
	return render_template('CW02/reservation.html')

# reserve form
@app.route('/succesreserve', methods=["POST", "GET"])
def succesreserve():
	if request.method == "POST":
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		school = request.form["school"]
		grade = request.form["grade"]
		birth = request.form["birth"]
		tel = request.form["tel"]

		cursor = db.cursor()
		cursor.execute("""insert into reservation (firstname, lastname, school, grade, birth, tel) values (%s, %s, %s, %s, %s, %s)""", (firstname, lastname, school, grade, birth, tel))
		
		try:
			db.commit();
			msg = "Congratulations! You have successfully registered. Our staff will contact you as soon as possible."
		except Exception as e:
			db.rollback();

		return render_template("CW02/reservation_msg.html", msg = msg)

# seaech waiting
@app.route("/waitinglist", methods=["POST", "GET"])
def waitinglist():
	error = ''
	if request.method == "POST":
		tel = request.form["tel"]

		cursor = db.cursor()
		cursor.execute('SELECT * FROM reservation WHERE tel = %s',(tel))
		result = cursor.fetchall()
		return render_template('CW02/waitinglist.html', data = result)

		try:
			cursor = db.commit();
			error = 'Sorry we cannot found your phone, please try again.'
		except Exception as e:
			db.rollback();
		return redirect(url_for("waitinglist", error = error))

	return render_template('CW02/waitinglist.html')

# contact us page
@app.route("/contactus")
def contactus():
	return render_template('CW02/contactus.html')

@app.route("/adminhome")
def adminhome():
	return render_template("CW02/adminhome.html")

# admin login page
@app.route("/adminloginpage", methods=['POST', 'GET'])
def adminlogin():
	error = ''
	msg = ''
	if request.method == 'POST':
		username = request.form["username"]
		pwd = request.form["password"]

		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		cursor.execute('SELECT username, password FROM admin WHERE username = %s AND password = %s', (username,pwd))
		users = cursor.fetchone()

		if users:
			session['username'] = username
			session['password'] = pwd

			msg = session['username'] + ' ,this is admin page.' 
			return render_template("CW02/adminhome.html", msg = msg)
		else:
			error = 'Your User Name or Password is not true, please try again!'
			return render_template("CW02/admin.html", error = error)
		
	return render_template("CW02/admin.html")
	db.close()

# admin signup page
@app.route('/adminsignup', methods=["POST", "GET"])
def adminsignup():
	if request.method == "POST":
		username = request.form["username"]
		pwd = request.form["password"]

		cursor = db.cursor()
		cursor.execute("""insert into admin (username, password) values (%s, %s)""", (username, pwd))
		
		try:
			db.commit();
			msg = "Welcome to join M Education Center! Please remember the username and password."
		except Exception as e:
			db.rollback();

		return render_template("CW02/adminsignup_msg.html", msg = msg)

	return render_template("CW02/adminsignup.html")	

# admin page upload materials
@app.route("/adminupload", methods=["POST", "GET"])
def adminupload():
	msg = ''
	if request.method == "POST":
		classname = request.form["classname"]
		grade = request.form["grade"]
		eximage = request.form["eximage"]
		ex = request.form["ex"]

		cursor = db.cursor()
		cursor.execute("""insert into materials (classname, grade, eximage, ex) values (%s, %s, %s, %s)""", (classname, grade, eximage, ex))

		try:
			db.commit();
			msg = 'Succes upload the materials.'
		except Exception as e:
			db.rollback(); 
		return render_template("CW02/adminupload.html", msg = msg)	

	return render_template("CW02/adminupload.html")

# updata the materials page
@app.route("/uploadmaterials", methods = ["POST", "GET"])
def uploadmaterials():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM materials')
	result = cursor.fetchall()
	print (result)
	msg = 'Hello '+ session['stname'] + '. You can download the materials for free trial.'

	return render_template('CW02/materials.html', result = result, msg = msg)

#admin check the materials page
@app.route("/adminmaterials")
def adminmaterials():
	return render_template('CW02/materials.html')
		
# admin page show waiting list and search
@app.route("/adminwaitinglist", methods=["POST", "GET"])
def adminwaitinglist():
	error = ''
	cursor = db.cursor()
	cursor.execute('SELECT * FROM reservation')
	result = cursor.fetchall()
	print(result)

	if request.method == "POST":
		tel = request.form["tel"]

		cursor = db.cursor()
		cursor.execute('SELECT * FROM reservation WHERE tel = %s',(tel))
		result = cursor.fetchall()
	else:
		error = 'Your phone nuber cannot found, please try again!'	

		return render_template('CW02/adminwaitinglist.html', data = result, error = error)

	return render_template("CW02/adminwaitinglist.html", data = result)



if __name__ == '__main__':
	app.run(debug = True)