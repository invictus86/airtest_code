import socket, time, sys, os
import ctypes

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

# import ekt_rds, ekt_dta, ekt_file, ekt_net
from ektlib import ekt_rds, ekt_dta, ekt_file, ekt_net
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import json
import win32api
import file_operate


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
    src_file = r"D:\7414\burn_file\1000\1000\UpgradeFile.bin"
    dst_file = r"F:\UpgradeFile.bin"
    print(src_file)
    print(dst_file)

    rds.power_off()
    time.sleep(2)
    rds.usb_switch_pc()
    time.sleep(8)
    file_operate.cope_file_src_dst(src_file, dst_file)
    time.sleep(6)
    rds.power_on()
    time.sleep(1)
    rds.usb_switch_stb()
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
    return rds


if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///",
    ]
               )

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

double_click(Template(r"../res/img/ATserver/atserver_startup.png", threshold=0.9))
# win32api.ShellExecute(0, 'open', r'D:\安装包\ATserver_contain_tsrate\ATServer.exe', '', '', 1)
time.sleep(5)

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///?title_re=ATServer*",
        # "Windows:///",
    ]
               )

# script content
print("start...")

touch(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
# double_click(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
time.sleep(20)
assert_exists(Template(r"../res/img/ATserver/atserver_data_not_found.png", threshold=0.9))
touch(Template(r"../res/img/ATserver/atserver_confirm.png"))
time.sleep(10)

file_usb_before_enter_app(wait_time=90)

while True:
    a = input("please input your choose:")
    if a == "":
        file_usb_before_enter_app(wait_time=120)
    if a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        break
