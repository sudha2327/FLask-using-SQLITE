from sqlite3.dbapi2 import Row
from flask import *
import sqlite3 as sql

from werkzeug.exceptions import ExpectationFailed

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/save',methods=['POST','GET'])

def save():

    if request.method=='POST':
        try:
            name=request.form['name']
            email=request.form['em']
            address=request.form['address']

            print("name===>",name);
            print("email==>",email)
            print("address==>",address)

            with sql.connect('S:\coding\Flask\database.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO employee2 (name,email,address) values(?,?,?)",(name,email,address))
                con.commit()
                msg="added successfully"
        except:
            con.rollback()
            msg="cant insert"
        finally:
            return render_template('success.html',msg=msg)
            con.close()

@app.route('/view')

def view():
    con=sql.connect("S:\coding\Flask\database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT *FROM employee2")

    rows=cur.fetchall()
    return render_template('view.html',rows=rows)
    

        




if __name__=="__main__":
    app.run(debug=True)

