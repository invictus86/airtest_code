# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import json
import win32api
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
        # "Windows:///?title_re=HiTool-Hi3716MV450*",
        "Windows:///",
    ]
               )

# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
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
    dsn7514i_stream_file = load_dict.get("dsn7514i_stream_file")
    dsn7514i_download_file = load_dict.get("dsn7514i_download_file")
    print(dsn7514i_stream_file)
    print(dsn7514i_download_file)

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
xshell_import_cmd(dsn7514i_stream_file)
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
xshell_import_cmd(dsn7514i_download_file)
logging.info('xshell_import_cmd(dsn7514i_download_file)')
time.sleep(10)
assert_exists(Template(r"../res/img/wingdb/wingdb_download_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_download_success.png", threshold=0.9))')
touch(Template(r"../res/img/wingdb/wingdb_mst_output.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_mst_output.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_ice.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_ice.png"))')
time.sleep(0.5)
touch(Template(r"../res/img/wingdb/wingdb_go.png"))
logging.info('touch(Template(r"../res/img/wingdb/wingdb_go.png"))')
time.sleep(30)
assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))
logging.info('assert_exists(Template(r"../res/img/wingdb/wingdb_burn_success.png", threshold=0.9))')
os.system("taskkill /F /IM WinGDB_v1.4.0.exe")



# touch(Template(r"../res/img/wingdb/wingdb_strean_file_open.png"))

# try:
#     assert_exists(Template(r"../res/img/hitool/choose_chip.png", threshold=0.9))
#     touch(Template(r"../res/img/hitool/combo_box.png"))
#     time.sleep(0.5)
#     swipe(Template(r"../res/img/hitool/hitool_begin.png"), Template(r"../res/img/hitool/hitool_end.png"))
#     time.sleep(0.5)
#     touch(Template(r"../res/img/hitool/hi3716mv450.png"))
#     time.sleep(0.5)
#     touch(Template(r"../res/img/hitool/hitool_confirm.png"))
#     time.sleep(3)
#     touch(Template(r"../res/img/hitool/hiburn.png"))
# except:
#     pass
#
# time.sleep(3)
# assert_exists(Template(r"../res/img/hitool_hi3716mv450.png", threshold=0.9))
# touch(Template(r"../res/img/jtag_network.png"))
# time.sleep(0.5)
# touch(Template(r"../res/img/view.png"))
#
# with open(r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\config.json", 'r') as load_f:
#     load_dict = json.load(load_f)
#     # print(load_dict)
#     str1 = load_dict.get("data1")
#     str2 = load_dict.get("data2")
#     print(str1)
#     print(str2)
#
# time.sleep(3)
# xshell_import_cmd(str1)
# # time.sleep(3)
# touch(Template(r"../res/img/big_view.png"))
# time.sleep(3)
# xshell_import_cmd(str2)
#
# touch(Template(r"../res/img/burn.png", threshold=0.7))
# time.sleep(3)
# touch(Template(r"../res/img/console.png", threshold=0.7))
#
# time.sleep(80)
# assert_exists(Template(r"../res/img/burn_success.png", threshold=0.9))
# try:
#     assert_exists(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
#     touch(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
# except:
#     pass
# os.system("taskkill /F /IM HiTool.exe")
# time.sleep(5)

