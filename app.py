import sqlite3
import os
import uuid
import histsimilar
import time
import datetime
import random
import textreplace
import json
from flask import Flask, render_template,session, g,abort,flash, request, redirect, url_for, \
    send_from_directory,jsonify




app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = UPLOAD_FOLDER
path = r'testpic/TEST%d/%d.JPG'

DATABASE = 'sqldb.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
rootdir = 'F:\flask-file-upload-example-master\uploads' 
filename = "database/test.txt"
filename1 = "database/test1.txt"
filename2 = "database/test2.txt"
f1 = open("database/test1.txt")
fp=open('database/testtopic1.txt','w')
lii=histsimilar.data(filename)
#dict=[{'imgurl':'../uploads/6f7088b4.jpg','title':'1aaa'},{'imgurl':'../uploads/7bf7191e.jpg','title':'2bbb'},{'imgurl':'../uploads/4b721df0.jpg','title':'s9999'}]

app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def get_connection():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db
def get_conn(path):
   
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('s:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('n:[:memory:]')
        return sqlite3.connect(':memory:')

def get_cursor(conn):
    
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


def drop_table(conn, table):
    
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('[{}]!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def create_table(conn, sql):
   
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('[student]!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))



def close_all(conn, cu):
    
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()



def save(conn, sql, data):
    
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('sql:[{}],s:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchall(conn, sql):
    
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('sql:[{}]'.format(sql))
        cu.execute(sql)
        r=[dict(id=row[0],title=row[1],url=row[2],address=row[3])for row in cu.fetchall()]
        if len(r) > 0:
		     return r
            #for e in range(len(r)):
             #   print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql)) 

def fetchone(conn, sql, data):
    
    if sql is not None and sql != '':
        if data is not None:
            #Do this instead
            d = (data,) 
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('tsql:[{}],c:[{}]'.format(sql, data))
            cu.execute(sql, d)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] equal None!'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def update(conn, sql, data):
    
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('tsql:[{}],c:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def delete(conn, sql, data):
    
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('tsql:[{}],c:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def drop_table_test():
    
    print('ss...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)

def create_table_test():
   
    print('cs...')
    create_table_sql = '''CREATE TABLE `pic` (
                          `id` int(11) NOT NULL,
                          `title` varchar(20) NOT NULL,
                          `url` varchar(4) DEFAULT NULL,
                          `address` int(11) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)

def save_test():
    
    print('bs...')
    save_sql = '''INSERT INTO pic values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', '../uploads/6f7088b4.jpg', ''),
            (2, 'Tom', '../uploads/6f7088b4.jpg', ''),
            (3, 'Jake', '../uploads/6f7088b4.jpg', ''),
            (4, 'Cate', '../uploads/6f7088b4.jpg', '')]
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)

def fetchall_test():
   
    print('sd...')
    fetchall_sql = '''SELECT * FROM pic'''
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)

def fetchone_test():
   
    print('select a data from database...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = 1
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, data)

def update_test():
    
    print('update data...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)

def delete_test():
   
    print('delete data...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)


def init():
    
    global DB_FILE_PATH
    DB_FILE_PATH = 'F:\sqlite-shell-win32-x86-3090200\\sqldb.db'
   
    global TABLE_NAME
    TABLE_NAME = 'student'
    
    global SHOW_SQL
    SHOW_SQL = True
    print('show_sql : {}'.format(SHOW_SQL))
    
    drop_table_test()
   
    create_table_test()
   
    save_test()
    

def main():
    init()
	#delete_test()
    #fetchall_test()
    fetchall_test()
    print('#' * 50)
    fetchone_test()
    print('#' * 50)
    update_test()
    fetchall_test()
    print('#' * 50)
	#app = Flask(__name__)
   # delete_test()
   # fetchall_test()
def connect_db():
    return sqlite3.connect('F:\sqlite-shell-win32-x86-3090200\\sqldb.db')
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def generate_unique_filename(filename):
    return str(uuid.uuid4())[:8] + '.' + filename.rsplit('.', 1)[1]

def similar():
     #path = r'testpic/TEST%d/%d.JPG'
	for i in xrange(1, 10):
		print 'test_case_%d: %.3f%%'%(i, \
			histsimilar.calc_similar_by_path('testpic/TEST%d/%d.JPG'%(i, 1), 'testpic/TEST%d/%d.JPG'%(i, 2))*100)

def list():
    for root,dirs,files in os.walk(r'F:\\flask-file-upload-example-master\\uploads'):
        for file in files:
            print root + os.sep + file
			
def equals(dict):
    list="[{'imgurl':'"+dict[1]['imgurl']+"','title':'"+dict[1]['title']+"','name':'"+dict[1]['name']+"'}]"
    return eval(list)
def data(f1):
    #f = open("database/test.txt")
	dict=f1.read()
	#f.close()
	return eval(dict)

@app.route('/', methods=['GET', 'POST'])
def index():
   # histsimilar.data()
   #dict=data(f1)
    #histsimilar.list2('F:\\flask-file-upload-example-master\\uploads',histsimilar.data(filename))
    #similar()
    #dict=[{'imgurl':'../uploads/6f7088b4.jpg','title':'1aaa'},{'imgurl':'../uploads/7bf7191e.jpg','title':'2bbb'},{'imgurl':'../uploads/4b721df0.jpg','title':'s9999'}]
	#list()
    #init()
	#delete_test()
    #fetchall_test()
    #r=fetchall_test()
    if request.method == 'POST':
        file = request.files['file']
		#print lii.append({'imgurl':'','title':'','name':'12.jpg'})
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))+".jpg"))
            return render_template('index.html',dict=histsimilar.list2('F:\\flask-file-upload-example-master\\uploads'))
    return render_template('index.html',dict=histsimilar.data(filename))
@app.route('/uploadstext',methods=['POST', 'GET'])
def uploadtext():
    if request.method == 'POST':
        histsimilar.writecontentcount(request.form['content'])
	histsimilar.writelist()
	return render_template('editor.html',content1=open('database/testtopic1.txt').read(),content2=open('database/testtopic2.txt').read(),content3=open('database/testtopic3.txt').read(),content4=open('database/testtopic4.txt').read(),content5=open('database/testtopic5.txt').read(),content6=open('database/testtopic6.txt').read(),content7=open('database/testtopic7.txt').read(),content8=open('database/testtopic8.txt').read(),content9=open('database/testtopic9.txt').read())
@app.route('/jump', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        file = request.files['file']
		#print lii.append({'imgurl':'','title':'','name':'12.jpg'})
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))+".jpg"))
            return render_template('index.html',dict=histsimilar.list2('F:\\flask-file-upload-example-master\\uploads'))
