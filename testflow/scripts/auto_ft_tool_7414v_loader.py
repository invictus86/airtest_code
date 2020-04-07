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


double_click(Template(r"../res/img/open_ft_tool.png", threshold=0.7))
time.sleep(1)
assert_exists(Template(r"../res/img/ft_tool_v4_0_1.png"))
assert_exists(Template(r"../res/img/burn_check_partitions.png"))
swipe(Template(r"../res/img/ft_tool_begin.png"), Template(r"../res/img/ft_tool_end.png"), vector=[0.0016, 0.0056])
time.sleep(1)
touch(Template(r"../res/img/ft_tool_open.png"))

with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    str3 = load_dict.get("data3")
    print(str3)
    logging.info(str3)

time.sleep(3)
xshell_import_cmd(str3)

touch(Template(r"../res/img/clear_message.png"))
# time.sleep(0.5)
touch(Template(r"../res/img/set_device.png"))
assert_exists(Template(r"../res/img/single_core.png"))
touch(Template(r"../res/img/set.png"))
assert_exists(Template(r"../res/img/formatting.png"))
touch(Template(r"../res/img/cancle.png"))
# time.sleep(0.5)
touch(Template(r"../res/img/start_burn.png"))
time.sleep(15)
assert_exists(Template(r"../res/img/ft_tool_burn_success.png"))
time.sleep(3)

while True:
    a = input("please input your choose:")
    if a == "":
        touch(Template(r"../res/img/clear_message.png"))
        # time.sleep(0.5)
        touch(Template(r"../res/img/set_device.png"))
        assert_exists(Template(r"../res/img/single_core.png"))
        touch(Template(r"../res/img/set.png"))
        assert_exists(Template(r"../res/img/formatting.png"))
        touch(Template(r"../res/img/cancle.png"))
        # time.sleep(0.5)
        touch(Template(r"../res/img/start_burn.png"))
        time.sleep(15)
        assert_exists(Template(r"../res/img/ft_tool_burn_success.png"))
        time.sleep(3)
    if a == "q" or a == "Q":
        # touch(Template(r"../res/img/exit.png", threshold=0.5))
        os.system("taskkill /F /IM FT_Tool.exe")
        break
