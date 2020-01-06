# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import json
import win32api

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        # "Windows:///?title_re=HiTool-Hi3716MV450*",
        "Windows:///",
    ]
               )

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


# double_click(Template(r"../res/img/open_hi_tool.png", threshold=0.7))
win32api.ShellExecute(0, 'open', r'D:\9615\HiTool-STB-5.0.45\HiTool\HiTool.exe', '', '', 1)
time.sleep(10)
assert_exists(Template(r"../res/img/hitool_hi3716mv450.png", threshold=0.9))
touch(Template(r"../res/img/jtag_network.png"))
time.sleep(1)
touch(Template(r"../res/img/view.png"))

with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    str1 = load_dict.get("data1")
    str2 = load_dict.get("data2")
    print(str1)
    print(str2)

# str1 = r"D:\9615\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\burn\spi_nand_partitions_irdeto.xml"
# str2 = r"D:\9615\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\burn\advca_programmer.bin"
time.sleep(3)
xshell_import_cmd(str1)
# time.sleep(3)
touch(Template(r"../res/img/big_view.png"))
time.sleep(3)
xshell_import_cmd(str2)

touch(Template(r"../res/img/burn.png", threshold=0.7))
time.sleep(3)
touch(Template(r"../res/img/console.png", threshold=0.7))

time.sleep(80)
assert_exists(Template(r"../res/img/burn_success.png", threshold=0.9))
try:
    assert_exists(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
    touch(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
except:
    pass

while True:
    a = input("please input your choose:")
    if a == "":
        touch(Template(r"../res/img/burn.png", threshold=0.7))
        time.sleep(83)
        assert_exists(Template(r"../res/img/burn_success.png", threshold=0.9))
        try:
            assert_exists(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
            touch(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
        except:
            pass
    if a == "q" or a == "Q":
        # touch(Template(r"../res/img/exit.png", threshold=0.5))
        os.system("taskkill /F /IM HiTool.exe")
        break
# touch(Template(r"../res/img/confirm.png", threshold=0.7))
# time.sleep(1)
# touch(Template(r"../res/img/exit.png", threshold=0.5))
