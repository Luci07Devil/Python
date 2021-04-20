from sqlite3 import *
a=connect('bank.db')
#a.execute ('create table account (id integer  primary key AUTOINCREMENT,name varchar(60) unique,balance int,password varchar(50))')
#a.execute('insert into account (name,balance,password)values("hari","500","1212")')
#a.execute ('update account set balance=2000 where id=1')
a.commit()

def create():
    try:
        a.execute('insert into account (name,balance,password)values(?,"500",?)',(input("name"),input("password")))
        a.commit()
    except:
        print('name already exists')
def balance():
    try:
      id=int(input("id"))
    except:
        id=0
    name=(input('name'))
    pas=input('ur password')
    b=a.execute("select id,balance from account where (id=? or name=?) and password=?",(id,name,pas))
    z=0
    for z in b:
        print(z)
    if z==0:
        print('wrong id or name')
        
def withdrew():
    try:
        id=int(input("id"))
    except:
        id=0
    name=input("name")
    pas=input("password")
    b=a.execute("select id,balance,password from account where (id=? or name=?) and password=?",(id,name,pas))
    z=0
    for z in b:
        print(end="")
    if z!=0 and z[1]>=500:
        withd=int(input('withdraw amount'))
        if z[1]-withd>=500:
            y=z[1]-withd
            a.execute('update account set balance =? where id=? and password=?',(y,z[0],z[2]))
            a.commit()
        else:
            print('low balance')
    else:
        print('wrong login')
def deposit():
    try:
        id=int(input("id"))
    except:
        id=0
    name=input('name')
    b=a.execute("select id,balance,password from account where (id=? and name=?) ",(id,name))
    for z in b:
        print(end='')
    y=int(input('deposit'))
    y=y+z[1]
    a.execute('update account set balance =? where id=? or name=?',(y,id,name))
    a.commit()

        
b=a.execute("select * from account")
for z in b:
    print(z)

#create()
#balance()
#withdrew()
#deposit()
