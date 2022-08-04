# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket, win32api
import sys, os
import file_operate
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

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
while True:
    flash_type = input("1 :  nand flash\r\n"
                       "2 :  emmc flash\r\n"
                       "please input flash type: ")
    print("you choose flash type: {}".format(flash_type))
    if flash_type == "1" or flash_type == "2":
        break
    else:
        print("please input correct flash type")

while True:
    mac_address = input("example : 11:22:33:44:55:66\r\n"
                        "please input mac address: ")
    print("you choose mac_address: {}".format(mac_address))
    if len(mac_address) == 17:
        break
    else:
        print("please input correct mac address")

while True:
    sn = input("example : EKDIN4805MP00003\r\n"
               "please input sn: ")
    print("you choose sn: {}".format(sn))
    if len(sn) == 16:
        break
    else:
        print("please input correct sn")

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
rds.usb_switch_pc()
# 防止电脑启动U盘慢
try:
    time.sleep(5)
    filepath = "F:"
    file_operate.del_all_file(filepath)
except:
    time.sleep(5)
    filepath = "F:"
    file_operate.del_all_file(filepath)
file_operate.cope_floder_src_dst(r"D:\auto_burn_module\MTK_burn_script\write_serial", r"F:write_serial")

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

    xshell_import_cmd(["cd /mnt/hdd_1/write_serial/mtk/"])
    if flash_type == "1":
        xshell_import_cmd(["sh ./write_serial.sh {} {} ./hdcp_crc.bin ./ A11 nand".format(mac_address, sn)])
    elif flash_type == "2":
        xshell_import_cmd(["sh ./write_serial.sh {} {} ./hdcp_crc.bin ./ A11 emmc".format(mac_address, sn)])
    xshell_import_cmd(["hexdump -C /dev/mtd/serial"])


auto_xshell_input()
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

while True:
    a = input("please input your choose:")
    if a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        os.system("taskkill /F /IM Xshell.exe")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        break
