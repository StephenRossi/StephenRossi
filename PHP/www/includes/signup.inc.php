<?php
	session_start();
?>
<?php
include '../dbh.php';

$first = $_POST['first'];
$last = $_POST['last'];
$uid = $_POST['uid'];
$pwd = $_POST['pwd'];
$dispN = $_POST['uid'];
$userDescD = "";
$userDescD = mysqli_real_escape_string($userDescD);
$email= "";
$email = mysqli_real_escape_string($email);

$sql = "INSERT INTO users (firstN, lastN, uid, pwd, displayName, userDesc, email) VALUES ('$first', '$last', '$uid', '$pwd', '$dispN', '$userDescD', '$email')";
$result = mysqli_query($conn, $sql);
	
header("Location: ../logintest.php");

//echo $first."<br>";
//echo $last."<br>";
//echo $uid."<br>";          // To test and make sure it is working
//echo $pwd."<br>";

?>