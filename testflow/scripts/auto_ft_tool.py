# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os


def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)


del_files("./log/")

if not cli_setup():
    auto_setup(__file__, logdir="./log/", devices=[
        "Windows:///",
    ]
               )

# script content
print("start...")

assert_exists(Template(r"../res/img/ft_tool_v4_0_1.png"))
assert_exists(Template(r"../res/img/burn_check_partitions.png"))

touch(Template(r"../res/img/clear_message.png"))
time.sleep(0.5)
touch(Template(r"../res/img/set_device.png"))
assert_exists(Template(r"../res/img/single_core.png"))
touch(Template(r"../res/img/set.png"))
assert_exists(Template(r"../res/img/formatting.png"))
touch(Template(r"../res/img/cancle.png"))
time.sleep(0.5)
touch(Template(r"../res/img/start_burn.png"))
time.sleep(15)
assert_exists(Template(r"../res/img/hundred_percent.png"))
time.sleep(3)
