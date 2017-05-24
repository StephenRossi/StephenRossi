<?php
	include 'header.php';
?>
<br> <br>
<br>
<?php
	include 'dbh.php';	

	#print_r($_SESSION);
$sql = "SELECT * FROM chat";

if (isset($_SESSION['uid'])) {  // if logged in do everything below
	#echo $_SESSION['id']; <-->both print the users ID
	//print_r($_SESSION); <-/-> More complex/from session
	echo "<div class='welcomeText'> Welcome ".$_SESSION['uid']."!</div><br>";
	echo "<div id='container'> <h1>Profile of ".$_SESSION['uid'].":</h1>";
	echo "<div id='profileContainer'>
		<div id='profileinfobox'>
			<form action='includes/saveProg.inc.php' method='POST'>
				<div id='profilePicDisplay'> insert Image here</div>
				<div class='profTitle'> Display Name: </div><input id='changeDisplayN' name='changeDisplayN' value='".$_SESSION['dispName']."'> </input>
				<div id='profUid'>@".$_SESSION['uid']." </div> <br>
				<div class='profTitle'> First Name: </div><input id='changeFName' name='changeFName' value='".$_SESSION['fName']."'> </input> <br>
				<div class='profTitle'> Last Name: </div><input id='changeLName' name='changeLName' value='".$_SESSION['lName']."'> </input> <br>
				<div class='profTitle'> Email: </div><input id='setEmail' name='setEmail' value='".$_SESSION['email']."'> </input> <br>
				<div class='profTitle'> Description: </div><input id='setDesc' name='setDesc' value='".$_SESSION['description']."'> </input> <br>
				<button> Save </button>
			</form>
		</div>
	</div>";


	
	echo "</div>";

}
else {
	echo "<div class='loggedIn'> You are not logged in! </div>";
	echo "<form class='signUpInput' action='includes/signup.inc.php' method='POST'> 
		<input type='text' name='first' placeholder='First Name'><br>
		<input type='text' name='last' placeholder='Last Name'><br>
		<input type='text' name='uid' placeholder='Username'><br>
		<input type='password' name='pwd' placeholder='Password'><br>
		<button type='submit'>Sign Up</button>
	</form>";   //if not do this
}
?>
</body>
</html>