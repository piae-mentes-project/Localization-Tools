# Excel转Lang文件（翻译组用）

Unicode更新：删除了不必要的文件/目录，新增了requirements.txt，重写了.gitignore

requirements.txt使用方法：

```
pip install -r requirements.txt -i https://pypi.douban.com/simple/
```

建议使用pyinstaller打包，方法如下：

```
pip install pyinstaller -i https://pypi.douban.com/simple/
pyinstaller -F main.py
```
