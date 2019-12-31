# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

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


double_click(Template(r"../res/img/open_hi_tool.png", threshold=0.7))
time.sleep(10)
assert_exists(Template(r"../res/img/hitool_hi3716mv450.png", threshold=0.9))
touch(Template(r"../res/img/jtag_network.png"))
time.sleep(1)
touch(Template(r"../res/img/view.png"))

str1 = r"D:\9615\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\burn\spi_nand_partitions_irdeto.xml"
str2 = r"D:\9615\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\CH05101351_B7_signed_DSD9615iETL_BOOTLOADER_IMAGE_V5.1.6\burn\advca_programmer.bin"

xshell_import_cmd(str1)
# time.sleep(3)
touch(Template(r"../res/img/big_view.png"))
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
    a = input("input:")
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
        break
# touch(Template(r"../res/img/confirm.png", threshold=0.7))
# time.sleep(1)
# touch(Template(r"../res/img/exit.png", threshold=0.5))
