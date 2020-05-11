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

os.system(
    r'explorer.exe /n, D:\9215v\SSI.dsd9215v_master.2020.05.05.11\SSI.dsd9215v_master.2020.05.05.11\SSI.dsd9215v_master.2020.05.05.11')
time.sleep(1)
# win32api.ShellExecute(0, 'open', r'D:\flash_samples_7005\Flash samples\tftpd32.exe', '', '', 1)
double_click(Template(r"../res/img/9215v_xshell/9215v_tftp.png", threshold=0.9))

win32api.ShellExecute(0, 'open', r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Xmanager Enterprise 5\Xshell',
                      '', '', 1)
assert_exists(Template(r"../res/img/xshell_session.png", threshold=0.9))
time.sleep(1)
double_click(Template(r"../res/img/localhost.png"))

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

    for _ in range(10):
        text("A2tmGHgGjYgV1MN4")
        keyevent("{ENTER}")
        print("A2tmGHgGjYgV1MN4")
    assert_exists(Template(r"../res/img/9215v_xshell/fastboot_cmd.png", threshold=0.9))


    cmd1 = "setenv baudrate 115200"
    cmd2 = "setenv bootcmd 'run ssiboot'"
    cmd3 = "setenv bootdelay 1"
    cmd4 = "setenv ethact up"
    cmd5 = "setenv bootargs_512M 'mem=512M mmz=ddr,0,0,48M vmalloc=500M'"
    cmd6 = "setenv bootargs_1G 'mem=1G mmz=ddr,0,0,48M vmalloc=500M'"
    cmd7 = "setenv bootargs_2G 'mem=2G mmz=ddr,0,0,48M vmalloc=500M'"
    cmd8 = "setenv bootargs_768M 'mem=768M mmz=ddr,0,0,48M vmalloc=500M'"
    cmd9 = "setenv bootargs_1536M 'mem=1536M mmz=ddr,0,0,48M vmalloc=500M'"
    cmd10 = "setenv bootargs_3840M 'mem=3840M mmz=ddr,0,0,48M vmalloc=500M'"
    cmd11 = "setenv console 'ttyAMA0,115200'"
    cmd12 = "setenv ethaddr CC:B8:F1:72:07:7C"
    cmd13 = "setenv ipaddr 192.168.1.222"
    cmd14 = "setenv netmask 255.255.252.0"
    cmd15 = "setenv gatewayip 192.168.1.1"
    cmd16 = "setenv serverip {}".format(current_ip)
    cmd17 = "setenv loadaddr 0x1000000"
    cmd18 = "setenv mtdids 'nand0=hinand'"
    cmd19 = "setenv mtdparts 'mtdparts=hinand:8M(bootbak),4M(sbl),4M(sblbak),16M(trustedcore),16M(trustedcorebak),4M(baseparam),4M(pqparam),4M(logo),4M(deviceinfo),8M(bootmedia),16M(kernel),160M(rootfs),16M(upg_kernel),60M(upg_rootfs),8M(serial),60M(user),1M(fdt),-(others)'"
    cmd20 = "setenv sfcparts 'hi_sfc:1408K(fastboot),256K(bootenv),-(nvram)'"
    cmd21 = "setenv setssiargs 'setenv bootargs init=/init console=ttyAMA0,115200 ${mtdparts}\;${sfcparts} root=/dev/mtdblock_robbs16 rootfstype=squashfs ro'"
    cmd22 = "setenv ssiboot 'run setssiargs;run ssibootcmd'"
    cmd23 = "setenv ssibootcmd 'setenv notee y;nand read ${loadaddr} upg_kernel 0x1000000;bootm ${loadaddr}'"
    cmd24 = "setenv setfsiargs 'setenv bootargs init=/init console=ttyAMA0,115200 ${mtdparts}\;${sfcparts} root=/dev/mtdblock_robbs14 rootfstype=squashfs ro'"
    cmd25 = "setenv fsibootcmd 'loadteeos;nand read ${loadaddr} kernel 0x1000000;bootm ${loadaddr}'"
    cmd26 = "setenv fsiboot 'run setfsiargs;run fsibootcmd'"
    cmd27 = "setenv bootargs 'init=/init console=ttyAMA0,115200 mtdparts=hinand:8M(bootbak),4M(sbl),4M(sblbak),16M(trustedcore),16M(trustedcorebak),4M(baseparam),4M(pqparam),4M(logo),4M(deviceinfo),8M(bootmedia),16M(kernel),160M(rootfs),16M(upg_kernel),48M(upg_rootfs),8M(serial),60M(user),-(others);hi_sfc:1408k(fastboot),256K(bootenv),-(nvram) root=/dev/mtdblock_robbs14 rootfstype=squashfs ro'"
    cmd28 = "setenv panel_type gpio"
    cmd29 = "setenv ledconf '42 32 29 28 20 45 47'"
    cmd30 = "setenv stdin serial"
    cmd31 = "setenv stdout serial"
    cmd32 = "setenv stderr serial"
    cmd33 = "save"
    cmd34 = "sigenv"
    cmd35 = "tftp ssi.bin;nand erase upg_rootfs;nand write ${loadaddr} upg_rootfs 0x3C00000"
    cmd36 = "tftp ssi.uImage;nand erase upg_kernel;nand write ${loadaddr} upg_kernel 0x1000000"
    cmd37 = "tftp baseparam.img;nand erase baseparam;nand write ${loadaddr} baseparam 0x400000"
    cmd38 = "tftp pq_param.bin;nand erase pqparam;nand write ${loadaddr} pqparam 0x400000"
    cmd39 = "tftp logo.img;nand erase logo;nand write ${loadaddr} logo 0x400000"
    cmd40 = "tftp fdt.dtbo;nand erase fdt;nand write ${loadaddr} fdt 0x100000"
    cmd41 = "res"

    xshell_import_cmd([cmd1])
    time.sleep(3)
    keyevent("{ENTER}")
    list_cmd1 = [cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14, cmd15,
                 cmd16, cmd17, cmd18, cmd19, cmd20, cmd21, cmd22, cmd23, cmd24, cmd25, cmd26, cmd27, cmd28, cmd29,
                 cmd30, cmd31, cmd32, cmd33, cmd34]


    xshell_import_cmd(list_cmd1)

    xshell_import_cmd([cmd35])
    time.sleep(52)
    assert_exists(Template(r"../res/img/9215v_xshell/cmd35_success.png", threshold=0.9))
    xshell_import_cmd([cmd36])
    time.sleep(10)
    assert_exists(Template(r"../res/img/9215v_xshell/cmd36_success.png", threshold=0.9))
    xshell_import_cmd([cmd37])
    time.sleep(2)
    assert_exists(Template(r"../res/img/9215v_xshell/fastboot_cmd_xshell.png", threshold=0.9))
    xshell_import_cmd([cmd38])
    time.sleep(2)
    assert_exists(Template(r"../res/img/9215v_xshell/fastboot_cmd_xshell.png", threshold=0.9))
    xshell_import_cmd([cmd39])
    time.sleep(3)
    assert_exists(Template(r"../res/img/9215v_xshell/fastboot_cmd_xshell.png", threshold=0.9))
    xshell_import_cmd([cmd40])
    time.sleep(3)
    assert_exists(Template(r"../res/img/9215v_xshell/fastboot_cmd_xshell.png", threshold=0.9))
    xshell_import_cmd([cmd41])
    time.sleep(25)
    assert_exists(Template(r"../res/img/9215v_xshell/burn_ssi_success.png", threshold=0.9))



auto_xshell_input()
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

while True:
    a = input("please input your choose:")
    if a == "":
        auto_xshell_input()
    if a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        os.system("taskkill /F /IM tftpd32.exe")
        os.system("taskkill /F /IM Xshell.exe")
        # os.system("taskkill /F /IM explorer.exe")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        break
