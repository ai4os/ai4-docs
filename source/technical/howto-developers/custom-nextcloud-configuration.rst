How to configure a custom Nextcloud
===================================

In order to link an account from a custom Nextcloud to the dashboard, you have to make sure that your Nextcloud allows requests from the different dashboard domains. This can be done in the Apache configuration file of your Nextcloud. 

Here is an example which shows such configuration including the regular expression that encloses all the different domains that must be able to make requests.

::

   <Directory "/var/www/nextcloud/">
     Options +FollowSymlinks
     AllowOverride All
     SetEnvIf Origin "^http(s)?://(.+\.)?(dev.ai4eosc\.eu|cloud.ai4eosc\.eu|dev.imagine-ai\.eu|cloud.imagine-ai\.eu))$" origin_is=$0
     <IfModule mod_headers.c>
       Header always set Strict-Transport-Security "max-age=15552000; includeSubdomains"
       Header always set Access-Control-Allow-Origin %{origin_is}e env=origin_is
       Header always set Access-Control-Allow-Credentials "true"
       Header always set Access-Control-Allow-Methods "PROPFIND"
       Header always set Access-Control-Allow-Headers "authorization,content-type"
     </IfModule>

     # Specific handling for OPTIONS requests
     <If "%{REQUEST_METHOD} == 'OPTIONS'">
       Header merge Access-Control-Allow-Origin %{origin_is}e env=PREFLIGHT_REQUEST_FROM_WEBSITE
       Header merge Access-Control-Allow-Methods "PROPFIND" env=PREFLIGHT_REQUEST_FROM_WEBSITE
       Header merge Access-Control-Allow-Headers "authorization,content-type" env=PREFLIGHT_REQUEST_FROM_WEBSITE
       Header merge Access-Control-Allow-Credentials "true" env=PREFLIGHT_REQUEST_FROM_WEBSITE
       # Respond with 204 No Content for OPTIONS requests
       # Note: This directive might not be respected depending on the server configuration and Apache version
       RewriteEngine On
       RewriteCond %{REQUEST_METHOD} OPTIONS
       RewriteRule .* - [R=204,L]
     </If>
  
     <IfModule mod_dav.c>
       Dav off
     </IfModule>

     SetEnv HOME /var/www/nextcloud
     SetEnv HTTP_HOME /var/www/nextcloud
   </Directory>
