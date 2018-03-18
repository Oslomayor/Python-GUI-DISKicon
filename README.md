# Python-GUI-DISKicon
Python GUI 程序，快速制作个性化磁盘图标

### 9:41PM, Mar 18th, 2018 @ HDU_Wireless

##  使用效果

### 主界面

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/%E4%BF%AE%E6%94%B9%E7%A3%81%E7%9B%98%E5%9B%BE%E6%A0%87.PNG?raw=true)

### U盘效果

![](https://raw.githubusercontent.com/Oslomayor/USB-Device-ICO/master/%E9%95%87%E9%95%BF%E7%9A%84U%E7%9B%98.PNG)

## 环境配置

* Python 3.6

  以及3个Python的标准库，不需另外安装第三方库

* os

* shutil

* tkinter

## 使用说明

* 更改磁盘或U盘的默认图标

* 本质上是往磁盘中写入一个 **autorun.inf** 文件  

  内容是

  > [Autorun]
  >
  > icon=xxx.ico

  其中 xxx 为 ico 图片的文件名

  Windows 读取磁盘时, 会自动运行 **autorun.inf**

* 之前写了[C语言版本](https://github.com/Oslomayor/USB-Device-ICO) ，最近在学习Python的图形库tkinter，于是做了个GUI版本

* U盘需要重新拔插见效，电脑的磁盘需要重启电脑生效
