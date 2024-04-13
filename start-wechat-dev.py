import tkinter as tk
import webbrowser
import PIL

from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage

# 网页链接
def open_webpage():
    webbrowser.open("https://szfilehelper.weixin.qq.com/")


def get_img(filename, width, height):
    im = PIL.Image.open(filename).resize((width, height))
    im = ImageTk.PhotoImage(im)
    return im

# 创建窗口：实例化一个窗口对象。
root = Tk()
 
# 窗口大小
root.geometry("600x450+374+182")
 
#  窗口标题
root.title("我的个性签名设计")

# 设置背景图片
# 打开图片
image = PIL.Image.open("E:/文件项目/Python/background.png")

# 加载图片
bg_image = PhotoImage(file="E:/文件项目/Python/background.png")

# 创建一个标签，将图片设置为其背景
label = Label(root, image=bg_image)

# 将标签放置在窗口中
label.place(x=0, y=0, relwidth=1, relheight=1)
 
# 添加标签控件
label = Label(root,text="本电脑暂不支持登录微信",font=("宋体",30),fg="black")
"""
text参数用于指定显示的文本；
font参数用于指定字体大小和字体样式；
fg参数用于指定字体颜色；
"""
# 定位
label.grid(row=0,column=0)

# 第二行文字
label = Label(root,text="请点击下方使用网页文件传输助手",font=("宋体",30),fg="black")
# 定位
label.grid(row=1,column=0)

# 第二行文字
label = Label(root,text="以进行传输文件",font=("宋体",30),fg="black")
# 定位
label.grid(row=2,column=0)

# 添加点击按钮
button = Button(root,text="打开网页文件传输助手",font=("宋体",25),fg="blue",command=open_webpage)
button.grid(row=3,column=0)

# 显示窗口
root.mainloop()