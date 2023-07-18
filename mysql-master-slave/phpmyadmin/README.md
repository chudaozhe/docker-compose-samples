# Environment variables summary

- PMA_ARBITRARY - when set to 1 connection to the arbitrary server will be allowed
- PMA_HOST - define address/host name of the MySQL server
- PMA_VERBOSE - define verbose name of the MySQL server
- PMA_PORT - define port of the MySQL server
- PMA_HOSTS - define comma separated list of address/host names of the MySQL servers
- PMA_VERBOSES - define comma separated list of verbose names of the MySQL servers
- PMA_PORTS - define comma separated list of ports of the MySQL servers
- PMA_USER and PMA_PASSWORD - define username to use for config authentication method
- PMA_ABSOLUTE_URI - define user-facing URI
- HIDE_PHP_VERSION - if defined, will hide the php version (expose_php = Off). Set to any value (such as HIDE_PHP_VERSION=true).
- UPLOAD_LIMIT - if set, will override the default value for apache and php-fpm (default value is 2048 kb)
- PMA_CONFIG_BASE64 - if set, will override the default config.inc.php with the base64 decoded contents of the variable
- PMA_USER_CONFIG_BASE64 - if set, will override the default config.user.inc.php with the base64 decoded contents of the variable
