#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

if ! dpkg -l | grep -q nginx;
then
        apt-get -y update
        apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/


nginx="/etc/nginx/sites-enabled/default"
n_alias="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"

sed -i "/error_page 404 \\/404.html;/a\\$n_alias" "$nginx"

service nginx restart
