
```bash
pkcon install -y python3
pkcon install -y python3-virtualenv
pkcon install -y python3-pip
install -d ~/.local/opt/nico-python-env
virtualenv -p python3 ~/.local/opt/nico-python-env/
source ~/.local/opt/nico-python-env/bin/activate
which python
install -d ~/.local/src/nico-python
git clone git@github.com:computate/nico-python.git ~/.local/src/nico-python
```
