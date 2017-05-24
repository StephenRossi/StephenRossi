<?php
	session_start();
	echo $_SESSION['uid'];

	$first = $_POST['changeFName'];
	$last = $_POST['changeLName'];
	$dispN = $_POST['changeDisplayN'];
	$email = $_POST['setEmail'];
	$desc = $_POST['setDesc'];


	include '../dbh.php';

	$sql = "UPDATE users SET firstN='$first', lastN='$last', displayName='$dispN', email='$email', userDesc='$desc' WHERE uid='$_SESSION[uid]'";

	$result = mysqli_query($conn, $sql);

	$_SESSION['dispName'] = $dispN;
	$_SESSION['fName'] = $first;
	$_SESSION['lName'] = $last;
	$_SESSION['description'] = $desc;
	$_SESSION['email'] = $email;

	header("Location: ../profiles.php");
?>