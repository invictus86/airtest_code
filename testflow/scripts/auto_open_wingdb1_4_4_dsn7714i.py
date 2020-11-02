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


with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    dsn7714i_sdram_file = load_dict.get("dsn7714i_sdram_file")
    dsn7714i_download_file = load_dict.get("dsn7714i_download_file")
    print(dsn7714i_sdram_file)
    print(dsn7714i_download_file)

# double_click(Template(r"../res/img/open_hi_tool.png", threshold=0.7))

win32api.ShellExecute(0, 'open', r'D:\auto_burn_module\DSN7714i\WinGDB\WinGDB_v1.4.4\WinGDB_1.4.4\WinGDB.exe', '', '',
                      1)
# assert_exists(Template(r"../res/img/wingdb/wingdb_ico.png", threshold=0.9))
# logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_ico.png", threshold=0.9))')
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_platform_setting.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_platform_setting.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_stream_file.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_stream_file.png"))')
time.sleep(0.5)
xshell_import_cmd(dsn7714i_sdram_file)
logging.info('xshell_import_cmd(dsn7514i_stream_file)')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_ok.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ok.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_init_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_init_ice.png"))')
time.sleep(0.5)
rds, _, _ = v5_sys_init()
rds.power_off()
time.sleep(3)
rds.power_on()
touch(Template(r"../res/img/wingdb/wingdb_init_ok.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_init_ok.png"))')
time.sleep(0.5)
assert_exists(Template(r"../res/img/wingdb/wingdb_init_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_init_success.png", threshold=0.9))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_download.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_download.png"))')
time.sleep(0.5)
xshell_import_cmd(dsn7714i_download_file)
logging.info('xshell_import_cmd(dsn7514i_download_file)')
time.sleep(60)
touch(Template(r"../res/img/wingdb/wingdb_mst_output.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_mst_output.png"))')
time.sleep(0.5)
assert_exists(Template(r"../res/img/wingdb/wingdb_download_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_download_success.png", threshold=0.9))')
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_go.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_go.png"))')
# try:

# time.sleep(90)
time.sleep(50)
try:
    assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))
except:
    assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))')
os.system("taskkill /F /IM WinGDB.exe")
os.system("taskkill /F /IM ATServer.exe")
