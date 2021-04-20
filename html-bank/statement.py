#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print() 
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
import cgi
form = cgi.FieldStorage()
name=form.getvalue('ac')
pas=form.getvalue('c')
b=conn.execute('exec sb ?',(name))



print("""
<html>
<head>
<style>
table,tr,td
{
border-collapse:collapse;
border-style:none;
text-align:right;
}
th
{
padding:40px;
position:relative;
left:-60px;
}
#a
{
position:relative;
left:300px;
top:80px;
}
#h
{
float:left;
}
#l
{
float:right;
}
</style>

</head>
<body>
<a href="account.py?ac=%s&c=%s" id="h"><button>Home</button></a>
<a href="index.py" id="l"><button>Logout</button></a>

<div id="a">

<table>
<tr>
<th>S.no</th>
<th>Acc_No</th>
<th>CurBal</th>
<th>Dr</th>
<th>Cr</th>
<th>DateTime</th>



</tr>

</div>
</body>
</html>

"""%(name,pas))

for c in b:
 print("""
<html>
<head>
<style>
table,tr,td
{
border-collapse:collapse;
border-style:none;
text-align:right;
}

td
{
padding:38px;


}
</style>
</head>
<body>
<table border="2">


<tr>

<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>

</tr>


</table>
</body>
</html>
    
"""%(c[0],c[1],c[2],c[3],c[4],c[5]))
