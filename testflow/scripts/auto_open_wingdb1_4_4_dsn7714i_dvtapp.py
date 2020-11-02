# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import json
import win32api
import ctypes
import logging
import socket
from airtest.core.settings import Settings
from ektlib import ekt_rds, ekt_dta, ekt_file, ekt_net
import file_operate

Settings.FIND_TIMEOUT = 60

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
        # "Windows:///?title_re=HiTool-Hi3716MV450*",
        "Windows:///",
    ]
               )

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
# script content
print("start...")

double_click(Template(r"../res/img/ATserver/atserver_startup.png", threshold=0.9))
time.sleep(5)
touch(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
time.sleep(5)
try:
    assert_exists(Template(r"../res/img/ATserver/atserver_connect_success.png", threshold=0.9))
except:
    # time.sleep(15)
    assert_exists(Template(r"../res/img/ATserver/atserver_data_not_found.png", threshold=0.9))
    touch(Template(r"../res/img/ATserver/atserver_confirm.png"))

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


def xshell_import_cmd(cmd):
    # transfer_str = ""
    print(cmd.split(" "))
    list_single_cmd = cmd.split(" ")
    sleep(0.5)
    for single_cmd in list_single_cmd:
        print(single_cmd)
        text(single_cmd)
        keyevent("{SPACE}")
    keyevent("{ENTER}")
    sleep(1.5)


def clean_key():
    """
    upgrade EKCleanSPCBKey.CD5 set the STB to default value.
    :return: None
    """
    rds, _, _ = v5_sys_init()
    rds.power_off()
    time.sleep(1)
    rds.power_on()
    time.sleep(3)
    src_file = r"D:\auto_burn_module\DSN7714i\CH05101459_B3_DSN7714i_IRDETO_SIGNED_bootloader_IMAGE_V5.1.2\update\clean\EKCleanSPCBKey.CD5"
    print(src_file)
    dst_file = r"F:\EKCleanSPCBKey.CD5"
    print(dst_file)
    del_file = r"F:\IRDETO_0238_0037.CD5"
    rds.usb_switch_pc()
    time.sleep(8)
    file_operate.remove_file(del_file)
    filepath = "F:"
    file_operate.del_all_file(filepath)
    time.sleep(5)
    file_operate.cope_file_src_dst(src_file, dst_file)
    time.sleep(6)
    rds.power_off()
    time.sleep(1)
    rds.power_on()
    time.sleep(1)
    rds.usb_switch_stb()
    time.sleep(10)
    try:
        time.sleep(10)
    finally:
        rds.usb_switch_pc()
        time.sleep(5)
        file_operate.remove_file(dst_file)
        rds.usb_switch_none()
        time.sleep(10)


def v5_usb_init(cd5_file):
    """
    perform copy cd5 file from the computer to the usb,then switch the usb connect to the STB and reboot the STB
    :param cd5_file: str,the CD5 file name
    :return: rds,EktRds instance
    """
    rds, _, _ = v5_sys_init()
    src_file = r"D:\auto_burn_module\DSN7714i\CH05101459_B3_DSN7714i_IRDETO_SIGNED_bootloader_IMAGE_V5.1.2\update\{}".format(
        cd5_file)
    dst_file = r"F:\IRDETO_0238_0037.CD5"
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


def file_usb_before_enter_app(filename, wait_time=0):
    """
    upgrade via USB before the STB can enter DVT APP
    :param filename:str,CD5 file name
    :param match_info: the texts to be matched
    :param wait_time: sleep time before start match
    :param timeout_secs: the time to match texts
    :return: None
    """
    rds = v5_usb_init(filename)
    time.sleep(wait_time)
    rds.usb_switch_none()
    return rds


with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    dsn7714i_sdram_file = load_dict.get("dsn7714i_sdram_file")
    dsn7714i_download_file_signed = load_dict.get("dsn7714i_download_file_signed")
    print(dsn7714i_sdram_file)
    print(dsn7714i_download_file_signed)

clean_key()
file_usb_before_enter_app('man/IRDETO_0238_0037.CD5', wait_time=60)
file_usb_before_enter_app('dev/IRDETO_0238_0037.CD5', wait_time=60)
file_usb_before_enter_app('cd5/IRDETO_0238_0037.CD5', wait_time=240)

os.system("taskkill /F /IM ATServer.exe")
