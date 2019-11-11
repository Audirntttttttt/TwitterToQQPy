# Twitter to QQ (Python)

这个Python脚本可以将一个或多个推特账号的更新推送至QQ，并且可以机翻，使用python方便扩展更多功能。

## 依赖

首先需要 酷Q Pro （使用酷Q Air将无法发送图片）并在 [这里](https://cqhttp.cc/docs/4.12/#/Configuration) 按照教程配置好 CQhttp 插件
爬虫部分采用 [RSSHub](https://rsshub.app/)。
Python依赖在request.txt中

## 使用方法

### 安装

```bash
git clone git@github.com:Audirntttttttt/TwitterToQQPy.git
cd TwitterToQQPy
pip install -r requirements.txt
```

### 配置

#### CoolQ的配置

在酷Q目录下`\data\app\io.github.richardchien.coolqhttpapi\config`的json文件中，修改以下选项：

```json
"port": 你使用的接口,
"use_http": true,
"use_ws": false,
"access_token": "your token",
"secret": "your secret",
```
在本项目的目录下，修改config.py：
```python
access_token = 'your access_token'
secret = 'your secret'
api_root = '酷Qhttp运行的地址'
```
与上方的配置相对应

#### 百度翻译API的配置

在[这里](http://api.fanyi.baidu.com/api/trans/product/index)申请百度翻译的API的接口，并修改config.py:

```python
#百度翻译的appid与secretKey

appid = 'your appid'
secretKey = 'your secretkey'
```

#### 发送与接收的配置

在config.py中设置，config.py有详尽的说明。

### 启动文件

配置完成后

```bash
python main.py
```

或者

```bash
pm2 start main.py --interpreter=python3
```



