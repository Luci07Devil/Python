#!"F:\\Python\\pythonw.exe"
print("Content-Type:text/html")    
print()

import cgi
form=cgi.FieldStorage()
per=form.getvalue('am')
mya=form.getvalue('ac1')
ac=form.getvalue('ac')
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
def main():

    b=conn.execute('select balance from bank where accountno=?',(mya))
    for z in b:
        pass
    b=conn.execute('select balance,name from bank where accountno=?',(ac))
    for k in b:
        pass
    if z:
        pass
    c=k[1]
    ye=int(k[0])-int(per)
    if ye>=500:
        y=int(z[0])+int(per)
        j=int(k[0])-int(per)
        conn.execute('update bank set balance=? where accountno=?',(y,mya))
        conn.execute('update bank set balance=? where accountno=?',(j,ac))
        conn.commit()
        n=conn.execute('select top 1 id from statment order by id desc')
        for ce in n:
            ke=int(ce[0])
            ke=ke+1
        conn.execute('insert into statment (id,accountno,currentbalance,creditbalance)values (?,?,?,?)',(ke,mya,y,per))
        n=conn.execute('select top 1 id from statment order by id desc')
        for ce in n:
            ke=int(ce[0])
            ke=ke+1
        conn.execute('insert into statment (id,accountno,currentbalance,debalance)values (?,?,?,?)',(ke,ac,j,per))
        conn.commit()
        print("""
        <html>
        <head>
    
        <script>
        setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			alert('done')
		</script>
        </head>

        <body>

        </body>
        </html>"""%(ac,c))
    else:
        print("""
    <html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='transfer.py?ac=%s&c=%s'
			},0);
			alert('insuffcient balance')
		</script>
</head>

<body>

</body>
</html>"""%(ac,c))

try:
    main()
except:
    b=conn.execute('select balance,name from bank where accountno=?',(ac))
    for k in b:
        pass
    c=k[1]
    print("""
                <html>
                <head>
                <title>Suresh Bank</title>
                <script>
                setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			
			alert('Account no wrong')
			
		</script>
                </head>

                <body onload="setTimeout()">
                    
                </body>
                </html>"""%(ac,c))
