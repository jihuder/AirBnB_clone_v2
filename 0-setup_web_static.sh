#!/usr/bin/env bash
# sets up nginx web server and the host
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
echo "<h1>Holberton School</h1>" > ~/index.html
sudo cp ~/index.html /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/index.html  /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "40i \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
