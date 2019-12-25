# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket
import sys

if not cli_setup():
    auto_setup(__file__, logdir="./log/", devices=[
        #             "Windows:///524676",
        "Windows:///?title_re=localhost_serial*",
        #         "Windows:///?title_re=*Xshell",
    ])

# script content
print("start...")

HOST = '192.168.1.41'
PORT = 8900
BUFSIZ = 4096
ADDR = (HOST, PORT)


def power_on():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
    except Exception as e:
        print("连接服务器失败:", e)
        sys.exit(-1)
    data = ":RDS:POWER_ON\r\n"
    tcpCliSock.send(bytes(data, encoding='utf-8'))
    tcpCliSock.close()


def power_off():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
    except Exception as e:
        print("连接服务器失败:", e)
        sys.exit(-1)
    data = ":RDS:POWER_OFF\r\n"
    tcpCliSock.send(bytes(data, encoding='utf-8'))
    tcpCliSock.close()


power_off()
sleep(3)
power_on()
sleep(5)

for _ in range(10):
    text("^c")
    sleep(1)

with open(r"E:\ivan_code\test_code\auto_make_7414v_bad_block_file\bad_block.txt") as f:
    cmd_list = f.readlines()
#     print(cmd_list)


for cmd in cmd_list:
    print(cmd.split(" "))
    list_single_cmd = cmd.split(" ")
    for single_cmd in list_single_cmd:
        text(single_cmd)
        keyevent("{SPACE}")
    keyevent("{ENTER}")
    sleep(5.0)
