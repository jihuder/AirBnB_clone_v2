#!/usr/bin/env bash
# sets up nginx web server and the host 
apt-get update
apt-get install nginx -y 
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo "Holberton School" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "40i \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
