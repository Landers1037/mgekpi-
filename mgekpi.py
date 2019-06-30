from pywget import Pywget
from aria2 import Mgekaria
from youget import Mgekget
import click
from colorama import Fore ,init
from platform import system

if system() == 'Windows':
    init(wrap=True)
elif system() == 'Linux':
    init(autoreset=True)
else:
    init(wrap=True)

print(Fore.GREEN,'Welcome Mgekpi')

#装饰函数接口
@click.group()
def mgek():
    pass

@click.command()
@click.argument('url')
@click.option('--o',is_flag=True, help='单文件模式')
def aria(url,o):
    aria2 = Mgekaria()
    if o:
        aria2.start()
        aria2.get_file_from_cmd(url)
    else:
        aria2.get_file_from_url(url)


@click.command()
@click.argument('url')
def wget(url):
    wget = Pywget()
    wget.get(url)


@click.command()
@click.argument('url')
def youget(url):
    youget = Mgekget()
    youget.get(url)
    
@click.command()
@click.option('--c',is_flag=True,help='修改aria2单文件下载配置')
@click.option('--k',is_flag=True,help='退出aria2')
def conf(c,k):
    aria2 = Mgekaria()
    if c:
        aria2.customize()
    elif k:
        aria2.kill()
    else:
        aria2.customize()

mgek.add_command(aria)
mgek.add_command(wget)
mgek.add_command(youget)
mgek.add_command(conf)



if __name__ == '__main__':
    mgek()