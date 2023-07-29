<?php
require 'vendor/autoload.php';
use Fluent\Logger\FluentLogger;
$logger = new FluentLogger("fluentd","24224");
$logger->post("debug.test",array("id"=>time(), 'content'=>'abc3', 'created_time'=>date('Y-m-d H:i:s')));
echo 'ok';