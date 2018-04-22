import threading
import time
import  multiprocessing

# def music(name,loop):
#     for i in range(loop):
#         print(' 听歌%s-----%s'%(name,time.ctime()))
#         time.sleep(1)
# def movie(name,loop):
#     for i in range(loop):
#         print('看定影%s-----%s'%(name,time.ctime()))
#         time.sleep(1)
# t1=threading.Thread(target=music,args=('爱的誓言',5),name='bbb')
# t2=threading.Thread(target=movie, args=('异形3', 5),name='aaa')
# if __name__=='__main__':
#     # music('爱的誓言',5)
#     # movie('异形3',5)
#     t1.start()
#     t2.start()
#     t2.join()
#     print('主线程:%s'%time.ctime())

'''
加线程锁
'''
balance=0
def change(n):
    global balance
    balance+=n
    balance-=n

#lock1 = threading.Lock()
def run_thread(n,lock3):
    for i in range(10):
        #获取锁
        lock3.acquire()
        change(n)
        lock3.release()

# t1=threading.Thread(target=run_thread,args=(5,),name='bbb')
# t2=threading.Thread(target=run_thread, args=(8,),name='aaa')
# if __name__=='__main__':
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(balance)
lock2=multiprocessing.Lock()
p1 = multiprocessing.Process(target=run_thread,args=(5,lock2),name='bbb')
p2 = multiprocessing.Process(target=run_thread,args=(5,lock2),name='aaa')
if __name__=='__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(balance)