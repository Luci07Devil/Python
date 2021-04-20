#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print() 
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=.;''login=sa;''password=1212;''Database=bank')
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('ac')
na=form.getvalue('c')
print("""
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Login V1</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
	
	<div class="limiter">
		<div class="container-login100">
				<div class="head-logo">
						<div>
						<img class="logo-img"  src="images/logo.png" alt="" ><br>
						<h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							welcome %s
						</h1>
						</div>	
					</div>
			<div class="wrap-login100">
					<button class="topright">
                            <a href="index.py" class="btn">
                               logout     
                            </a>
                        </button>
				<div class="login100-pic js-tilt" data-tilt>
					<img src="images/img-01.png" alt="IMG">
				</div>

				<form class="login100-form validate-form">
					<span class="login100-form-title">
						OPTIONS
					</span>

                    <div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="reset.py?ac=%s" class="login100-form-btn">
                               CHANGE PASSWORD     
                            </a>
						</button>
                    </div>




					<div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="withdraw.py?ac=%s&c=%s" class="login100-form-btn">
                               Withdraw     
                            </a>
						</button>
                    </div>
                    <div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="balance.py?ac=%s&c=%s" class="login100-form-btn">
                               Balance     
                            </a>
						</button>
                    </div>
                    <div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="deposit.py?ac=%s&c=%s" class="login100-form-btn">
                               Deposit    
                            </a>
						</button>
                    </div>
                    <div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="transfer.py?ac=%s&c=%s" class="login100-form-btn">
                               Transfer     
                            </a>
						</button>
                    </div>
                    <div class="container-login100-form-btn">
						<button class="login100-form-btn">
							<a href="statement.py?ac=%s&c=%s" class="login100-form-btn">
                               Statement     
                            </a>
						</button>
                    </div>
				</form>
			</div>
		</div>
	</div>
	
	

	
<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/tilt/tilt.jquery.min.js"></script>
	<script >
		$('.js-tilt').tilt({
			scale: 1.1
		})
	</script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>
"""%(na,ac,ac,na,ac,na,ac,na,ac,na,ac,na))
