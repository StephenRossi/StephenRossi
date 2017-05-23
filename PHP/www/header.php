<!--login.php-->
<?php
	date_default_timezone_set("America/New_York");
	session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="style.css?v=6">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<title>Login Test</title>
</head>
<style type="text/css">
	
</style>
<body>

<header>
	<nav>
		<div><a href="logintest.php" id="headTitle">StephenRossi</a></div>
		<ul>
			<li>
				<a href="logintest.php">HOME</a>
			</li>

			<?php
			if (isset($_SESSION['uid'])) {  // if logged in do everything below
				echo "<form action='includes/logout.inc.php'>
					<button>Log-Out</button>
				</form>
				<li>
				<a href='profiles.php'>PROFILE</a>
				</li>";
			}
			else {
			    echo "<form  action='includes/login.inc.php' method='POST'>
					<input type='text' name='uid' placeholder='Username'>
					<input type='password' name='pwd' placeholder='Password'>
					<button type='submit'>Log-In</button>
				</form>
				<li>
				<a href='signuppage.php'>SIGN UP</a>
				</li>";
			}
			?>
		</ul>
	</nav>
</header>