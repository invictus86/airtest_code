# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import socket, win32api
import sys, os
import file_operate
from ektlib import ekt_rds, ekt_net
import ctypes

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

os.system(r'explorer.exe /n, D:\auto_burn_module\DCD7015vALK\din7005')
time.sleep(1)
double_click(Template(r"../res/img/DCD7015v/tftpd32.png", threshold=0.9))

win32api.ShellExecute(0, 'open', r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Xmanager Enterprise 5\Xshell',
                      '', '', 1)
time.sleep(2)
# double_click(Template(r"../res/img/localhost.png"))

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        #             "Windows:///524676",
        "Windows:///?title_re=localhost_serial*",
        #         "Windows:///?title_re=*Xshell",
    ])

# script content
print("start...")


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
time.sleep(5)
filepath = "F:"
file_operate.del_all_file(filepath)
file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\all_fuse_tool\fuse_tool_vmx_v1.3",
                               r"F:fuse_tool_vmx_v1.3")
file_operate.cope_floder_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\images", r"F:images")

file_operate.cope_floder_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader", r"F:loader")

# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\bootenv.ubo", r"F:bootenv.ubo")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\deviceinfo.abs", r"F:deviceinfo.abs")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\erase_loader_data.bin", r"F:erase_loader_data.bin")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\fsi.bin", r"F:fsi.bin")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\product_sabbat_dual.abs", r"F:product_sabbat_dual.abs")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\see_bin.ubo", r"F:see_bin.ubo")
# file_operate.cope_file_src_dst(r"D:\auto_burn_module\DCD7015vALK\din7005\loader\vmlinux_signed_loader.bin",
#                                r"F:vmlinux_signed_loader.bin")

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
    sleep(5)


    for _ in range(10):
        text("A2tmGHgGjYgV1MN4")
        keyevent("{ENTER}")
        sleep(1)
    time.sleep(5)
    assert_exists(Template(r"../res/img/DCD7015v/boot_cmd.png", threshold=0.9))
    keyevent("{ENTER}")
    time.sleep(1)
    keyevent("{ENTER}")

    # cmd1 = "set serverip 192.168.16.222; set ipaddr 192.168.16.157;"

    cmd1 = "set ipaddr 192.168.1.199"
    cmd2 = "tftp {}:product_sabbat_dual.abs;".format(current_ip)
    cmd3 = "nor write 0x80007fc0 0 ${filesize};"
    cmd4 = "tftp {}:bootenv_test.bin;".format(current_ip)
    cmd5 = "nor write 0x80007fc0 0x00260000 0x20000;"
    cmd6 = "tftp {}:boot_logo.bin;".format(current_ip)
    cmd7 = "nor write 0x80007fc0 0x00240000 0x20000;"


    cmd8 = "tftp {}:deviceinfo.abs".format(current_ip)
    cmd9 = "nand erase deviceinfo 0x00080000"
    cmd10 = "nand write 0x80007fc0 deviceinfo 0x00080000"

    cmd11 = "tftp {}:fsi.bin".format(current_ip)
    cmd12 = "nand erase rootfs 0x09b80000"
    cmd13 = "nand write 0x80007fc0 rootfs 0x09b80000"

    cmd14 = "tftp {}:fsi.uImage".format(current_ip)
    cmd15 = "nand erase kernel 0x00a00000"
    cmd16 = "nand write 0x80007fc0 kernel 0x00a00000"

    cmd17 = "tftp {}:see_bin.ubo".format(current_ip)
    cmd18 = "nand erase see 0x00600000"
    cmd19 = "nand write 0x80007fc0 see 0x00600000"

    cmd20 = "set bootcmd 'run fsiboot'"
    cmd21 = "save"

    cmd22 = "cd /mnt/hdd_1"
    cmd23 = "./fuse_tool_vmx_v1.3"

    cmd24 = "flash_eraseall /dev/mtd/nor_boot"
    cmd25 = "dd if=/mnt/hdd_1/loader/product_sabbat_dual.abs of=/dev/mtd/nor_boot"
    cmd26 = "flash_eraseall /dev/mtd/nor_env"
    cmd27 = "dd if=/mnt/hdd_1/loader/bootenv.ubo of=/dev/mtd/nor_env"
    cmd28 = "flash_eraseall /dev/mtd/upg_rootfs"
    cmd29 = "nandwrite /dev/mtd/upg_rootfs -p /mnt/hdd_1/loader/fsi.bin"
    cmd30 = "flash_eraseall /dev/mtd/upg_kernel"
    cmd31 = "nandwrite /dev/mtd/upg_kernel -p /mnt/hdd_1/loader/vmlinux_signed_loader.bin"
    cmd32 = "flash_eraseall /dev/mtd/upg_see"
    cmd33 = "nandwrite /dev/mtd/upg_see -p /mnt/hdd_1/loader/see_bin.ubo"
    cmd34 = "flash_eraseall /dev/mtd/deviceinfo"
    cmd35 = "nandwrite /dev/mtd/deviceinfo -p /mnt/hdd_1/loader/deviceinfo.abs"

    cmd34_1 = "flash_eraseall /dev/mtd/fdt"
    cmd35_1 = "nandwrite /dev/mtd/fdt -p /mnt/hdd_1/loader/fdt.dtbo"

    cmd36 = "flash_eraseall /dev/mtd/loader_data"
    cmd37 = "dd if=/mnt/hdd_1/loader/erase_loader_data.bin of=/dev/mtd/loader_data"
    cmd38 = "flash_eraseall /dev/mtd/bootlogo"
    cmd39 = "dd if=/mnt/hdd_1/loader/logo_enriching.abs_GTD of=/dev/mtd/bootlogo"

    xshell_import_cmd([cmd1])
    time.sleep(1)
    xshell_import_cmd([cmd2])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    time.sleep(5)
    xshell_import_cmd([cmd3])
    time.sleep(15)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd4])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd5])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd6])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd7])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    time.sleep(1)

    power_off()
    sleep(3)
    power_on()
    # sleep(20)
    sleep(15)
    for _ in range(15):
        text("A2tmGHgGjYgV1MN4")
        keyevent("{ENTER}")
        sleep(1)
    time.sleep(5)
    assert_exists(Template(r"../res/img/DCD7015v/boot_cmd.png", threshold=0.9))
    # assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))

    xshell_import_cmd(["set ipaddr 192.168.2.143"])
    time.sleep(3)
    xshell_import_cmd([cmd8])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd9])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd10])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd11])
    time.sleep(18)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd12])
    time.sleep(5)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd13])
    time.sleep(40)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd14])
    time.sleep(15)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd15])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd16])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd17])
    time.sleep(5)
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd18])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd19])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd20])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))
    xshell_import_cmd([cmd21])
    assert_exists(Template(r"../res/img/DCD7015v/cmd20_success.png", threshold=0.9))

    power_off()
    sleep(3)
    power_on()
    sleep(20)
    sleep(30)
    # assert_exists(Template(r"../res/img/DCD7015v/cmd_testkit_success.png", threshold=0.9))
    keyevent("{ENTER}")
    time.sleep(1)
    keyevent("{ENTER}")
    xshell_import_cmd([cmd22])
    time.sleep(1)
    xshell_import_cmd([cmd23])
    text("1")
    keyevent("{ENTER}")
    time.sleep(1)
    assert_exists(Template(r"../res/img/enter1_success.png", threshold=0.9))
    text("2")
    keyevent("{ENTER}")
    time.sleep(1)
    text("0x35363031")
    keyevent("{ENTER}")
    time.sleep(1)
    text("3")
    keyevent("{ENTER}")
    time.sleep(1)
    text("4")
    keyevent("{ENTER}")
    time.sleep(1)
    text("5")
    keyevent("{ENTER}")
    time.sleep(1)
    text("0")
    keyevent("{ENTER}")
    time.sleep(3)

    xshell_import_cmd([cmd24])
    time.sleep(25)
    xshell_import_cmd([cmd25])
    time.sleep(30)
    xshell_import_cmd([cmd26])
    time.sleep(5)
    xshell_import_cmd([cmd27])
    time.sleep(5)
    xshell_import_cmd([cmd28])
    time.sleep(5)
    xshell_import_cmd([cmd29])
    time.sleep(10)
    xshell_import_cmd([cmd30])
    time.sleep(5)
    xshell_import_cmd([cmd31])
    time.sleep(10)
    xshell_import_cmd([cmd32])
    time.sleep(5)
    xshell_import_cmd([cmd33])
    time.sleep(5)
    xshell_import_cmd([cmd34])
    time.sleep(5)
    xshell_import_cmd([cmd35])
    time.sleep(5)

    xshell_import_cmd([cmd34_1])
    time.sleep(5)
    xshell_import_cmd([cmd35_1])
    time.sleep(5)

    xshell_import_cmd([cmd36])
    time.sleep(5)
    xshell_import_cmd([cmd37])
    time.sleep(5)
    xshell_import_cmd([cmd38])
    time.sleep(5)
    xshell_import_cmd([cmd39])
    time.sleep(5)

    power_off()
    sleep(3)
    power_on()
    time.sleep(25)


auto_xshell_input()
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

while True:
    a = input("please input your choose:")
    if a == "":
        time.sleep(3)
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        if not cli_setup():
            auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
                #             "Windows:///524676",
                "Windows:///?title_re=localhost_serial*",
                #         "Windows:///?title_re=*Xshell",
            ])
        auto_xshell_input()
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    elif a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        os.system("taskkill /F /IM tftpd32.exe")
        os.system("taskkill /F /IM Xshell.exe")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        break