# while True:
#     a = input("please input your choose:")
#     if a == "":
#         touch(Template(r"../res/img/burn.png", threshold=0.7))
#         time.sleep(83)
#         assert_exists(Template(r"../res/img/burn_success.png", threshold=0.9))
#         try:
#             assert_exists(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
#             touch(Template(r"../res/img/burn_success_confirm.png", threshold=0.9))
#         except:
#             pass
#     if a == "q" or a == "Q":
#         # touch(Template(r"../res/img/exit.png", threshold=0.5))
#         os.system("taskkill /F /IM HiTool.exe")
#         break
#
# import socket, time, sys, os
# import ctypes
#
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parentdir)
#
# # import ekt_rds, ekt_dta, ekt_file, ekt_net
# from ektlib import ekt_rds, ekt_dta, ekt_file, ekt_net
# from airtest.core.api import *
# from airtest.cli.parser import cli_setup
# import json
# import win32api
# import file_operate
#
#
# def cope_file_to_new_path(old_file_path, new_file_path):
#     with open(old_file_path, "rb") as f1, open(new_file_path, "wb") as f2:
#         content = f1.read()
#         f2.write(content)
#
#
# def get_local_ip():
#     """
#     get local ip
#     :return:
#     """
#     addrs = socket.getaddrinfo(socket.gethostname(), None)
#     for item in addrs:
#         if str(item[-1][0])[0:3] == "192":
#             ip = str(item[-1][0])
#             print("current ip is : {}".format(ip))
#     return ip
#
#
# def v5_sys_init():
#     """
#     init the system,establish connect to the ATserver.
#     :return: rds(EKTRds instance),doc(EktFileCfg instance),dta(EktDtDevice instance)
#     """
#     curretn_ip = get_local_ip()
#     net = ekt_net.EktNetClient(curretn_ip, 8900)
#     rds = ekt_rds.EktRds(net)
#     dta = ekt_dta.EktDtDevice(net)
#     doc = ekt_file.EktFileCfg(net)
#     return rds, doc, dta
#
#
# def v5_usb_init(cd5_file):
#     """
#     perform copy cd5 file from the computer to the usb,then switch the usb connect to the STB and reboot the STB
#     :param cd5_file: str,the CD5 file name
#     :return: rds,EktRds instance
#     """
#     rds, _, _ = v5_sys_init()
#     src_file = r"D:\9615\burn_file\unsigned_application_file\{}".format(cd5_file)
#     dst_file = r"F:\IRDETO_0238_0033.CD5"
#     print(src_file)
#     print(dst_file)
#
#     rds.power_off()
#     time.sleep(2)
#     rds.usb_switch_pc()
#     time.sleep(8)
#     file_operate.cope_file_src_dst(src_file, dst_file)
#     time.sleep(6)
#     rds.power_on()
#     time.sleep(0.5)
#     rds.usb_switch_stb()
#     return rds
#
#
# def file_usb_before_enter_app(filename, wait_time=0):
#     """
#     upgrade via USB before the STB can enter DVT APP
#     :param filename:str,CD5 file name
#     :param match_info: the texts to be matched
#     :param wait_time: sleep time before start match
#     :param timeout_secs: the time to match texts
#     :return: None
#     """
#     rds = v5_usb_init(filename)
#     time.sleep(wait_time)
#     rds.usb_switch_none()
#     return rds
#
#
# def clean_key():
#     """
#     upgrade EKCleanSPCBKey.CD5 set the STB to default value.
#     :return: None
#     """
#     rds, _, _ = v5_sys_init()
#     rds.power_off()
#     time.sleep(0.5)
#     rds.power_on()
#     time.sleep(3)
#     src_file = r"D:\9615\burn_file\unsigned_application_file\EKCleanSPCBKey.CD5"
#     print(src_file)
#     dst_file = r"F:\EKCleanSPCBKey.CD5"
#     print(dst_file)
#     del_file = r"F:\IRDETO_0238_0033.CD5"
#     rds.usb_switch_pc()
#     time.sleep(8)
#     file_operate.remove_file(del_file)
#     time.sleep(5)
#     file_operate.cope_file_src_dst(src_file, dst_file)
#     time.sleep(6)
#     rds.power_off()
#     time.sleep(0.5)
#     rds.power_on()
#     time.sleep(0.5)
#     rds.usb_switch_stb()
#     time.sleep(10)
#     try:
#         time.sleep(10)
#     finally:
#         rds.usb_switch_pc()
#         time.sleep(5)
#         file_operate.remove_file(dst_file)
#         rds.usb_switch_none()
#         time.sleep(10)
#
#
# def test_06_04_loader_osd():
#     """
#     upgrade 'MANKEY.CD5','DEVKEY.KD5','DEV003.CD5',after upgrade STB can enter DVTAPP or an exception will be raised
#     :return:None
#     """
#     clean_key()
#     rds = file_usb_before_enter_app('MANKEY.CD5', wait_time=60)
#     time.sleep(0.5)
#     file_usb_before_enter_app('DEVKEY.KD5', wait_time=60)
#     time.sleep(0.5)
#     file_usb_before_enter_app('DEV003.CD5', wait_time=240)
#
#
# if not cli_setup():
#     auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
#         "Windows:///",
#     ]
#                )
#
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
#
# double_click(Template(r"../res/img/ATserver/atserver_startup.png", threshold=0.9))
# # win32api.ShellExecute(0, 'open', r'D:\安装包\ATserver_contain_tsrate\ATServer.exe', '', '', 1)
# time.sleep(5)
#
# if not cli_setup():
#     auto_setup(__file__, logdir=r"C:\Users\ivan.zhao\PycharmProjects\airtest_code\testflow\scripts\log", devices=[
#         "Windows:///?title_re=ATServer*",
#         # "Windows:///",
#     ]
#                )
#
# # script content
# print("start...")
#
# touch(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
# # double_click(Template(r"../res/img/ATserver/atserver_connect.png", threshold=0.9))
# time.sleep(20)
# assert_exists(Template(r"../res/img/ATserver/atserver_data_not_found.png", threshold=0.9))
# touch(Template(r"../res/img/ATserver/atserver_confirm.png"))
# time.sleep(10)
#
# clean_key()
# file_usb_before_enter_app('MANKEY.CD5', wait_time=60)
# file_usb_before_enter_app('DEVKEY.KD5', wait_time=60)
# file_usb_before_enter_app('DEV003.CD5', wait_time=240)
# os.system("taskkill /F /IM ATServer.exe")

# while True:
#     a = input("please input your choose:")
#     if a == "":
#         clean_key()
#         file_usb_before_enter_app('MANKEY.CD5', wait_time=60)
#         file_usb_before_enter_app('DEVKEY.KD5', wait_time=60)
#         file_usb_before_enter_app('DEV003.CD5', wait_time=240)
#     if a == "q" or a == "Q":
#         os.system("taskkill /F /IM ATServer.exe")
#         break


