# 2:28PM, Mar 18th, 2018 @ dorm 602,18
# Python GUI 程序
# 快速制作个性化磁盘图标

import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def select_ico_disk():
    # filetypes=(("ico files","*.ico"),("ico files","*.ico")) 必须写两个("ico files","*.ico")才正常
    if messagebox.askokcancel("镇长出品", "请选择一张ico格式的图片") == False:
        os._exit(0)
    ico_dir = filedialog.askopenfilename(filetypes=(("ico files","*.ico"),("ico files","*.ico")))
    if messagebox.askokcancel("镇长出品", "请选择磁盘或U盘") == False:
        os._exit(0)
    disk_dir = filedialog.askdirectory()

    # 如果选择的 ico 图标不在该磁盘目录，则复制 ico 到磁盘
    # ico_dir 包含 ico 的文件名，用字符串方法提取路径
    if '/'.join(ico_dir.split('/')[:-1:])+'/' != disk_dir:
        shutil.copy(ico_dir, disk_dir)

    write_autoruninf(ico_dir, disk_dir)

def write_autoruninf(ico_dir, disk_dir):
    ico_name = 'disk_ico.ico'
    for item in os.listdir(disk_dir):
        # 从路径中提取文件名
        if item == ico_dir.split('/')[-1]:
            try:
                # 重命名 ico
                os.rename(disk_dir + '/' + item, disk_dir + '/' + ico_name)
            except FileExistsError:
                # 如果 ico 图标已经存在，则删除旧的 ico 图标
                os.remove(disk_dir + '/' + ico_name)
    # 以下4行,为更改U盘图标核心代码
    file = open(disk_dir + '/autorun.inf','w')
    file.write('[Autorun]')
    file.write('\n')
    file.write('icon={}'.format(ico_name))
    file.close()

    # 设置 inf 和 ico 文件属性为隐藏
    os.system('attrib +h {}'.format(disk_dir + 'autorun.inf'))
    os.system('attrib +h {}'.format(disk_dir + ico_name))

    messagebox.askokcancel("镇长出品", "制作完成，重启磁盘生效")

def main():
    top = tk.Tk(className='制作个性磁盘图标V1-镇长出品')
    top.minsize(350, 200)
    try:
        # 在按钮上添加图片
        img = tk.PhotoImage(file="E:\AllPrj\PyCharmPrj\py-GUI\img.png")
        start_button = tk.Button(top, image=img, text="点击制作磁盘图标", compound='top', command=select_ico_disk)
    except tk.TclError:
        # 若图片不存在，则不显示
        start_button = tk.Button(top, height=8, width=20, text="点击制作磁盘图标", compound='top', command=select_ico_disk)
    start_button.pack()
    top.mainloop()

if __name__ == '__main__':
    main()