
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

# Configure Red Hat CodeReady Studio

You can download Red Hat Code Ready Studio here: 

https://developers.redhat.com/products/codeready-studio/download

You will want to create a Red Hat account if you do not already have one. 

After you download CodeReady Studio, create a directory for it and install it with this command: 

```bash
install -d ~/.local/opt/codereadystudio
java -jar ~/Downloads/codereadystudio-*-installer-standalone.jar
```

You can use the default installation settings. I suggest to install CodeReady Studio in your in $HOME/.local/opt/codereadystudio

When you run CodeReady Studio, I suggest you create your workspace here: ~/.local/src

## Install these update sites: 

In CodeReady Studio, go to Help -> Install New Software...

Add these update sites and install these useful plugins: 

### Vrapper Vim Plugin
- http://vrapper.sourceforge.net/update-site/stable
    - Choose the "Vrapper" plugin if you want to be able to edit code with Vim commands
    - Vrapper keys to unbind in Window -> Preferences -> General -> Keys: 
        - ctrl+d, ctrl+u, ctrl+r, shift+ctrl+v, alt+v
    - Vrapper keys to set: 
        - and search for "Vrapper" and set the keys to alt+v

### DevStyle for dark theme

- http://www.genuitec.com/updates/devstyle/ci/
    - Choose "DevStyle Features" for themes

### YAML Editor

- http://www.genuitec.com/updates/devstyle/ci/
    - Choose "DevStyle Features" for themes

### Install this pydev update site in Codeready studio!
- https://www.pydev.org/updates
