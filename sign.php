

<html>
<body>

<?php
	define('DB_HOST', 'localhost');
	define('DB_NAME', 'user-details');	
	define('DB_USER','root');
	define('DB_PASSWORD','');
	
	$con=@mysql_connect(DB_HOST,DB_USER,DB_PASSWORD) or die("Failed to connect to MySQL: " . mysql_error()); 
	$db=mysql_select_db(DB_NAME,$con) or die("Failed to connect to MySQL: " . mysql_error()); 
	function NewUser() 
	{ 
	$firstname	= $_POST['fname'];
	$lastname	= $_POST['lname'];
	$dob  = $_POST['dob'];
	$contact = $_POST['phone'];
	$city  = $_POST['city'];
	$email = $_POST['username']; 
	$password = $_POST['password']; 
	$query = "INSERT INTO `userdetails` (`First name`,`Last name`,`DoB`,`Contact`,`City`,`email`,`password`) VALUES ('$firstname','$lastname','$dob','$contact','$city','$email','$password')"; 
	$data = mysql_query ($query)or die(mysql_error()); 
	

	if($data) 
	{ 
		 
		print "<h4 align='center' style='color : black;'>Registered!</h4>";
		include('C:\xampp\htdocs\web tech\myhome.html');
	} 
	} 
	function SignUp() 
	{ 
	if(!empty($_POST['username'])) //checking the 'user' name which is from Sign-Up.html, is it empty or have some text 
	{
			$query = mysql_query("SELECT * FROM userdetails WHERE email = '$_POST[username]' AND password = '$_POST[password]'") or die(mysql_error()); 
			if(!$row = mysql_fetch_array($query) or die(mysql_error())) 
			{ 
				newuser(); 
			} 
			else 
			{ 
				echo "SORRY...YOU ARE ALREADY REGISTERED USER..."; 
				include('login.html');
			} 
	} 
	} 
	if(isset($_POST['submit'])) 
	{ 
		SignUp(); 
	} 


?> 
</body>
</html>