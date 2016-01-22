# Make PyGunner.py executable
chmod +x PyGunner.py

# Make a symlink to /usr/local/bin/, so that we can call the script from anywhere
ln -s `pwd`/PyGunner.py /usr/local/bin/pygunner