@app.route('/direct',methods=['POST', 'GET'])
def derictfile():
	return render_template('editor.html',img_from_args=request.args.get('img'),content1=histsimilar.data0('database/test4.txt')[0]['text'],content2=histsimilar.data0('database/test4.txt')[1]['text'],content3=histsimilar.data0('database/test4.txt')[2]['text'],content4=histsimilar.data0('database/test4.txt')[3]['text'],content5=histsimilar.data0('database/test4.txt')[4]['text'],content6=histsimilar.data0('database/test4.txt')[5]['text'],content7=histsimilar.data0('database/test4.txt')[6]['text'],content8=histsimilar.data0('database/test4.txt')[7]['text'],content9=histsimilar.data0('database/test4.txt')[8]['text'])
@app.route('/right',methods=['POST', 'GET'])
def rights():
    return render_template('editor.html',data=json.dumps(histsimilar.addlistup(0)),img_from_args=request.args.get('img'),content1=histsimilar.data0('database/test4.txt')[0]['text'],content2=histsimilar.data0('database/test4.txt')[1]['text'],content3=histsimilar.data0('database/test4.txt')[2]['text'],content4=histsimilar.data0('database/test4.txt')[3]['text'],content5=histsimilar.data0('database/test4.txt')[4]['text'],content6=histsimilar.data0('database/test4.txt')[5]['text'],content7=histsimilar.data0('database/test4.txt')[6]['text'],content8=histsimilar.data0('database/test4.txt')[7]['text'],content9=histsimilar.data0('database/test4.txt')[8]['text'])
@app.route('/pagejump',methods=['POST', 'GET'])
def index2():
	return render_template('index.html',dict=histsimilar.data2(filename,request.args.get('page')))
@app.route('/_add_numbers',methods=['POST', 'GET'])
def add_numbers():
    textreplace.replace(open('database/test1.txt').readlines())
    return render_template('index.html',dict=histsimilar.data(filename))
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)