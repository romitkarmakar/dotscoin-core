import sys
import time
from datetime import datetime
import socket
import threading
import requests
import json
host = '0.0.0.0'
port = 6500
INVALID_DATA=False

def get_nodes():
    base_url="http://dns.dotscoin.com/get_nodes/"
    nodes = requests.get(base_url)
    print(nodes)
    print(nodes.json()['nodes'])

udpsock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsock.bind((host,port))

def get_nodes():
    base_url="http://dns.dotscoin.com/get_nodes/"
    nodes = requests.get(base_url)
    print(nodes)
    print(nodes.json()['nodes'])

def broadcast(data,host,port):
    udpsock.sendto(data.encode('utf-8'),(host,port))