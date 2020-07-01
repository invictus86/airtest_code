# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import win32api, json
import ctypes
import logging

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
xshell_import_cmd("0x300000")
time.sleep(1)
touch(Template(r"../res/img/DSN5414a/start.png"))
time.sleep(420)
assert_exists(Template(r"../res/img/DSN5414a/burn_success.png"))
touch(Template(r"../res/img/DSN5414a/burn_success_ok.png"))
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

while True:
    a = input("please input your choose:")
    if a == "":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        touch(Template(r"../res/img/DSN5414a/start.png"))
        time.sleep(420)
        assert_exists(Template(r"../res/img/DSN5414a/burn_success.png"))
        touch(Template(r"../res/img/DSN5414a/burn_success_ok.png"))
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    if a == "q" or a == "Q":
        # touch(Template(r"../res/img/exit.png", threshold=0.5))
        os.system("taskkill /F /IM WinSTBUpgrader.exe")
        os.system("taskkill /F /IM LaunchPad.exe")
        break
