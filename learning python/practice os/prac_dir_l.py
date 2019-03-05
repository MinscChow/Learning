
import os,time


#获取文件夹内所有文件大小
total_size=round(sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])/1024)


#获取文件夹下文件个数，只取一层
def numOfFile(path,num=1):
    try:
        if os.path.isdir(path):
            for x in os.listdir(path):
                num+=1
    except BaseException as e:
        pass
    finally:
        return num


#Permission属性区域的bit0~bit8，也即st_mode字段的最低9位，代表文件的许可权限，它标识了文件所有者（owner）、组用户（group）、其他用户（other）的读（r）、写（w）、执行（x）权限
#把二进制字符转换成权限码
def str2word(numstr):
    wordstr = ''
    words = ['r','w','x']
    for i ,x in enumerate(numstr):
        if x=='1':
            wordstr += (lambda i,words : words[ i % 3])(i,words)
        else:
            wordstr += '-'
    return wordstr

def listFile(path):
    print('total %d'%total_size)
    print('权限\t\t文件数\t用户\t群组\t大小\t月份\t日期\t时间\t文件名')
    for x in os.listdir(path):
        dir=os.path.join(path,x)
        stat=os.stat(dir)
        print('-'+str2word(str(bin(stat.st_mode)[-9:])),end='\t')
        print(numOfFile(dir),end='\t')
        uid=stat.st_uid
        with open('/etc/passwd','r') as f:
            flist=f.readlines()
        ug_index=[i for i,x in enumerate(flist) if x.find(str(uid)) != -1]
        ug = flist[ug_index[0]]
        user_name=ug.split(':')[0]
        group_name=ug.split(':')[4].split(',')[0]
        print(user_name,end='\t')
        print(group_name,end='\t')
        print(stat.st_size,end='\t')
        mtime=time.localtime(stat.st_mtime)
        print(str(mtime.tm_mon)+'月',end='\t')
        print(mtime.tm_mday,end='\t')
        print(str(mtime.tm_hour)+':'+str(mtime.tm_min),end='\t')
        print(x)

listFile('.')

