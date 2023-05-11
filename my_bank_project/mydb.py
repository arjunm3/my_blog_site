import sqlite3
conn=sqlite3.connect('myproject.db')
c1=conn.cursor()
def createdb():
    c1.execute('create table if not exists login(user TEXT,password TEXT)')
def create_acc():
    c1.execute('create table if not exists accounts(account_no NUMERIC,account_name TEXT,account_type TEXT,balance NUMERIC)')
def add_det(a,b):
    c1.execute('insert into login values(?,?)',(a,b))
    conn.commit()
    c1.close()
    conn.close()
createdb()
create_acc()
