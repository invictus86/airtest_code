# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import win32api, json
import ctypes
import logging
import socket
from ektlib import ekt_rds, ekt_dta, ekt_file, ekt_net
import file_operate

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='auto_burn.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///",
    ]
               )

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
    assert_exists(Template(r"../res/img/ATserver/atserver_data_not_found.png", threshold=0.9))
    touch(Template(r"../res/img/ATserver/atserver_confirm.png"))
except:
    assert_exists(Template(r"../res/img/ATserver/atserver_connect_success.png", threshold=0.9))
time.sleep(3)


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


def xshell_import_cmd(cmd):
    # transfer_str = ""
    print(cmd.split(" "))
    list_single_cmd = cmd.split(" ")
    sleep(0.5)
    for single_cmd in list_single_cmd:
        print(single_cmd)
        logging.info(single_cmd)
        text(single_cmd)
        keyevent("{SPACE}")
    keyevent("{ENTER}")
    sleep(1.5)


# script content
print("start...")


def v5_sys_init():
    """
    init the system,establish connect to the ATserver.
    :return: rds(EKTRds instance),doc(EktFileCfg instance),dta(EktDtDevice instance)
    """
    curretn_ip = get_local_ip()
    net = ekt_net.EktNetClient(curretn_ip, 8900)
    rds = ekt_rds.EktRds(net)
    dta = ekt_dta.EktDtDevice(net)
    doc = ekt_file.EktFileCfg(net)
    return rds, doc, dta


def v5_usb_init():
    """
    perform copy cd5 file from the computer to the usb,then switch the usb connect to the STB and reboot the STB
    :param cd5_file: str,the CD5 file name
    :return: rds,EktRds instance
    """
    rds, _, _ = v5_sys_init()
    src_file = r"D:\auto_burn_module\DSN5414a\UpgradeFile.bin"
    dst_file = r"F:\UpgradeFile.bin"
    print(src_file)
    logging.info(src_file)
    print(dst_file)
    logging.info(dst_file)

    rds.power_off()
    logging.info("rds.power_off()")
    time.sleep(2)
    rds.usb_switch_pc()
    logging.info("rds.usb_switch_pc()")
    time.sleep(8)
    file_operate.cope_file_src_dst(src_file, dst_file)
    logging.info("file_operate.cope_file_src_dst(src_file, dst_file)")
    time.sleep(6)
    rds.power_on()
    logging.info("rds.power_on()")
    time.sleep(1)
    rds.usb_switch_stb()
    logging.info("rds.usb_switch_stb()")
    return rds


def file_usb_before_enter_app(wait_time=0):
    """
    upgrade via USB before the STB can enter DVT APP
    :param filename:str,CD5 file name
    :param match_info: the texts to be matched
    :param wait_time: sleep time before start match
    :param timeout_secs: the time to match texts
    :return: None
    """
    rds = v5_usb_init()
    time.sleep(wait_time)
    rds.usb_switch_none()
    logging.info("rds.usb_switch_none()")
    return rds


double_click(Template(r"../res/img/DSN5414a/synergy.png", threshold=0.7))
time.sleep(1)
double_click(Template(r"../res/img/DSN5414a/upgrade.png", threshold=0.7))
time.sleep(2)
touch(Template(r"../res/img/DSN5414a/port_choose.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/port_com5.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/open.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/platform_choose.png"))
time.sleep(1)
# swipe(Template(r"../res/img/DSN5414a/platform_begin.png"), Template(r"../res/img/DSN5414a/platform_end.png"))
touch(Template(r"../res/img/DSN5414a/platform_end.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/nagra.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/add.png"))
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/browse.png"))

with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    str3 = load_dict.get("dsn5414a_browse_file_experimental")
    print(str3)
    logging.info(str3)

time.sleep(1)
xshell_import_cmd(str3)
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/startaddr.png"))
time.sleep(1)
xshell_import_cmd("0x0")
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/block_size.png"))
time.sleep(1)
# xshell_import_cmd("0x300000")
xshell_import_cmd("0x1000000")
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/start.png"))
time.sleep(500)
assert_exists(Template(r"../res/img/DSN5414a/burn_success.png"))
touch(Template(r"../res/img/DSN5414a/burn_success_ok.png"))

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
while True:
    rec_data = input("请确认断开板上飞线,连接USB线之后按a之后回车:")
    if rec_data == "a" or rec_data == "A":
        file_usb_before_enter_app(60)
        break
    else:
        print("非法输入")

while True:
    a = input("短接后按回车键(enter)    :烧录下一块板\r\n字母(q或者Q)之后按回车键 :退出\r\nplease input your choose:")
    if a == "":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        touch(Template(r"../res/img/DSN5414a/start.png"))
        time.sleep(500)
        assert_exists(Template(r"../res/img/DSN5414a/burn_success.png"))
        touch(Template(r"../res/img/DSN5414a/burn_success_ok.png"))
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        while True:
            rec_data = input("请确认断开板上飞线,连接USB线之后按a之后回车:")
            if rec_data == "a" or rec_data == "A":
                file_usb_before_enter_app(60)
                break
            else:
                print("非法输入")
    elif a == "q" or a == "Q":
        # touch(Template(r"../res/img/exit.png", threshold=0.5))
        os.system("taskkill /F /IM WinSTBUpgrader.exe")
        os.system("taskkill /F /IM LaunchPad.exe")
        os.system("taskkill /F /IM ATServer.exe")
        break
    else:
        print("非法输入")
