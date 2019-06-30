import wget

#wget download

class Pywget():
    def get(self,url):
        wget.download(url,out='download')

    def getoname(self,url,name):
        wget.download(url,out=name)

