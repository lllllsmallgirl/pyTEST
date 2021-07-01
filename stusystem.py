import os
filename='student.txt'
def main():
    while True:
        menm()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer=input('您确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break     #退出系统
                else:
                    continue
            elif choice==1:
                insert()    #录入学生信息
            elif choice==2:
                search()    #查找学生信息
            elif choice==3:
                deletel()   #删除学生信息
            elif choice==4:
                modify()    #修改学生信息
            elif choice==5:
                sort()      #排序
            elif choice==6:
                total()     #统计学生总人数
            elif choice==7:
                show()      #显示所有的学生信息

def menm():
    print('================================学生信息管理系统==========================================')
    print('------------------------------------功能菜单---------------------------------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有的学生信息')
    print('\t\t\t\t0.退出')
    print('-----------------------------------------------------------------------------------------')
def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如1001）：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩'))
            python=int(input('请输入python成绩'))
            java=int(input('请输入Java成绩'))
        except:
            print('输入错误，不是整数类型，请重新输入')
            continue
        #将录入的学生信息添加到列表中 
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y':
            continue
        if answer=='n':
            break
    #调用save函数
    save(student_list)
    print('学生信息录入完毕！！！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():  
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按学号查找请输入1，按姓名查找请输入2:')
            if mode=='1':
                id=input('请输入查找学生的ID：')
            elif mode=='2':
                name=input('请输入查找学生的姓名')
            else:
                print('输入错误请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student_old=rfile.readlines()
                for item in student_old:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            show()
        else:
            print('暂未存放信息')
        answer=input('是否继续查找学生信息？y/n\n')
        if answer=='y':
            search()
        else:                                        
            break

def deletel():
    while True:
        student_id=input('请输入要删除的学生的ID')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                   student_old=file.readlines()  
            else:
                student_old=[]  
            flag=False  #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))  #将字符串转成字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print('id为',student_id,'的学生信息已被删除')
                    else:
                        print('没有找到id为',student_id,'的学生信息')
            else:
                print('无学生信息')
                break
            show()       #删除后要重新显示所有学生信息
            answer=input('是否要继续删除？y/n\n')
            if answer=='y':
                continue
            else:
                break

def modify():
   show()
   while True:
       if os.path.exists(filename):
           with open(filename,'r',encoding='utf-8') as rfile:
               student_old=rfile.readlines()
       else:
           return
       student_id=input('请输入要修改学生的ID：')
       with open(filename,'w',encoding='utf-8') as wfile:
        flag=True
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息')
                try:
                    d['name']=int(input('请输入学生姓名'))
                    d['english']=int(input('请输入英语成绩'))
                    d['python']=int(input('请输入python成绩'))
                    d['java']=int(input('请输入java成绩'))
                except:
                    print('你的输入有误，请重新输入')
                    continue
                wfile.write(str(d)+'\n')
                print('修改成功')
                flag=False
            else:
                wfile.write(str(d)+'\n')
        if flag:
            print('没有找到id为',student_id,'的学生信息')
       answer=input('是否继续修改学生信息？y/n')
       if answer=='y':
           modify()
       else:
            break

def sort():
    pass

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
            if student_old:
                print('一共有{0}个学生'.format(len(student_old)))
            else:
                print('学生信息还未录入')
    else:
        print('暂未保存数据信息')

def show():
    pass
if __name__=='__main__':
    main()