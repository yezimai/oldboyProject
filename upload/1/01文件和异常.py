#python 高级专题

#教学监督热线：400-1567-315

#1.文件
path = r'C:\Users\不动\Desktop\基础班代码\06高级专题\test.txt'
file = open(path,'w',encoding = 'utf8')
file.write('aaaaa')
file.close()  #关闭文件
file = open(path,'w',encoding = 'utf8')
file.flush()
a = ['人生苦短，我用python','\n','python是最好的编程语言','测试']

file.write(a[0] + '\n')
file.writelines(a)
file.close()

file = open(path,'r',encoding = 'utf8')
file.read()
file.seek(0,0)
file.readline()
file.readlines()


file.closed
file.mode
file.name
file.close()

with open(path,'r',encoding = 'utf8') as f:
    #print(f.read())
    pass

#异常

try:
    print('111')
    #file = open(path,'w',encoding = 'utf8')
    e = 'aaaaa'
    raise Exception(e)
    #f2 = open('super.txt','r')
    print('222')
##except Exception:
##    print('错误')    
except FileNotFoundError:
    print('文件错误')
except Exception as e:
    print('错误:',e)
else:
    print('打开文件成功')
finally:
    file.close()
    print('关闭成功')


def fun(x,y): #计算乘积
    #assert type(x) in (tuple,set)   #断言  后面为假的时候报错  AssertionError
    try:
        return x*y
    except TypeError:
        print('传入参数有误')























