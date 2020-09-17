<?php

$address = file_get_contents("http://62.193.6.32:5000/?lat=35.722848&lon=51.346150");
//$address = file_get_contents("62.193.6.32:5000/?lat=35.722848&lon=51.346150");
//be careful, it doesnt work!
//u have to specify the protocol! (http,ftp, ....)
echo $address;
?>