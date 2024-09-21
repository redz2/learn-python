1. pip设置国内源
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

2. 配置venv
```
python -m venv .venv
```

3. 安装python解释器
* 官网下载安装：https://www.python.org/downloads/
* 解压后进行安装(比较耗时)
```
./configure -C --with-openssl=/usr/local/openssl --with-openssl-rpath=auto --prefix=/usr/local/python312
make && make install
```
* 配置环境变量
```
echo "export PATH=$PATH:/usr/local/python312/bin" >> /etc/profile
```