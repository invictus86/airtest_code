import socket, time
import ekt_rds, ekt_dta, ekt_file, ekt_net


def cope_file_to_new_path(old_file_path, new_file_path):
    with open(old_file_path, "rb") as f1, open(new_file_path, "wb") as f2:
        content = f1.read()
        f2.write(content)


def get_local_ip():
    """
    get local ip
    :return:
    """
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for item in addrs:
        if str(item[-1][0])[0:3] == "192":
            ip = str(item[-1][0])
            print("current ip is : {}".format(ip))
    return ip


def v5_sys_init():
    """
    init the system,establish connect to the ATserver.
    :return: rds(EKTRds instance),doc(EktFileCfg instance),dta(EktDtDevice instance)
    """
    curretn_ip = get_local_ip()
    net = ekt_net.EktNetClient(curretn_ip, 8900)
    rds = ekt_rds.EktRds(net)
    dta = ekt_dta.EktDtDevice(net)
    doc = ekt_file.EktFileCfg(net)
    return rds, doc, dta


def v5_usb_init(cd5_file):
    """
    perform copy cd5 file from the computer to the usb,then switch the usb connect to the STB and reboot the STB
    :param cd5_file: str,the CD5 file name
    :return: rds,EktRds instance
    """
    rds, doc, _ = v5_sys_init()
    src_file = doc.cd5_file(cd5_file)
    dst_file = doc.usb_file(doc.load_file)

    rds.power_off()
    time.sleep(2)
    rds.usb_switch_pc()
    time.sleep(8)
    doc.copy_file(src_file, dst_file)
    time.sleep(6)
    rds.power_on()
    time.sleep(1)
    rds.usb_switch_stb()
    return rds


def file_usb_before_enter_app(filename, wait_time=0):
    """
    upgrade via USB before the STB can enter DVT APP
    :param filename:str,CD5 file name
    :param match_info: the texts to be matched
    :param wait_time: sleep time before start match
    :param timeout_secs: the time to match texts
    :return: None
    """
    rds = v5_usb_init(filename)
    time.sleep(wait_time)
    rds.usb_switch_none()
    return rds


def clean_key():
    """
    upgrade EKCleanSPCBKey.CD5 set the STB to default value.
    :return: None
    """
    rds, doc, _ = v5_sys_init()
    rds.power_off()
    time.sleep(1)
    rds.power_on()
    time.sleep(3)
    src_file = doc.cd5_file(doc.clean_file)
    print(src_file)
    dst_file = doc.usb_file(doc.clean_file)
    print(dst_file)
    del_file = doc.usb_file(doc.load_file)
    rds.usb_switch_pc()
    time.sleep(8)
    doc.del_file(del_file)
    time.sleep(5)
    doc.copy_file(src_file, dst_file)
    time.sleep(6)
    rds.power_off()
    time.sleep(1)
    rds.power_on()
    time.sleep(1)
    rds.usb_switch_stb()
    time.sleep(10)
    try:
        # wait_for_text_match("Clean Key", 60)
        time.sleep(10)
    finally:
        rds.usb_switch_pc()
        time.sleep(5)
        doc.del_file(dst_file)
        rds.usb_switch_none()
        time.sleep(10)


def test_06_04_loader_osd():
    """
    upgrade 'MANKEY.CD5','DEVKEY.KD5','DEV003.CD5',after upgrade STB can enter DVTAPP or an exception will be raised
    :return:None
    """
    clean_key()
    rds = file_usb_before_enter_app('MANKEY.CD5', wait_time=60)
    time.sleep(1)
    file_usb_before_enter_app('DEVKEY.KD5', wait_time=60)
    time.sleep(1)
    file_usb_before_enter_app('DEV003.CD5', wait_time=240)


test_06_04_loader_osd()
