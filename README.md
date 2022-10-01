# 0x03. AirBnB clone - Deploy static
Install shellcheck version 0.3.3-1
sudo apt-get update
sudo apt-get install -y shellcheck=0.3.3


chmod +x test_script; ./test_script; shellcheck test_script

chmod +x purge-nginx; shellcheck purge-nginx

sudo apt install fabric

sudo apt-get install libssl-dev
sudo apt-get install build-essential
sudo apt-get install python3.4-dev
sudo apt-get install libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1


# Tasks
## 0. Prepare your web servers
Write a Bash script that sets up your web servers for the deployment of web_static.

```
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }

	error_page 404 /custom_404.html;
	location /custom_404.html {
		root /var/www/html;
		internal;
	}

	location /redirect_me {
		return 301 http://github.com/;
	}
```

chmod +x 0-setup_web_static.sh
shellcheck 0-setup_web_static.sh

### Web 01
./0-transfer_file purge-nginx 3.235.227.53 ubuntu ~/.ssh/school
ssh ubuntu@3.235.227.53 cat purge-nginx

ssh ubuntu@3.235.227.53 ./purge-nginx > /dev/null 2>&1
ssh ubuntu@3.235.227.53 nginx -V

./0-transfer_file 0-setup_web_static.sh 3.235.227.53 ubuntu ~/.ssh/school
ssh ubuntu@3.235.227.53 cat 0-setup_web_static.sh

ssh ubuntu@3.235.227.53 ./0-setup_web_static.sh > /dev/null 2>&1
ssh ubuntu@3.235.227.53 echo $?

#### Tests
ssh ubuntu@3.235.227.53 sudo ./0-setup_web_static.sh; echo $?

ssh ubuntu@3.235.227.53 service nginx status
ssh ubuntu@3.235.227.53 sudo nginx -t
ssh ubuntu@3.235.227.53 cat /etc/nginx/sites-enabled/default

ssh ubuntu@3.235.227.53 ls -l /data
ssh ubuntu@3.235.227.53 ls -l /data/web_static
ssh ubuntu@3.235.227.53 ls /data/web_static/current
ssh ubuntu@3.235.227.53 cat /data/web_static/current/index.html


curl 3.235.227.53/hbnb_static/index.html
curl -sI 3.235.227.53/redirect_me/
curl 3.235.227.53/xyz

### Web 02
./0-transfer_file purge-nginx 3.235.251.139 ubuntu ~/.ssh/school
ssh ubuntu@3.235.251.139 cat purge-nginx

ssh ubuntu@3.235.251.139 ./purge-nginx > /dev/null 2>&1
ssh ubuntu@3.235.251.139 nginx -V

./0-transfer_file 0-setup_web_static.sh 3.235.251.139 ubuntu ~/.ssh/school
ssh ubuntu@3.235.251.139 cat 0-setup_web_static.sh

ssh ubuntu@3.235.251.139 ./0-setup_web_static.sh > /dev/null 2>&1
ssh ubuntu@3.235.251.139 echo $?

ssh ubuntu@3.235.251.139 sudo ./0-setup_web_static.sh; echo $?

#### Tests
ssh ubuntu@3.235.251.139 service nginx status
ssh ubuntu@3.235.251.139 sudo nginx -t
ssh ubuntu@3.235.251.139 cat /etc/nginx/sites-enabled/default

ssh ubuntu@3.235.251.139 ls -l /data
ssh ubuntu@3.235.251.139 ls -l /data/web_static
ssh ubuntu@3.235.251.139 ls /data/web_static/current
ssh ubuntu@3.235.251.139 cat /data/web_static/current/index.html


curl 3.235.251.139/hbnb_static/index.html
curl -sI 3.235.251.139/redirect_me/
curl 3.235.251.139/xyz


## 1. Compress before sending
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

chmod +x 1-pack_web_static.py
pycodestyle 1-pack_web_static.py

fab -f 1-pack_web_static.py do_pack


## 2. Deploy archive!
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

chmod +x 2-do_deploy_web_static.py
pycodestyle 2-do_deploy_web_static.py


fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i ~/.ssh/school -u ubuntu


## 3. Full deployment
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:


chmod +x 3-deploy_web_static.py
pycodestyle 3-deploy_web_static.py


## 4. Keep it clean!
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:


chmod +x 100-clean_web_static.py
pycodestyle 100-clean_web_static.py

## 5. Puppet for setup
Redo the task #0 but by using Puppet:

chmod +x 101-setup_web_static.pp


# Unit Tests
## Test pep8 styles
Install pep8 module
```bash
pip install pep8
```

Import into test file and test a file
```python
import pep8

class test_City(test_basemodel):
    """
    Tests for City class instances.
    """

	def test_pep8(self):
		"""Check pep8 styling"""
		p = pep8.StyleGuide(quiet=True).check_files(["models/city.py"])
		self.assertEqual(p.total_errors, 0)
```

Run all unit tests
```bash
python3 -m unittest discover tests;
```
