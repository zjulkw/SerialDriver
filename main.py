import serial
import time  # 延时使用
import binascii
import serial.tools.list_ports

data1 = '7a7d7e'
data2 = '7f7c7b'

#查看可用端口并自动建立连接
#s = serial.Serial("COM9", 115200)  # 初始化串口
plist = list(serial.tools.list_ports.comports())
print(plist)
if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 115200, timeout=6) #波特率设为115200
    s = serialFd
    print("可用端口名>>>", serialFd.name)


print('进入配置模式')
print('>>>2a2d2e')
Hex_str1 = bytes.fromhex('2A 2D 2E')  # 文本转换Hex 进入配置模式
s.write(Hex_str1)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出
    if data == data1:
        print('成功进入配置模式')

print('读取设备类型')
print('>>>fe0101ff')
Hex_str2 = bytes.fromhex('FE 01 01 FF')  # 文本转换Hex 读取设备类型
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出
#time.sleep(1)

print('读取PAN_ID')
print('>>>fe0203ff')
Hex_str2 = bytes.fromhex('FE 02 03 FF')  # 文本转换Hex 读取PAN_ID
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出

print('读取本机MAC地址')
print('>>>fe0806ff')
Hex_str2 = bytes.fromhex('FE 08 06 FF')  # 文本转换Hex 读取PAN_ID
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出

print('读取网络状态')
print('>>>fe0102ff')
Hex_str2 = bytes.fromhex('FE 01 02 FF')  # 文本转换Hex 读取PAN_ID
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出

print('读取波特率')
print('>>>fe010cff')
Hex_str2 = bytes.fromhex('FE 01 0C FF')  # 文本转换Hex 读取PAN_ID
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出

print('退出配置模式，进入传输模式')
print('>>>2f2c2b')
Hex_str2 = bytes.fromhex('2F 2C 2B')  # 文本转换Hex 退出配置模式，进入传输模式
s.write(Hex_str2)  # 串口发送 Hex_str()
time.sleep(0.2)
n = s.inWaiting()  # 串口接收
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
    print('<<<'+data)  # 字符串输出
    if data == data2:
        print('成功退出配置模式，进入传输模式')

while True:

    # 接收
    n = s.inWaiting()  # 串口接收
    if n:
        data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
        print('<<<'+data)  # 字符串输出
