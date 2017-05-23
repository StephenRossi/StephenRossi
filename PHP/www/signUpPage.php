<?php
	include 'header.php';
?>
<?php
if (isset($_SESSION['id'])) {  // checks if logged in do everything below
	echo "<br><br><br><br><br><br><br><div class='welcomeText'> You already have an account/are already logged in! </div>";
}
else {
	echo "<br><br><br><br><br><br><form class='signUpInput' action='includes/signup.inc.php' method='POST'> 
		<input type=ext' name='first' placeholder='First Name'><br>
		<input type='text' name='last' placeholder='Last Name'><br>
		<input type='text' name='uid' placeholder='Username'><br>
		<input type='password' name='pwd' placeholder='Password'><br>
		<button type='submit'>Sign Up</button>
	</form>";  //if not do this
}
?>
<br>


</body>
</html>