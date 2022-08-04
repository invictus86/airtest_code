# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket, win32api
import sys, os
from ektlib import ekt_rds, ekt_net
import ctypes
from file_operate import get_local_ip

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        # "Windows:///?title_re=HiTool-Hi3716MV450*",
        "Windows:///",
    ]
               )

# script content
print("start...")

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

double_click(Template(r"../res/img/ATserver/atserver_startup.png", threshold=0.9))
time.sleep(5)

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///?title_re=ATServer*",
        # "Windows:///",
    ]
               )

touch(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
time.sleep(5)
try:
    assert_exists(Template(r"../res/img/ATserver/atserver_connect_success.png", threshold=0.9))
except:
    # time.sleep(15)
    assert_exists(Template(r"../res/img/ATserver/atserver_data_not_found.png", threshold=0.9))
    touch(Template(r"../res/img/ATserver/atserver_confirm.png"))
time.sleep(3)

while True:
    is_ssi_correct = input("example : 1\r\n"
                           "flash_erase /dev/mtd/upg_kernel 0 0\r\n"
                           "nandwrite -p /dev/mtd/upg_kernel /mnt/hdd_1/ssi.uImage\r\n"
                           "flash_erase /dev/mtd/upg_rootfs 0 0\r\n"
                           "nandwrite -p /dev/mtd/upg_rootfs /mnt/hdd_1/ssi.bin\r\n"
                           "please input is ssi correct: ")
    print("you choose is_ssi_correct: {}".format(is_ssi_correct))
    if is_ssi_correct == "1":
        break
    else:
        print("please input correct is_ssi_correct")

win32api.ShellExecute(0, 'open', r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Xmanager Enterprise 5\Xshell',
                      '', '', 1)
# 防止五秒没打开xhsell
try:
    time.sleep(5)
    if not cli_setup():
        auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
            #             "Windows:///524676",
            "Windows:///?title_re=localhost_serial*",
            # "Windows:///?title_re=ATServer*",
            #         "Windows:///?title_re=*Xshell",
        ])
except:
    time.sleep(5)
    if not cli_setup():
        auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
            #             "Windows:///524676",
            "Windows:///?title_re=localhost_serial*",
            # "Windows:///?title_re=ATServer*",
            #         "Windows:///?title_re=*Xshell",
        ])

# script content
print("start...")

current_ip = get_local_ip()
HOST = current_ip
PORT = 8900
BUFSIZ = 4096
ADDR = (HOST, PORT)

net = ekt_net.EktNetClient(current_ip, 8900)
rds = ekt_rds.EktRds(net)

time.sleep(3)
rds.usb_switch_stb()
time.sleep(2)
del rds
del net


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


def xshell_import_cmd(list_cmd):
    for cmd in list_cmd:
        transfer_str = ""
        for single_str in cmd:
            if single_str == "{":
                single_str = "{{}"
            elif single_str == "}":
                single_str = "{}}"
            elif single_str == "(":
                single_str = "{(}"
            elif single_str == ")":
                single_str = "{)}"
            transfer_str = transfer_str + single_str
        print(transfer_str.split(" "))
        list_single_cmd = transfer_str.split(" ")
        sleep(0.5)
        for single_cmd in list_single_cmd:
            text(single_cmd)
            print(single_cmd)
            keyevent("{SPACE}")
        keyevent("{ENTER}")
        sleep(3.0)


def auto_xshell_input():
    power_off()
    sleep(3)
    power_on()
    sleep(30)

    xshell_import_cmd(["flash_erase /dev/mtd/upg_kernel 0 0"])
    time.sleep(10)
    xshell_import_cmd(["nandwrite -p /dev/mtd/upg_kernel /mnt/hdd_1/ssi.uImage"])
    time.sleep(10)
    xshell_import_cmd(["flash_erase /dev/mtd/upg_rootfs 0 0"])
    time.sleep(10)
    xshell_import_cmd(["nandwrite -p /dev/mtd/upg_rootfs /mnt/hdd_1/ssi.bin"])
    time.sleep(15)


auto_xshell_input()
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

while True:
    a = input("please input your choose:")
    if a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        os.system("taskkill /F /IM Xshell.exe")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        break
