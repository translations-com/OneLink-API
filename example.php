<?php
if($argc<2){
    echo "\n usage: php getOTX.php content service\n";
    exit;
}

// Setup Defaults
$otx_account = 'otx,otxpass';
$otx_mimetype = "text/html";

// Fill from cli
$otx_content =                 $argv[1];
$otx_service = ( isset($argv[2])) ? $argv[2] : "smt";

// Setup data for http query 
$url = 'https://es-otx.onelink-poc.com/OneLinkOTX/';
$data = array(
                                'otx_account' => $otx_account
                                ,'otx_service' => $otx_service
                                ,'otx_mimetype' => $otx_mimetype
                                ,'otx_content' => $otx_content
                                                                
);
// Setup stream options
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data),
    ),
);

// Create stream , get contents 
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

// Results
echo "\n    content:" . $otx_content;
echo "\n translated:" . $result ."\n";
?>
