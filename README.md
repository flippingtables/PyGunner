# PyGunner
A tool simplifying the process of sending mail with [Mailgun](https://www.mailgun.com/).

# Install
Clone the repo.

# Requirements
This tool requires python requests module.

`pip install requests` if it isn't already installed.

# Usage

To use the tool, add your details to the *config.json* file.

Then:
`chmod +x PyGunner.py`

Make a symbolic link of the Python script to your /usr/local/bin dir:

`sudo ln -s $HOME/bin/PyGunner/PyGunner.py /usr/local/bin/pygunner`

And simply run the script:
`./PyGunner -s "Email Subject" -m "Email Message"`