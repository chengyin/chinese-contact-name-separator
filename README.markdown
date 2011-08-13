SeparateChineseNames.py
=====================
将地址簿中中文名字拆分成姓和名按 Last Name 和 First Name 存储。

需求
----

- Mac OS X 10.5 (or other ScriptingBridge-capable systems)
- Python (Pre-installed in Mac OS X)

使用
----

1. 关闭 Address Book。
2. 执行
    $ python SeparateChineseNames.py
    
这个命令会将地址簿中中文名字拆分成姓和名按 Last Name 和 First Name 存储。

具体来说，所更新的项为：
1. 有 First Name 而没有 Last Name。
2. First Name 全为汉字且长度在 1 和 3 之间。

脚本*不会*处理复姓、公司名称等情况。

---

其他的问题请联系 chengyin.liu@gmail.com。
基本框架 fork 自 jjgod 的 [APN 脚本](http://github.com/jjgod/apn)。

Please use it at your own risk.
