<?php
	session_start();

include '../dbh.php';
date_default_timezone_set("America/New_York");

$chatInp = $_POST["chatInp"];
$user = $_SESSION['uid'];
$date = date("m/d/y");
$time = date("h:ia");

$sql = "INSERT INTO chat (chatText,inputDate ,inputTime, userN ) VALUES ('$chatInp', '$date', '$time','$user')";
$result = mysqli_query($conn, $sql);

header("Location: ../logintest.php");
//echo $chatInp;
//echo "<br>";
//echo $user;
//echo "<br>";
//echo $date;
//echo "<br>";
//echo $time;

?>