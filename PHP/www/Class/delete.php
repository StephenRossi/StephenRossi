<?php
$conn = mysqli_connect("localhost", "root", "", "students");
                     // ServerName  username  pwd   db
if (!$conn) {
	die("Connection Failed: ".mysqli_connect_error());
}
$id = $_POST['id'];
$sql = "DELETE FROM studentlist WHERE id='$id'";
$result = mysqli_query($conn, $sql);
	
header("Location: index.php");
?>