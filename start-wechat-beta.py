import tkinter as tk
import webbrowser
import PIL
import io
import requests

from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage

# 网页链接
def open_webpage():
    webbrowser.open("https://szfilehelper.weixin.qq.com/")


# 创建窗口：实例化一个窗口对象。
root = Tk()
 
# 窗口大小
root.geometry("600x450+374+182")
 
# 窗口标题
root.title("微信")

# 窗口图标
root.iconbitmap('.\wechat.ico')
 
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

'''
# 暂时使用不正常
# 图片链接
url = "https://bing.joker.cc/api/"
# 下载图片数据
image_bytes = requests.get(url).content
# 将数据存放到data_stream中
data_stream = io.BytesIO(image_bytes)
# 转换为图片格式
pil_image = PIL.Image.open(data_stream)
# 获取图片的宽度和高度
w, h = pil_image.size
# 获取图片的文件名
fname = url.split('/')[-1]
sf = "{} ({}x{})".format(fname, w, h)
# 将pil格式的图片转换为tk格式的image
tk_image = ImageTk.PhotoImage(pil_image)
# 创建个label组件, root作为父节点
label = Label(root, image=tk_image)
# 定位
label.grid(row=3,column=0)
'''

# 显示窗口
root.mainloop()