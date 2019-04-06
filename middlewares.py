#在middlewares.py文件下面添加此代理，第七行的账号密码是你的代理账号密码
import base64
#使用阿布云代理ip
class my_proxy(object):
    def process_request(self,request,spider):
        request.meta['proxy'] = 'http-dyn.abuyun.com:9020'
        proxy_name_pass = b'H80I8052G49WUJ2D:F2438463FECC134F'
        encode_pass_name = base64.b64encode(proxy_name_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encode_pass_name.decode()
