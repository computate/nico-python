
```bash
sudo yum install -y python36 python-virtualenv python-pip
sudo install -o $USER -g $USER -d /opt/nico-python-env
virtualenv -p python36 /opt/nico-python-env/
source /opt/nico-python-env/bin/activate
which python
sudo install -o $USER -g $USER -d /usr/local/src/nico
```
