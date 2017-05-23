<?php
	session_start();
?>
<?php
include '../dbh.php';


$uid = $_POST['uid'];
$pwd = $_POST['pwd'];

$sql = "SELECT * FROM users WHERE uid='$uid' AND pwd='$pwd'";
$result = mysqli_query($conn, $sql);

if (!$row = mysqli_fetch_assoc($result)) {
	echo "Your username or password is incorrect!";
}
else {
	$_SESSION['id'] = $row['id']; 
	$_SESSION['uid'] = $row['uid'];
	$_SESSION['dispName'] = $row['displayName'];
	$_SESSION['desc'] = $row['userDesc'];
	$_SESSION['fName'] = $row['firstN'];
	$_SESSION['lName'] = $row['lastN'];
	$_SESSION['description'] = $row['userDesc'];
	$_SESSION['email'] = $row['email'];

}


header("Location: ../logintest.php");

?>