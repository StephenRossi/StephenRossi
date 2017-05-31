<?php
$conn = mysqli_connect("localhost", "root", "", "students");
                     // ServerName  username  pwd   db
if (!$conn) {
	die("Connection Failed: ".mysqli_connect_error());
}

$first = $_POST['FName'];
$last = $_POST['LName'];
$grade = $_POST['Age'];

$sql = "INSERT INTO studentlist (FName, LName, Grade) VALUES ('$first', '$last', '$grade')";
$result = mysqli_query($conn, $sql);
	
header("Location: index.php");

?>