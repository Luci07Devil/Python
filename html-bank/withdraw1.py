#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print()
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('account')
#ac="655580033"
def main():
    import pyodbc
    conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
    amount=int(form.getvalue('withdraw'))
    otp=form.getvalue('otp')
    otp1=form.getvalue('otp1')

    b=conn.execute('select balance,name from bank where accountno=?',(ac))
    for z in b:
        pass
    y=z[1]
   
    if otp==otp1:
        z=int(z[0])-int(amount)
        b=conn.execute('select top 1 id from statment order by id desc')
        for c in b:
            ke=int(c[0])
            ke=ke+1
        if(z>=500):
            conn.execute('update bank set balance=? where accountno=?',(z,ac))
            conn.execute('insert into statment (id,accountno,currentbalance,debalance)values (?,?,?,?)',(ke,ac,z,amount))
            conn.commit()
            conn.close()
            print("""
                    <html>
                <head>
                <title>Suresh Bank</title>
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
                </html>"""%(ac,y))
    
        else:
                print("""
                <html>
                <head>
                <title>Suresh Bank</title>
                <script>
                setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			
			alert('insuffcient balance')
			
		</script>
                </head>

                <body onload="setTimeout()">
                    
                </body>
                </html>"""%(ac,y))
    else:
           print("""
                <html>
                <head>
                <title>Suresh Bank</title>
                <script>
                setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			
			alert('wrong otp')
			
		</script>
                </head>

                <body onload="setTimeout()">
                    
                </body>
                </html>"""%(ac,y))


main()
