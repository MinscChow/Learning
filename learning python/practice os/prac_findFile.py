import os


s=input('please input the string that needs to find:')

def fff(path):
    oblist=os.listdir(path)
    x=[x for i,x in enumerate(oblist) if x.find(s) != -1]
    for o in x:
        if os.path.isfile(o):
            print(os.path.join(path,o))
        elif os.path.isdir(o):
            o=os.path.join(path,o)
            fff(o)

fff('.')
