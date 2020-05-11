# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import json
import win32api
import ctypes
import logging
from airtest.core.settings import Settings

Settings.FIND_TIMEOUT = 30

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
    dtn7514i_stream_file = load_dict.get("dtn7514i_stream_file")
    dtn7514i_download_file = load_dict.get("dtn7514i_download_file")
    print(dtn7514i_stream_file)
    print(dtn7514i_download_file)

# double_click(Template(r"../res/img/open_hi_tool.png", threshold=0.7))
win32api.ShellExecute(0, 'open', r'D:\7514\wingdb_tool\WinGDB_v1.4.0\WinGDB_v1.4.0\WinGDB_v1.4.0.exe', '', '', 1)
assert_exists(Template(r"../res/img/wingdb/wingdb_ico.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_ico.png", threshold=0.9))')
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_platform_setting.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_platform_setting.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_stream_file.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_stream_file.png"))')
time.sleep(0.5)
xshell_import_cmd(dtn7514i_stream_file)
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
xshell_import_cmd(dtn7514i_download_file)
logging.info('xshell_import_cmd(dsn7514i_download_file)')
time.sleep(10)
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
time.sleep(30)
try:
    assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))
except:
    assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))')
os.system("taskkill /F /IM WinGDB_v1.4.0.exe")
