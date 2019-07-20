from flask import *
import time
import mysql.connector

app = Flask(__name__)
root ={}

def insert(sql):
	conn = mysql.connector.connect(user='root', password='123456', database='chat')
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

def select(sql):
	conn = mysql.connector.connect(user='root', password='123456', database='chat')
	cursor = conn.cursor()
	cursor.execute(sql)
	results = cursor.fetchall()
	conn.close()
	return results

@app.route('/', methods=['GET','POST'])
def index():
	if root:
		sql = "select * from c_blog"
		blogs = select(sql)
		return render_template('index.html', names=root[1], blogs=blogs)
	else:
		return render_template('login.html')

@app.route('/regist', methods=['GET','POST'])
def regist():
	return render_template('regist.html')

@app.route('/login', methods=['GET','POST'])
def login():
	global root
	if root:
		root ={}
		return render_template('login.html')
	sql = "select * from c_user where user_name='"+request.form.get('user')+"' and passcode='"+request.form.get('password')+"'"
	results = select(sql)
	#return str(results)
	if len(results)==1:
		root = results[0]
		sql = "select * from c_blog"
		blogs = select(sql)
		#return render_template('index.html',names=root[1], blogs=blogs)
		return redirect(url_for('index'))
	else:
		return render_template('login.html')

@app.route('/registuser', methods=['GET','POST'])
def getRigistRequest():
	sql = "select * from c_user where user_name='"+request.form.get('user')+"'"
	results = select(sql)
	if len(results)==1:
		return """<script>alert("该用户名已被注册！")</script>"""
	else:
		sql = "INSERT INTO c_user(user_name, passcode) VALUES ('"+request.form.get('user')+"', '"+request.form.get('password')+"')"
		insert(sql)
		return render_template('login.html')

@app.route('/submit', methods=['GET','POST'])
def submsgs():
	msg = request.form.get('input')
	sql = "insert into c_blog(user_id, user_name, blog_content) values ('"+str(root[0])+"', '"+root[1]+"', '"+msg+"')"
	insert(sql)
	sql = "select * from c_blog"
	blogs = select(sql)
	return render_template('index.html', names=root[1], blogs=blogs)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.debug = True
	app.run(port = 4013)