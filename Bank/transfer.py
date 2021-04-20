from bank import *
def transfer():
    id1=int(input("urid"))
    name1=input("urname")
    pas2=input("urpassword")
    b=a.execute("select id,balance,password from account where (id=? or name=?) and password=?",(id1,name1,pas2))
    z=0
    for z in b:
        print(end="")
    if z!=0:
        try:
            id=int(input("id"))
        except:
            id=0
        name=input('name')
        y=int(input('amount tobe transfer'))
        k=z[1]-y
        if  k>=0:
            print(k)
            b=a.execute("select id,balance,password from account where (id=? and name=?) ",(id,name))
            for r in b:
                print(end='')
            y=y+r[1]
            a.execute('update account set balance =? where id=? and name=?',(y,id,name))
            a.execute('update account set balance =? where id=? and name=?',(k,id1,name1))
            a.commit()
            print('done')
    
transfer()
