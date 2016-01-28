# PyGunner
A tool simplifying the process of sending mail with [Mailgun](https://www.mailgun.com/).

# Install
Clone the repo.

# Requirements
This tool requires python requests module.

`pip install requests` if it isn't already installed.

# Usage

To use the tool, add your details to the `config.json` file.

`cd PyGunner`

`sudo /bin/sh install.sh`

And simply run the script:  
`pygunner -s "Email Subject" -m "Email Message"`

# Example usecase
Add this to your server`/etc/ssh/sshrc` file

```
#!/bin/bash
IP=$(echo ${SSH_CONNECTION:-Unknown}|/usr/bin/cut -d " " -f 1)
MSG="User \"${USER:-[Unknown]}\" log in from ${IP:-[Unknown IP]}"
pygunner -s "SSH login to TheServer" -m "$MSG"
```

Whenever someone logs in via SSH you will receive a mail.
