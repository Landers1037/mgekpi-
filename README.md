# mgekpi plus工具
整合了aria2 wget you-get的命令行下载工具

### 使用

```bash
$ python3 mgekpi.py [option]
```

```bash
 Welcome Mgekpi
Usage: mgekpi.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  aria
  conf
  wget
  youget
```

#### aria2服务下载

```bash
$ python mgekpi.py aria url
```

#### aria2单文件下载模式

```bash
$ python mgekpi aria --o url
```

#### you-get下载

```bash
$ python mgekpi youget url
```

#### wget多线程下载

```bash
$ python mgekpi wget url
```

#### 修改配置

```bash
$ python mgekpi.py conf
```

修改aria2单文件模式的配置

```bash
 Welcome Mgekpi
 
        1.dht监听端口
        2.bt监听端口
        3.最大线程数
        4.允许线程数
        5.同时下载文件数
        6.是否断点续传
        7.最大下载速率(0为不限制)
        8.后台保护进程
         
输入序号修改
```

#### 退出aria2后台服务

```bash
$ python mgekpi.py conf --k
```

