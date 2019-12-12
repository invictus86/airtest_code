# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket
import sys

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
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


# power_off()
# sleep(3)
# power_on()
# sleep(5)

# for _ in range(5):
#     text("A2tmGHgGjYgV1MN4")
#     keyevent("{ENTER}")
#     sleep(1)
# time.sleep(5)

cmd1 = "set serverip 192.168.16.222; set ipaddr 192.168.16.157;"
cmd2 = "set bootdelay 1"
cmd3 = "set kernelargs coherent_pool=2m androidboot.console=ttyS0 "
cmd4 = "set memsize 512"
cmd5 = "setenv mtdparts 'mtdparts=ali_nand:8M@0M(boot),8M@8M(bootbak),2M@16M(bootenv),8M@18M(deviceinfo),8M@26M(bootmedia),8M@34M(see),16M@42M(kernel),8M@58M(ae),160M@66M(rootfs),8M@226M(upg_see),16M@234M(upg_kernel),60M@250M(upg_rootfs),3M@310M(serial),60M@313M(user)'"
cmd6 = "setenv sflashparts 'ali_sflash:2304k(nor_boot),128K(bootlogo),128K(nor_env),128k(VMXloader),512k(ca_data)'"
cmd7 = "set setfsiargs 'setenv bootargs init=/init androidboot.console=ttyS0 ${kernelargs} ${mtdparts}\;${sflashparts} root=/dev/mtdblock_robbs8 rootfstype=squashfs ro'"
cmd8 = "setenv sflashparts 'ali_sflash:2304k(nor_boot),128K(bootlogo),128K(nor_env),128k(ca_data)'"
cmd9 = "set fsibootcmd 'nand read 0x80007fc0 kernel 0x800000;bootm 0x80007fc0'"
cmd10 = "set fsiboot 'run setfsiargs;loadsee; run fsibootcmd'"
cmd11 = "set setssiargs 'setenv bootargs init=/init androidboot.console=ttyS0 ${kernelargs} ${mtdparts}\;${sflashparts} root=/dev/mtdblock_robbs11 rootfstype=squashfs ro'"
cmd12 = "set ssibootcmd 'nand read 0x80007fc0 upg_kernel 0x800000;bootm 0x80007fc0'"
cmd13 = "set ssiboot 'run setssiargs;loadupgsee;run ssibootcmd'"
cmd14 = "set bootcmd 'run ssiboot'"
cmd15 = "save"
cmd16 = "nand scrub.chip"
cmd17 = "tftp 0x80007fc0 deviceinfo.abs; nand erase deviceinfo 0x00100000; nand write 0x80007fc0 deviceinfo ${filesize}"
cmd18 = "tftp 0x80007fc0 ssi.bin;nand erase upg_rootfs 0x03c00000;nand write 0x80007fc0 upg_rootfs ${filesize}"
cmd19 = "tftp 0x80007fc0 ssi.uImage;nand erase upg_kernel 0x01000000;nand write 0x80007fc0 upg_kernel ${filesize}"
cmd20 = "tftp 0x80007fc0 sec_see_bin.ubo;nand erase upg_see 0x00800000;nand write 0x80007fc0 upg_see ${filesize}"
cmd21 = "tftp 0x80007fc0 sec_see_bin.ubo;nand erase see 0x00800000;nand write 0x80007fc0 see ${filesize}"
cmd22 = "reset"

list_cmd1 = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14, cmd15, cmd16]
# list_cmd2 = [cmd17, cmd18, cmd19, cmd20, cmd21, cmd22]

# list_cmd1 = [""]
# list_cmd1 = [cmd11]
time.sleep(3)
assert_exists(Template(r"../res/img/cmd18_success.png", threshold=0.9))
# for cmd in list_cmd1:
#     transfer_str = ""
#     for single_str in cmd:
#         if single_str == "{":
#             single_str = "{{}"
#         elif single_str == "}":
#             single_str = "{}}"
#         elif single_str == "(":
#             single_str = "{(}"
#         elif single_str == ")":
#             single_str = "{)}"
#         transfer_str = transfer_str + single_str
#     # print(transfer_str)
#
#     print(transfer_str.split(" "))
#     list_single_cmd = transfer_str.split(" ")
#     for single_cmd in list_single_cmd:
#         text(single_cmd)
#         print(single_cmd)
#         keyevent("{SPACE}")
#     keyevent("{ENTER}")
#     sleep(3.0)

# with open(r"E:\ivan_code\test_code\bad_block\bad_block.txt") as f:
#     cmd_list = f.readlines()
# #     print(cmd_list)
#
#
# for cmd in cmd_list:
#     print(cmd.split(" "))
#     list_single_cmd = cmd.split(" ")
#     for single_cmd in list_single_cmd:
#         text(single_cmd)
#         keyevent("{SPACE}")
#     keyevent("{ENTER}")
#     sleep(5.0)
