import os
while True:
    a = input("please input your choose:")
    if a == "":
        pass
        # auto_xshell_input()
    if a == "q" or a == "Q":
        os.system("taskkill /F /IM ATServer.exe")
        os.system("taskkill /F /IM tftpd32.exe")
        os.system("taskkill /F /IM Xshell.exe")
        # os.system("taskkill /F /IM explorer.exe")
        break