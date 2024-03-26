apt-get -y install git
apt-get -y install python3 python3-venv python3-dev
apt-get -y install postgresql nginx

python3 -m venv venv --system-site-packages
venv/bin/pip install -r requirements.txt
venv/bin/pip install -r requirements_production.txt

cp /tmp/production.py visapp/visapp/settings/

