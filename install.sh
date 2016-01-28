# Make PyGunner.py executable
chmod +x PyGunner.py

# Copy the binary to /usr/local/bin/pygunner, and store the config file in /etc/pygunner/config.json
sudo cp PyGunner.py /usr/local/bin/pygunner
sudo mkdir /etc/pygunner
sudo cp config.json /etc/pygunner/config.json
