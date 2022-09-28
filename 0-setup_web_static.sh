#!/usr/bin/env bash
#  Bash script that sets up web servers for the deployment of web_static

# Install nginx
sudo apt update
sudo apt install -y nginx

# Create default nginx folder for pages
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

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

# Create an endpoint to index.html
sudo sed -i "s/server_name _;/&\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex.html;\n\t}/" 

# Restart nginx server
sudo service nginx restart
