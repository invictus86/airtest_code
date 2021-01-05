# import win32api
# win32api.ShellExecute(0, 'open', r'D:\auto_burn_module\DTN7514I\WinGDB_v1.4.0\WinGDB_v1.4.0\WinGDB_v1.4.0.exe', '', '',
#                       1)

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket, win32api
import sys, os
import file_operate
from ektlib import ekt_rds, ekt_net
import ctypes
def get_local_ip():
    """
    get local ip
    :return:
    """
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for item in addrs:
        if str(item[-1][0])[0:3] == "192":
            ip = str(item[-1][0])
            print("current ip is : {}".format(ip))
    return ip


current_ip = get_local_ip()
HOST = current_ip
PORT = 8900
BUFSIZ = 4096
ADDR = (HOST, PORT)

net = ekt_net.EktNetClient(current_ip, 8900)
rds = ekt_rds.EktRds(net)
rds.usb_switch_pc()