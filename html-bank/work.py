#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print() 
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=.;''login=sa;''password=1212;''Database=bank')
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('cu')
na=form.getvalue('ne')
ne=form.getvalue('nep')
b=conn.execute("select * from bank  where password=?",(ac))
for c in b:
   pass
try:    
    if c[0]!=0:
        if na==ne:
            conn.execute('update bank set password=? where accountno=?',(na,c[1]))
            conn.commit()
            print("""
    <html>
    <head >
        <title>Suresh Bank</title>
    <script >
    setTimeout(function()
                    {
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			alert('changed succefully')
		</script>
    </head>
    
    <body>
    
    </body>
    </html>
    """ %(c[1],c[2]))
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
			alert('Wrong password')
		</script>
</head>

<body>

</body>
</html>
"""%(c[1],c[2]))

           
except Exception as e: 
           print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			alert('Wrong password')
		</script>
</head>

<body>

</body>
</html>
"""%(c[1],c[2]))

