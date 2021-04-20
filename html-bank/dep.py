#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print()
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('ac')
amount=int(form.getvalue('am'))

b=conn.execute("select balance,name from bank where accountno=? ",(ac))
for c in b:
   pass
name1=int(amount)+int(c[0])
z=c[1]
b=conn.execute("update bank set balance=? where accountno=? ",(name1,ac))
n=conn.execute('select top 1 id from statment order by id desc')
for ce in n:
    ke=int(ce[0])
    ke=ke+1
conn.execute('insert into statment (id,accountno,currentbalance,creditbalance)values (?,?,?,?)',(ke,ac,name1,amount))
conn.commit()
conn.commit()
print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			alert('updated successfully')
		</script>
</head>

<body>

</body>
</html>
"""%(ac,z))
