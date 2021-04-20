#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print() 
import pyodbc
import smtplib
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('ac')
b=conn.execute('select emailid,password from bank where accountno=?',(ac))

for c in b:
    pass
try:
    if c:
        pass
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hariharanvimal@gmail.com", "hari@niit")
    msg=c[1]
    server.sendmail("hariharanvimal@gmail.com",c[0] , msg)
    print("""
    <html>
    <head>
    <title>Suresh Bank</title>
    <script>
    setTimeout(function()
		{
			window.location.href='index.py'
			},0);
			alert('password is sent to email')
    		</script>
    </head>

    <body>
    
    </body>
    </html>
    """)
except:
    print("""
    <html>
    <head>
    <title>Suresh Bank</title>
    <script>
    setTimeout(function()
		{
			window.location.href='reset1.py'
			},0);
			alert('wrong account')
    		</script>
    </head>

    <body>
    
    </body>
    </html>
    """)
    
