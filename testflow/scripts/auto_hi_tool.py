# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///?title_re=HiTool-Hi3716MV450*",
        # "Windows:///",
    ]
               )

# script content
print("start...")

# assert_exists(Template(r"../res/img/111.png"))
# assert_exists(Template(r"../res/img/hitoo716mv4l_hi350.png", threshold=0.9))
# Template(r"../res/img/jtag_network.png")

touch(Template(r"../res/img/burn.png", threshold=0.7))

# double_click(Template(r"../res/img/burn.png", record_pos=(0.308, 0.05), resolution=(1280, 800)))


# double_click(Template(r"tpl1577434199857.png", rgb=True, record_pos=(-0.272, 0.187), resolution=(627, 760)))
# touch(Template(r"tpl1577434199857.png", rgb=True, record_pos=(-0.272, 0.187), resolution=(627, 760)))

# touch(Template(r"../res/img/burn.png"))
# # time.sleep(0.5)
#
time.sleep(90)
assert_exists(Template(r"../res/img/burn_success.png", threshold=0.9))
# time.sleep(3)
# touch(
