#!/usr/bin/env bash
#  Bash script that sets up web servers for the deployment of web_static

# Install nginx
sudo apt update
sudo apt install -y nginx

# Create default nginx folder for pages
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /var/www/html/

# Create index.html file and
sudo touch /data/web_static/releases/test/index.html

# Create index.html symbolic link
sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership to ubuntu and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Overwite file content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create custom_404.html file
sudo touch /var/www/html/custom_404.html

# Change file ownership to current user to allow editing
sudo chown -R "$USER":"$USER" /var/www/html/custom_404.html

# Overwite file content
echo "Ceci n'est pas une page" > /var/www/html/custom_404.html

# Setup custom http response header
sudo sed -i "s/listen \[::\]:80 default_server;/&\n\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/sites-enabled/default

# Custom error page
sudo sed -i "s/server_name _;/&\n\terror_page 404 \/custom_404.html;\n\tlocation \/custom_404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-enabled/default

# Redirection
sudo sed -i "s/server_name _;/&\n\tlocation \/redirect_me {\n\t\treturn 301 http:\/\/github.com\/;\n\t}\n/" /etc/nginx/sites-enabled/default

# Create an endpoint to index.html
sudo sed -i "s/server_name _;/&\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html;\n\t}\n/" /etc/nginx/sites-enabled/default

# Restart nginx server
sudo service nginx restart
