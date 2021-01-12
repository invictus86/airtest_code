# import win32api
# win32api.ShellExecute(0, 'open', r'D:\auto_burn_module\DTN7514I\WinGDB_v1.4.0\WinGDB_v1.4.0\WinGDB_v1.4.0.exe', '', '',
#                       1)

# from airtest.core.api import *
# from airtest.cli.parser import cli_setup
# import socket, win32api
# import sys, os
# import file_operate
# from ektlib import ekt_rds, ekt_net
# import ctypes
# def get_local_ip():
#     """
#     get local ip
#     :return:
#     """
#     addrs = socket.getaddrinfo(socket.gethostname(), None)
#     for item in addrs:
#         if str(item[-1][0])[0:3] == "192":
#             ip = str(item[-1][0])
#             print("current ip is : {}".format(ip))
#     return ip
#
#
# current_ip = get_local_ip()
# HOST = current_ip
# PORT = 8900
# BUFSIZ = 4096
# ADDR = (HOST, PORT)
#
# net = ekt_net.EktNetClient(current_ip, 8900)
# rds = ekt_rds.EktRds(net)
# rds.usb_switch_pc()

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import win32api, json
import ctypes
import logging

while True:
    a = input("直接回车键(enter)    :烧录下一块板\r\n字母(q或者Q)之后回车 :退出\r\nplease input your choose:")
    # a = input("please input your choose:")
    if a == "":
        print(111)
        # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        # touch(Template(r"../res/img/DSN5414a/start.png"))
        # time.sleep(500)
        # assert_exists(Template(r"../res/img/DSN5414a/burn_success.png"))
        # touch(Template(r"../res/img/DSN5414a/burn_success_ok.png"))
        # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    if a == "q" or a == "Q":
        # touch(Template(r"../res/img/exit.png", threshold=0.5))
        # os.system("taskkill /F /IM WinSTBUpgrader.exe")
        # os.system("taskkill /F /IM LaunchPad.exe")
        break
