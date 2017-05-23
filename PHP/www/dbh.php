<?php 
//Database Handler

$conn = mysqli_connect("localhost", "root", "", "logintest");
                     // ServerName  username  pwd   db
if (!$conn) {
	die("Connection Failed: ".mysqli_connect_error());

	//ONLY use mysqli_connect_error() for testing!
    //When you release your site online you have to remove this function. Otherwise you are prone to SQL injection (hacking).
    //
    // 1547
}
?>