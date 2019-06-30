from pyaria2 import Aria2RPC
import os
from colorama import Fore
from platform import system


class Mgekaria():
    def __init__(self):
        self.conf = ''
        self.data = {
            "dhtport":"--dht-listen-port=6666",
            "btport":"--listen-port=51314",
            "s":"-s16",
            "x":"-x10",
            "j":"-j3",
            "c":"-c",
            "speed":"--max-download-limit=8000k",
            "daemon":""
        }
        for cus in self.data:
            self.conf = self.conf + self.data[cus] +' '
        self.jsonrpc = Aria2RPC('http://localhost:2333/rpc')
        set_dir = os.path.dirname(__file__)
        self.options = {"dir": set_dir}

    def start(self):
        try:
            if system() == 'Windows':
                p = os.popen(r'aria2c.exe --conf-path=aria2\aria2w.conf')
                print('')
            elif system() == 'Linux':
                p = os.popen(r'aria2c --conf-path=aria2\aria2l.conf')
            else:
                p = os.popen(r'aria2c --conf-path=aria2\aria2l.conf')

        except:
            print('aria2后台服务启动失败\n')

    def kill(self):
        os.popen(r'taskkill /F /IM aria2c.exe')
        print('关闭所有aria2c进程')

    def get_file_from_url(self,link):
        self.jsonrpc.addUri([link],self.options)

    def get_file_from_cmd(self,link):
        if system() == 'Windows':
            exe_path = r'aria2c.exe'
        elif system() == 'Linux':
            exe_path = r'aria2c'
        else:
            exe_path = r'aria2c'
        order = exe_path  +' ' + self.conf + link
        os.system(order)

    def showactive(self):
        rpc = self.jsonrpc
        data = rpc.tellActive()[0]
        print('完成进度:',data['completedLength'],'连接数:',data['connections'],\
        '下载路径:',data['dir'],'下载速度:',data['downloadSpeed'],'\n','gid:',data['gid'])
        # print(rpc.tellStatus(data['gid']))


    def customize(self):
        list = '''
        1.dht监听端口
        2.bt监听端口
        3.最大线程数
        4.允许线程数
        5.同时下载文件数
        6.是否断点续传
        7.最大下载速率(0为不限制)
        8.后台保护进程
        '''
        print(Fore.GREEN,list,Fore.RESET)
        num = input('输入序号修改 ')
        if num == '1':
            conf = input('输入端口号 ')
            self.data["dhtport"] = "--dht-listen-port=" + str(conf)
        elif num == '2':
            conf = input('输入端口号 ')
            self.data["btport"] = "--listen-port=" + str(conf)
        elif num == '3':
            conf = input('输入最大线程数 ')
            self.data["s"] = "-s" + str(conf)
        elif num == '4':
            conf = input('输入下载线程数(最大为16) ')
            self.data["x"] = "-x" + str(conf)
        elif num == '5':
            conf = input('输入同时下载任务数 ')
            self.data["j"] = "-j" + str(conf)
        elif num == '6':
            conf = input('是否续传y/n  ')
            if conf == 'y':
                self.data["c"] = "-c"
            elif conf == 'n':
                self.data["c"] = ""
            else:
                print('输入y/n\n')
        elif num == '7':
            conf = input('限制最大下载速率 ')
            if conf == '0':
                self.data["speed"] = ""
            else:
                self.data["speed"] = "--max-download-limit=" + conf + "k"
        elif num == '8':
            conf = input('是否开启后台保护(y/n) ')
            if conf == 'y':
                self.data["daemon"] = "-D"
            else:
                self.data["daemon"] = ""
        else:
            print(Fore.RED,'序号错误',Fore.RESET)

        self.conf = ''
        for cus in self.data:
            self.conf = self.conf + self.data[cus] +' '
        print(Fore.YELLOW,self.conf,Fore.RESET)