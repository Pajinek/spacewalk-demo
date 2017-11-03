#!/usr/bin/python

import sys
try:
    import xmlrpclib
except:
    import xmlrpc.client as xmlrpclib


def create_channel(channel_label):
    SATELLITE_URL = "http://demo.spacewalk.cloud/rpc/api"
    SATELLITE_LOGIN = "username"
    SATELLITE_PASSWORD = "password"

    client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
    key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)

    client.channel.software.create(key,
        channel_label, # label
        channel_label, # name
        'channel summary', # summary
        'channel-x86_64', # arch
        'fedora26-x86_64', # parent channel label
        'sha1' # checksum
    )

if __name__ == "__main__":
    create_channel(sys.argv[1])
