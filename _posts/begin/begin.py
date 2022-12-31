import datetime
import glob
import sys
from tkinter import Tk,Entry

class blog:
    def createFile(self,msg):
        # 文件夹目录
        path = "D:\github pages\chirpy\_posts\\"
        # 新建博客序号
        number = len(glob.glob(path+"*.md"))+1
        # 获取当前年月日
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        # 新博客名字
        new_file=str(date)+"-"+str(number)+".md"
        f=open(path+new_file,"a",encoding="utf-8")
        f.write("---\n"+"title: "+msg+"\n"+"authod: cotes\n"+"date: "+date+" 17:22:00 +0800\n"+"categories: []\n"+"---\n")
        f.close
        # 目录文件
        content="目录.txt"
        f=open(path+content,"a",encoding="utf-8")
        f.write("\n["+msg+"]("+new_file+")")
        f.close
        sys.exit(0)

    def __init__(self):
        self.window = Tk()
        self.window.geometry('297x30')
        self.input_entry=Entry(self.window,font=('微软雅黑',14),bg='white',fg='black',exportselection=0,width=28)
        self.input_entry.pack(side="left")

        self.input_entry.bind("<Return>",self.commit)

    def commit(self,event=None):
        title=self.input_entry.get()
        self.createFile(title)
        

    def run(self):
        self.window.mainloop()

if __name__=='__main__':
    a=blog()
    a.run()