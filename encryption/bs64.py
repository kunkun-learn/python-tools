import base64

# base64编码
s = 'ms08067'
bs = base64.b64decode(s.encode('utf-8'))
print(bs)

# base64解码
bbs = str(base64.b64decode(bs), 'utf-8')
print(bbs)
print('\n')
