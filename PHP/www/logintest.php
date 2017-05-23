<?php
	include 'header.php';
?>
<br> <br>
<br>
<?php

	#print_r($_SESSION);
$sql = "SELECT * FROM chat";

if (isset($_SESSION['uid']) and $_SESSION['id'] > 1) {  // if logged in do everything below
	#echo $_SESSION['id']; <-->both print the users ID
	//print_r($_SESSION); <-/-> More complex/from session
	echo "<div class='welcomeText'> Welcome ".$_SESSION['uid']."!</div><br>";
	echo "<div id='container'>
			<h1>".$_SESSION['uid']." is back! REJOICE!</h1>
			<div id='chatContain'>
				<div id='chatOut'>";       //INSERT/PRINT CHAT TABLE INFO HERE
					$serverName = 'localhost';
					$userName = 'root';
					$password = '';
					$dbname = 'logintest';

					$conn = new mysqli($serverName, $userName, $password, $dbname);
					if (!$conn) {
 	    				die("Connection failed: " . $conn->connect_error);
					}
					$sql = "SELECT userN, chatText, inputTime FROM chat";
					$result = $conn->query($sql);
					echo "<div id='chatConainer'>";
					while($row = $result->fetch_assoc()) {
    					echo "<div class='chatElement'>".$row["userN"]. ": " . $row["chatText"]. " <span>-" . $row["inputTime"]. "</span></div><br>";
					}
					echo "</div>";
					$conn->close();
				echo "</div>
				<form action='includes/chatAdd.inc.php' method='POST'>
					<input type='text' name='chatInp' placeholder='Whats on your mind ". $_SESSION['uid']."?'>
					<button id='chatIn'> Submit </button>
				</form>
			</div>
		</div>";

}
elseif(isset($_SESSION['uid']) and $_SESSION['id'] == 1) {
	echo "<div style='width: 100%; text-align: center;'>Lol admins are loosers<br><br><br>";	
	echo " This is the admin page but I dont want to set it up but It shows you the basic Idea </div>";

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
<script type="text/javascript">

</script>
</html>