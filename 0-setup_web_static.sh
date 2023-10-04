#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
	sudo apt update
	sudon apt install -y nginx
fi

sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

sudo echo "<html>
  <head>
  <head/>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config=$(cat <<EOL
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOL
)

echo "$config" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo systemctl restart nginx
