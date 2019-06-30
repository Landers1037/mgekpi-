from os import system

class Mgekget():

    def get(self,url):
        cmd = "you-get" + url
        system(cmd)