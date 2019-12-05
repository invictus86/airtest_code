# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.win.win import Windows

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "Windows:///",
        # "Windows:///?title_re=New Session*",
    ])

# script content
print("start...")

print(ST.THRESHOLD)
# with open("my-testflow/res/img/Snipaste_2019-12-04_11-18-52.png", "rb") as f:
# with open(r"../res/img/Snipaste_2019-12-04_11-18-52.png", "rb") as f:
#     print(f.read())

# text("aaa")
# touch(Template(r"tpl1575363995837.png", record_pos=(-0.478, -0.027), resolution=(3200, 1080)))
# touch(Template(r"tpl1575363995837.png"))
# touch(Template(r"../res/img/Snipaste_2019-12-04_11-18-52.png"))

# touch(Template(r"../res/img/Snipaste_2019-12-04_11-18-52.png"))

# touch(Template(r"res/img/Snipaste_2019-12-04_11-18-52.png"))
# # touch(Template(r"C:\Users\ivan.zhao\PycharmProjects\my-testflow\res\img\Snipaste_2019-12-04_11-18-52.png"))
# sleep(0.3)

# touch(Template(r"tpl1575365154636.png", record_pos=(-0.474, -0.015), resolution=(3200, 1080)))
# sleep(0.3)
#
# touch(Template(r"tpl1575365204067.png", record_pos=(-0.409, -0.014), resolution=(3200, 1080)))
# sleep(0.3)
#
# text("1024000")
# sleep(0.3)
# touch(Template(r"tpl1575365331049.png", record_pos=(-0.21, 0.014), resolution=(3200, 1080)))


# touch(Template(r"tpl1575337213806.png", record_pos=(-0.347, -0.157), resolution=(3200, 1080)))

# # double_click(Template(r"tpl1575337213806.png", record_pos=(-0.347, -0.157), resolution=(3200, 1080)))
# #
# # # Windows.mouse_down(button='right')
# window = Windows()
# address = window.get_ip_address()
# print(address)
# # window.start_app(path=r"C:\Users\ivan.zhao\Desktop\SpRcApi.png")
# # print(window.get_title())

# window.mouse_down(button='right')
# time.sleep(0.1)
# window.mouse_up(button="right")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
