#!/usr/bin/python
__author__ = 'joannes'

import json
import requests
import argparse
import sys
import os

class PyGunner(object):

    def readConfig(self):
        try:
            currentPath = os.path.dirname(os.path.realpath(__file__))
            with open(currentPath+'/config.json', 'r') as data_file:
                data = json.load(data_file)
                return data
        except EnvironmentError:
            print("Config file not found. Quitting.")
            sys.exit(1)

    def __init__(self):
        config = self.readConfig()

        self.api_key = config["api_key"]
        self.sandbox = config["sandbox"]
        self.recipient = config["recipient"]
        self.sender = config["sender"]

    def sendMail(self, subject, message):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(self.sandbox)
        request = requests.post(request_url, auth=('api', self.api_key), data={
            'from': self.sender,
            'to': self.recipient,
            'subject': subject,
            'text': message
        })

    def run(self):
        parser = argparse.ArgumentParser(description='Send emails with Mailgun')
        parser.add_argument('-s', '--subject', dest='subject', type=str, help='Email Subject', required=True)
        parser.add_argument('-m', '--msg', dest='message', type=str, help='Email Message', required=True)
        args = parser.parse_args()

        self.sendMail(args.subject, args.message)
if __name__ == '__main__':
    PyGunner().run()
