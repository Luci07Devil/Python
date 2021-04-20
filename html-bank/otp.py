#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print()
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
import cgi
import random
try:
    form = cgi.FieldStorage()
    ac=form.getvalue('ac')
    k=form.getvalue('c')

    a=[x for x in range(10)]
    msg=''
    for k in range(4):
        msg=msg+str(random.choice(a))
    b=conn.execute("select emailid from bank  where accountno=?",(ac))
    for c in b:
       pass
    y=c[0]
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hariharanvimal@gmail.com", "hari@niit")
    server.sendmail("hariharanvimal@gmail.com",y , msg)

    print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='withdraw.py?ac=%s&c=%s&msg=%s'
			},0);
			alert('otp mailed to %s')
		</script>
</head>

<body>

</body>
</html>
""" %(ac,k,msg,y))
except:
    print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='withdraw.py?ac=%s&c=%s&msg=%s'
			},0);
			alert('unable to send otp try again')
		</script>
</head>

<body>

</body>
</html>
""" %(ac,k,msg))
