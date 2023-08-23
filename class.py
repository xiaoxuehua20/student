# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Student:
    def __init__(self,name,ID,age):
        self.name = name
        self.ID = ID
        self.age = age
        self.groud = {}

    def set_groud(self,subject,groud):
        self.groud[subject] = groud
        
goin_system = input('是否进入系统(y/n) ')
while goin_system =='y':
    print('-------------------------------------------')
    print('欢迎进入系统')
    
    
    f = open('Student.txt','r',encoding='utf-8')
    read_1 = f.readline()
    z = {}                                          #打开文件   转为字典
    while read_1 != '':
        read_2 = eval(read_1.replace("\n",''))
        z = z | read_2     
        dict_1 = z                                                #dict_1为最终结果
        
        read_1 = f.readline()
    f.close()
    
    

    chooth = input('查看、创建、更改或删除学生信息(a/b/c/d) ')
    print('')                                           #查看
    if chooth == 'a':
        name_input = input('请输入学生名 ')
        if name_input in dict_1:
            
            select_1 = input('查询ID还是成绩 (i/g) ')
            if select_1 == 'i':
                print('ID为: '+str(dict_1[name_input]['ID']))
            elif select_1 == 'g':
                print('该学生成绩为: '+str(dict_1[name_input]['groud']))
                
        else:
            print('学生名不存在')
            
    
    
    elif chooth == 'b':                                 #创建
        print('请完成学生基本信息设置')
    
        name_ask = input('请输入学生名 ')
        ID_ask = input('请输入学生ID ')
        age_ask = input('请输入学生年龄 ')
        cheng = Student(name_ask,ID_ask,age_ask)

        print('接下来进行科目设置')
        subject_ask = input('请输入科目 ')
        result_ask = input('请输入该科目成绩 ')
        end_ask = input("结束请输入'q',未结束请输入'enter' ")
        cheng.set_groud(subject_ask,result_ask)
        while end_ask != 'q':
            subject_ask = input('请输入科目 ')
            result_ask = input('请输入该科目成绩 ')
            end_ask = input("结束请输入'q',未结束请输入'enter' ")
            cheng.set_groud(subject_ask,result_ask)
            
        print('')    
        print('学生名: '+cheng.name+'\n'+'ID: '+cheng.ID+'\n'+'年龄: '+cheng.age)
        print('成绩: '+str(cheng.groud))
        save = input('是否保存以上信息(y/n) ')
        if save == 'y':
            f = open('Student.txt','a',encoding='utf-8')
            write_1 = {cheng.name:{'ID':cheng.ID,'groud':cheng.groud}}
            f.write(str(write_1)+'\n')
            f.close()
            print('已保存以上信息')
            print('请记住名称和ID')
            
    elif chooth == 'c':                                     #更改
        name_input = input('请输入学生名 ')
        if name_input in dict_1: 
            ID_input = input('为保证安全,请输入该学生ID ')
            if ID_input == dict_1[name_input]["ID"]:
                change_ask = input('更改成绩ID (s/i) ')
                if change_ask == 'i':  
                    ID_nwe = input('请输入新ID ')
                    dict_ID = dict_1
                    dict_ID[name_input]['ID'] = ID_nwe
                    with open('Student.txt','w',encoding='utf-8') as f:
                        f.write('')
                    f = open('Student.txt','a',encoding='utf-8')
                    for key,valbe in dict_ID.items():
                        dict_2 = {}
                        dict_2[key] = valbe
                        f.write(str(dict_2)+'\n')
                    f.close()
                elif change_ask == 's':
                    subject_2 = input('请输入科目 ')
                    if subject_2 in dict_1[name_input]['groud']:                       
                        subject_1 = input('更改科目成绩或删除该科目 (c/d) ')
                        if subject_1 == 'c':
                            subject_groud = input('请输入该科目成绩 ')
                            dict_subject = dict_1                                          #获取
                            dict_subject[name_input]['groud'][subject_2] = subject_groud
                            
                            with open('Student.txt','w',encoding='utf-8') as f:
                                f.write('')
                            f = open('Student.txt','a',encoding='utf-8')
                            for key,valbe in dict_subject.items():
                                dict_2 = {}                                                  #写入
                                dict_2[key] = valbe
                                f.write(str(dict_2)+'\n')
                            f.close()
                        
                        elif subject_1 == 'd':
                            y_n = input('是否删除 (y/n) ')
                            if y_n == 'y':
                                dict_groud = dict_1
                                del dict_groud[name_input]['groud'][subject_2]
                                with open('Student.txt','w',encoding='utf-8') as f:
                                    f.write('')
                                f = open('Student.txt','a',encoding='utf-8')
                                for key,valbe in dict_groud.items():
                                    dict_2 = {}                                                  #写入
                                    dict_2[key] = valbe
                                    f.write(str(dict_2)+'\n')
                                f.close()
                                print('已删除')
                            elif y_n == 'n':
                                print('操作结束')
                            else:
                                print('请按提示操作')
                        else:
                            print('请按提示操作')
                    else:
                        print('科目不存在')
                else:
                    print('请按提示操作')
            else:
                print('学生名或ID不正确')
        else:
            print('学生名或ID不正确')
        
    
    elif chooth == 'd':             #删除
        name_input = input('请输入学生名 ')
        if name_input in dict_1: 
            ID_input = input('为保证安全,请输入该学生ID ')
            if ID_input == dict_1[name_input]["ID"]:
                chooth_input = input('是否确认删除该学生的所有信息 (y/n) ')
                if chooth_input == 'y':
                    
                    dict_3 = dict_1
                    del dict_3[name_input]
                    with open('Student.txt','w',encoding='utf-8') as f:
                        f.write('')
                    f = open('Student.txt','a',encoding='utf-8')
                    for key,valbe in dict_3.items():
                        dict_2 = {}                                                  #写入
                        dict_2[key] = valbe
                        f.write(str(dict_2)+'\n')
                    f.close()
                    print('已删除')
                else:
                    print('已退出')
            else:
                print('学生名或ID不正确')
            
        else:
            print('学生名或ID不正确')
    else:
        print('请按提示字母输入')
            
    
            
    goin_system = input('\n是否退出系统(n/y) ')

print('')    
print('欢迎下次光临')