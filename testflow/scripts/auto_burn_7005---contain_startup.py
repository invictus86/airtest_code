# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket, win32api
import sys

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        # "Windows:///?title_re=HiTool-Hi3716MV450*",
        "Windows:///",
    ]
               )



win32api.ShellExecute(0, 'open', r'D:\flash_samples_7005\Flash samples\tftpd32.exe', '', '', 1)
time.sleep(1)
win32api.ShellExecute(0, 'open', r'D:\安装包\ATserver_contain_tsrate\ATServer.exe', '', '', 1)
time.sleep(1)
assert_exists(Template(r"../res/img/atserver_ico.png", threshold=0.9))



win32api.ShellExecute(0, 'open', r'D:\Program Files (x86)\NetSarang\Xshell 6\Xshell.exe', '', '', 1)

assert_exists(Template(r"../res/img/xshell_session.png", threshold=0.9))
# time.sleep(10)
time.sleep(1)
double_click(Template(r"../res/img/localhost.png"))

# import win32gui, win32con
#
# hwnd = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

#
# if not cli_setup():
#     auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
#         #             "Windows:///524676",
#         "Windows:///?title_re=localhost_serial*",
#         #         "Windows:///?title_re=*Xshell",
#     ])
#
# # script content
# print("start...")
#
#
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
#
# def power_on():
#     tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         tcpCliSock.connect(ADDR)
#     except Exception as e:
#         print("连接服务器失败:", e)
#         sys.exit(-1)
#     data = ":RDS:POWER_ON\r\n"
#     tcpCliSock.send(bytes(data, encoding='utf-8'))
#     tcpCliSock.close()
#
#
# def power_off():
#     tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         tcpCliSock.connect(ADDR)
#     except Exception as e:
#         print("连接服务器失败:", e)
#         sys.exit(-1)
#     data = ":RDS:POWER_OFF\r\n"
#     tcpCliSock.send(bytes(data, encoding='utf-8'))
#     tcpCliSock.close()
#
#
# def xshell_import_cmd(list_cmd):
#     for cmd in list_cmd:
#         transfer_str = ""
#         for single_str in cmd:
#             if single_str == "{":
#                 single_str = "{{}"
#             elif single_str == "}":
#                 single_str = "{}}"
#             elif single_str == "(":
#                 single_str = "{(}"
#             elif single_str == ")":
#                 single_str = "{)}"
#             transfer_str = transfer_str + single_str
#         print(transfer_str.split(" "))
#         list_single_cmd = transfer_str.split(" ")
#         sleep(0.5)
#         for single_cmd in list_single_cmd:
#             text(single_cmd)
#             print(single_cmd)
#             keyevent("{SPACE}")
#         keyevent("{ENTER}")
#         sleep(3.0)
#
#
# power_off()
# sleep(3)
# power_on()
# sleep(5)
#
# for _ in range(5):
#     text("A2tmGHgGjYgV1MN4")
#     keyevent("{ENTER}")
#     sleep(1)
# time.sleep(5)
# assert_exists(Template(r"../res/img/cmd_begin.png", threshold=0.9))
#
# # cmd1 = "set serverip 192.168.16.222; set ipaddr 192.168.16.157;"
# cmd1 = "set serverip {}; set ipaddr 192.168.1.157;".format(current_ip)
# cmd2 = "set bootdelay 1"
# cmd3 = "set kernelargs coherent_pool=2m androidboot.console=ttyS0 "
# cmd4 = "set memsize 512"
# cmd5 = "setenv mtdparts 'mtdparts=ali_nand:8M@0M(boot),8M@8M(bootbak),2M@16M(bootenv),8M@18M(deviceinfo),8M@26M(bootmedia),8M@34M(see),16M@42M(kernel),8M@58M(ae),160M@66M(rootfs),8M@226M(upg_see),16M@234M(upg_kernel),60M@250M(upg_rootfs),3M@310M(serial),60M@313M(user)'"
# cmd6 = "setenv sflashparts 'ali_sflash:2304k(nor_boot),128K(bootlogo),128K(nor_env),128k(VMXloader),512k(ca_data)'"
# cmd7 = r"set setfsiargs 'setenv bootargs init=/init androidboot.console=ttyS0 ${kernelargs} ${mtdparts}\;${sflashparts} root=/dev/mtdblock_robbs8 rootfstype=squashfs ro'"
# cmd8 = "setenv sflashparts 'ali_sflash:2304k(nor_boot),128K(bootlogo),128K(nor_env),128k(ca_data)'"
# cmd9 = "set fsibootcmd 'nand read 0x80007fc0 kernel 0x800000;bootm 0x80007fc0'"
# cmd10 = "set fsiboot 'run setfsiargs;loadsee; run fsibootcmd'"
# cmd11 = "set setssiargs 'setenv bootargs init=/init androidboot.console=ttyS0 ${kernelargs} ${mtdparts}\;${sflashparts} root=/dev/mtdblock_robbs11 rootfstype=squashfs ro'"
# cmd12 = "set ssibootcmd 'nand read 0x80007fc0 upg_kernel 0x800000;bootm 0x80007fc0'"
# cmd13 = "set ssiboot 'run setssiargs;loadupgsee;run ssibootcmd'"
# cmd14 = "set bootcmd 'run ssiboot'"
# cmd15 = "save"
# cmd16 = "nand scrub.chip"
# cmd17 = "tftp 0x80007fc0 deviceinfo.abs; nand erase deviceinfo 0x00100000; nand write 0x80007fc0 deviceinfo ${filesize}"
# cmd18 = "tftp 0x80007fc0 ssi.bin;nand erase upg_rootfs 0x03c00000;nand write 0x80007fc0 upg_rootfs ${filesize}"
# cmd19 = "tftp 0x80007fc0 ssi.uImage;nand erase upg_kernel 0x01000000;nand write 0x80007fc0 upg_kernel ${filesize}"
# cmd20 = "tftp 0x80007fc0 sec_see_bin.ubo;nand erase upg_see 0x00800000;nand write 0x80007fc0 upg_see ${filesize}"
# cmd21 = "tftp 0x80007fc0 sec_see_bin.ubo;nand erase see 0x00800000;nand write 0x80007fc0 see ${filesize}"
# cmd22 = "reset"
# cmd23 = "cd /mnt/hdd_1"
# cmd24 = "flash_eraseall /dev/mtd14"
# cmd25 = "dd if=/mnt/hdd_1/product_sabbat_dual.abs of=/dev/mtd14"
# cmd26 = "./hdcp_wr_wpkey"
# cmd27 = "./fuse_tool_vmx_v1.3"
#
# list_cmd1 = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14]
# list_cmd2 = [cmd15]
# list_cmd3 = [cmd16]
# list_cmd4 = [cmd17, cmd18, cmd19, cmd20, cmd21]
#
# xshell_import_cmd(list_cmd1)
# xshell_import_cmd(list_cmd2)
# assert_exists(Template(r"../res/img/done.png", threshold=0.9))
# xshell_import_cmd(list_cmd3)
# assert_exists(Template(r"../res/img/cmd15_confirm.png", threshold=0.9))
# text("y")
# keyevent("{ENTER}")
# time.sleep(5)
# assert_exists(Template(r"../res/img/ok.png", threshold=0.9))
# xshell_import_cmd([cmd17])
# assert_exists(Template(r"../res/img/cmd17_success.png", threshold=0.9))
# xshell_import_cmd([cmd18])
# time.sleep(40)
# assert_exists(Template(r"../res/img/cmd18_success.png", threshold=0.9))
# xshell_import_cmd([cmd19])
# time.sleep(15)
# assert_exists(Template(r"../res/img/cmd19_success.png", threshold=0.9))
# xshell_import_cmd([cmd20])
# time.sleep(6)
# assert_exists(Template(r"../res/img/cmd20_success.png", threshold=0.9))
# xshell_import_cmd([cmd21])
# time.sleep(6)
# assert_exists(Template(r"../res/img/cmd21_success.png", threshold=0.9))
# xshell_import_cmd([cmd22])
# time.sleep(25)
# assert_exists(Template(r"../res/img/cmd22_success.png", threshold=0.9))
# xshell_import_cmd([cmd23])
# assert_exists(Template(r"../res/img/cmd23_success.png", threshold=0.9))
# xshell_import_cmd([cmd24])
# time.sleep(8)
# assert_exists(Template(r"../res/img/cmd24_success.png", threshold=0.9))
# xshell_import_cmd([cmd25])
# time.sleep(20)
# assert_exists(Template(r"../res/img/cmd25_success.png", threshold=0.9))
# xshell_import_cmd([cmd26])
# assert_exists(Template(r"../res/img/cmd26_success.png", threshold=0.9))
# xshell_import_cmd([cmd27])
# assert_exists(Template(r"../res/img/cmd27_success.png", threshold=0.9))
#
# text("1")
# keyevent("{ENTER}")
# time.sleep(1)
# assert_exists(Template(r"../res/img/enter1_success.png", threshold=0.9))
# text("2")
# keyevent("{ENTER}")
# time.sleep(1)
# text("0x35363031")
# keyevent("{ENTER}")
# time.sleep(1)
# text("3")
# keyevent("{ENTER}")
# time.sleep(1)
# text("4")
# keyevent("{ENTER}")
# time.sleep(1)
# text("5")
# keyevent("{ENTER}")
# time.sleep(1)
# text("0")
# keyevent("{ENTER}")
# time.sleep(1)
# assert_exists(Template(r"../res/img/cmd23_success.png", threshold=0.9))
#
# sleep(3)
# power_off()
# sleep(3)
# power_on()
# time.sleep(25)
# assert_exists(Template(r"../res/img/auto_burn_7005_success.png", threshold=0.9))
