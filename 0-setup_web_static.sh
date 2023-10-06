#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

echo "Hello World!" | sudo dd status=none of=/var/www/html/index.html

echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html > /dev/null

NEW_RULE="\\\n\tlocation /redirect_me {\n\t\t return 301 https://www.youtube.com/@tboy54321;\n\t}\n"

sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup

sudo sed -i "53i $NEW_RULE" /etc/nginx/sites-available/default

NEW_="\\\n\terror_page 404 /404.html;\n\n\tlocation /404.html {\n\t\tinternal;\n\t}\n"

sudo sed -i "53i $NEW_" /etc/nginx/sites-available/default

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
