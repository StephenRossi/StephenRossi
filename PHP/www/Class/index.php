<!DOCTYPE html>
<html>
<head>
	<title>Students Table</title>
</head>
<body>

<form action="upload.php" method="POST">
	First Name: <input type="TEXT" name="FName" placeholder="Student's First Name"><br>
	Last Name: <input type="TEXT" name="LName" placeholder="Student's Last name"><br>
	Grade: <input type="TEXT" name="Age" placeholder="Student's Grade"><br>
	<input type="submit" name="go" value="Submit">
</form>
<br><br><br>
<form action="delete.php" method="POST">
	<input type="TEXT" name="id" placeholder="Users ID"><br>
	<input type="submit" name="go" value="Submit">
</form>
<?php
	$serverName = 'localhost';
	$userName = 'root';
	$password = '';
	$dbname = 'students';

	$conn = new mysqli($serverName, $userName, $password, $dbname);
	if (!$conn) {
 	   	die("Connection failed: " . $conn->connect_error);
	}
	$sql = "SELECT id, FName, LName, Grade FROM studentlist";
	$result = $conn->query($sql);
	echo "<br><br><table border='2'><tr><td>ID</td><td>First Name</td?><td>Last Name</td><td> Grade</td></tr>";

	while($row = $result->fetch_assoc()) {
    	echo "<tr><td>".$row["id"]."</td><td>".$row["FName"]. "</td> <td>" . $row["LName"]. " </td><td><span>" . $row["Grade"]. "</span></td></tr>";
		}
	echo "</table>";
	$conn->close();
?>
</body>
</html>