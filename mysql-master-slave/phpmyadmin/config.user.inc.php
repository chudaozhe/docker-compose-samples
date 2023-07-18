<?php
/* vim: set expandtab sw=4 ts=4 sts=4: */
$config = [
    [
        'verbose' => 'local-master',
        "host" => "docker-mysql-master",
        "user" => "root",
        "password" => "",
        "port" => "3306",
    ],
    [
        'verbose' => 'local-slave',
        "host" => "docker-mysql-slave",
        "user" => "root",
        "password" => "",
        "port" => "3306",
    ],
];
/* Servers configuration */
foreach ($config as $key => $conf) {
    $i = $key + 1; //注意 索引从1开始
    $cfg['Servers'][$i]['verbose'] = $conf['verbose'];
    $cfg['Servers'][$i]['host'] = $conf['host'];
    $cfg['Servers'][$i]['port'] = $conf['port'];
    $cfg['Servers'][$i]['socket'] = '';
    $cfg['Servers'][$i]['connect_type'] = 'tcp';
    $cfg['Servers'][$i]['extension'] = 'mysqli';
    $cfg['Servers'][$i]['auth_type'] = 'config';
    $cfg['Servers'][$i]['user'] = $conf['user'];
    $cfg['Servers'][$i]['password'] = $conf['password'];
    $cfg['Servers'][$i]['AllowNoPassword'] = true;

    $cfg['Servers'][$i]['bs_garbage_threshold'] = 50;
    $cfg['Servers'][$i]['bs_repository_threshold'] = '32M';
    $cfg['Servers'][$i]['bs_temp_blob_timeout'] = 600;
    $cfg['Servers'][$i]['bs_temp_log_threshold'] = '32M';
}
/* End of servers configuration */

$cfg['DefaultLang'] = 'en-utf-8';
$cfg['ServerDefault'] = 1;
$cfg['UploadDir'] = '';
$cfg['SaveDir'] = '';
$cfg['MaxNavigationItems'] = 100; //超过100个表再分页

