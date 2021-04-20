#!"F:\\Python\\pythonw.exe"
print("Content-Type: text/html")    
print()
import cgi
form = cgi.FieldStorage()
ac=form.getvalue('ac')


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
							welcome to internet banking
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
                        
                            <div class="container-login100-form-btn">
                                <button class="login100-form-btn">
                                    <a href="balance.py?ac=%s" class="login100-form-btn">
                                       Balance    
                                    </a>
                                </button>
                            </div>
                            <div class="container-login100-form-btn">
                                    <button class="login100-form-btn">
                                        <a href="withdraw.py?ac=%s" class="login100-form-btn">
                                           Withdraw     
                                        </a>
                                    </button>
                                </div>
                            <div class="container-login100-form-btn">
                                <button class="login100-form-btn">
                                    <a href="deposit.py?ac=%s" class="login100-form-btn">
                                       Deposit     
                                    </a>
                                </button>
                            </div>
                            <div class="container-login100-form-btn">
                                <button class="login100-form-btn">
                                    <a href="statement.py?ac=%s" class="login100-form-btn">
                                       Statement     
                                    </a>
                                </button>
                            </div>
				</div>

				<form class="login100-form validate-form" action ="transfer1.py">
					<span class="login100-form-title">
						Transfer
                    </span>
                    <div>
                            &nbsp;&nbsp;&nbsp; Sender Account Number is :
                        </div>
					<div class="wrap-input100 validate-input" data-validate = "Account Number is required" >
                           
						<input class="input100" type="text" name="ac" placeholder="Account Number" value=%s >
						<span class="focus-input100"></span>
						<span class="symbol-input100">
							<i class="fa fa-user" aria-hidden="true"></i>
						</span>
					</div>
                        <div>
                         <div>
                            &nbsp;&nbsp;&nbsp; Receiver Account Number is :
                        </div>
					<div class="wrap-input100 validate-input" data-validate = "Account Number is required">
                           
						<input class="input100" type="text" name="ac1" placeholder="Account Number" >
						<span class="focus-input100"></span>
						<span class="symbol-input100">
							<i class="fa fa-user" aria-hidden="true"></i>
						</span>
					</div>
                        <div>
                            &nbsp;&nbsp;&nbsp; Transfer Amount :
                        </div>
					<div class="wrap-input100 validate-input" data-validate = "Enter Amount">
                  
                            <input class="input100" type="text" name="am" placeholder=" Transfer Amount">
                            <span class="focus-input100"></span>
                            <span class="symbol-input100">
                                <i class="fa fa-rupee" aria-hidden="true"></i>
                            </span>
                        </div>
                        <div class="container-login100-form-btn">
						<input type="submit" value="Transfer" class="login100-form-btn">
							
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
"""%(ac,ac,ac,ac,ac))
