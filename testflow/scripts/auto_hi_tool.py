# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
        "Windows:///",
    ]
               )



# script content
print("start...")

assert_exists(Template(r"../res/img/hitool_hi3716mv450.png"))

touch(Template(r"../res/img/jtag_network.png"))

touch(Template(r"../res/img/burn.png"))
# time.sleep(0.5)

time.sleep(85)
assert_exists(Template(r"../res/img/burn_success.png"))
time.sleep(3)
