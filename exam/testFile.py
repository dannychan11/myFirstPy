#
# try :
#     with open('aaa.txt', 'r+',encoding='utf-8') as files:
#         print(files)
#         i = 1
#         for line in files:
#             print('这是第%s行，数据内容是%s' % (i, line))
#             i += 1
#             print(files.writable())
# except FileNotFoundError as e :
#     print(e)
#     print('一1场了')
# except Exception as e :
#     print(e)
#     print('一场了')
# else:
#     print('每捕获到')
# finally:
#     print('jieshule')
import  time
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(str(1)+str(1))