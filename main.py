import serial
import time  # 延时使用
import binascii
import serial.tools.list_ports

data1 = '7a7d7e'
data2 = '7f7c7b'

#查看可用端口并建立连接,如果端口数为1则自动建立连接，如果端口数大于1则需要手动输入端口号

plist = list(serial.tools.list_ports.comports()) #获取当前设备的所有COM端口
port_number = len(plist)

if port_number <= 0:
    print("没有发现端口!")
elif port_number == 1:
    print('可用端口数为:1')
    print('可用端口号>>>' + plist[0][0])
    s = serial.Serial(plist[0][0], 115200, timeout=6)
else:
    print('可用端口数为'+str(port_number))
    for i in range(0, len(plist)):
        print('可用端口号>>>'+plist[i][0])        #打印所有可用的端口号
    Get_Port_Number = input('请输入连接的端口号：')
    s = serial.Serial(Get_Port_Number, 115200, timeout=6)


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