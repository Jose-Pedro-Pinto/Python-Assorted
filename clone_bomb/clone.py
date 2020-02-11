import importlib
maxim=100
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def run():
    y=1
    string=""
    while True:
        x=__name__[len(__name__)-y]
        if not RepresentsInt(x):
            break
        string=str(x)+string
        y+=1
    x=__name__[len(__name__)-1]
    if x=="_":
        file1 = open("clone.py","r")
        buffer=file1.read()
        file2 = open("clone1.py","w")
        file2.write(buffer)
        file1.close()
        file2.close()
    else:
        if int(x)>=maxim:
            return
        file1 = open("clone"+string+".py","r")
        buffer=file1.read()
        file2 = open("clone"+str(int(string)+1)+".py","w")
        file2.write(buffer)
        file1.close()
        file2.close()
if __name__=='__main__':
    run()
    import clone1
    clone1.run()
else:
    run()
    y=1
    string=""
    while True:
        x=__name__[len(__name__)-y]
        if not RepresentsInt(x):
            break
        string=str(x)+string
        y+=1
    if int(string)+1<maxim:
        x=importlib.import_module("clone"+str(int(string)+1)+".py")
        x.run()
