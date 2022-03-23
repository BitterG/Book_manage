# -*- coding:utf-8- -*-
"""
作者：苦瓜
日期：2022年03月16日
"""
import pymysql

class BM(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='Book',
                                     charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        self.connection.close()

    def execute_sql(self, sql, field):
        # 执行指定数字mysql语句
        self.cursor.execute(sql)
        # print(self.cursor.fetchall())
        for temp in self.cursor.fetchall():
            print(temp.get(field))

    def show_cates(self):
        """展示图书分类"""
        sql = "select distinct Book_cate from map;"
        field = 'Book_cate'
        self.execute_sql(sql, field)

    def show_author(self):
        """展示作者"""
        sql = "select distinct Book_author from map;"
        field = 'Book_author'
        self.execute_sql(sql, field)

    def show_inf(self):
        """根据文字查询"""
        sql = "select * from map where Book_name like '%{}%';".format(self.num)
        self.cursor.execute(sql)
        temp = self.cursor.fetchall()
        if temp != 0:
            for i in temp:
                print(i.get('Book_name'), "书籍UID:{}".format(i.get('Book_id')))
        else:
            print("无结果")

    def Decorate(self):
        """装饰分割"""
        print("=+=+=+=+=查询结果=+=+=+=+=")

    def print_menu(self):
        """登陆后显示的菜单"""
        print("+=+=+=+图书系统+=+=+=+")
        print("1:查询所有图书分类")
        print("2:查询所有书籍作者")
        print("3:进入借书模式")
        print("4:进入还书模式")
        print("4:退出系统")
        return input("请输入功能数字或书籍名称进行查询:")

    def print_borrow_menu(self):
        """借用菜单"""
        print("=+=+=+=+=借用模式=+=+=+=+=")
        print("exit:返回上一层")
        print("借用输入书籍ID:")
        self.BID = input("请输入:")
        return self.BID

    def sure_borrew(self):
        """确认借用菜单"""
        print("1:确认借书")
        print("2:取消借书")
        return input("请输入:")

    def un_borrow(self):
        """还书函数"""
        print("1:查询已借用书籍")
        print("2:输入订单号还书")
        return input("请输入:")

    def id_un_borrow(self):
        """订单号还书"""
        return input("请输入订单号:")

    def start_menu(self):
        """启动初始菜单"""
        print("1:注册账号")
        print("2.登录账号")
        print("3:退出系统")
        return input("请输入:")

    def register(self):
        self.account = input("请输入用户名:")
        self.password = input("请输入密码:")
        self.confirm_password = input("请输入确认密码:")
        return self.account, self.password, self.confirm_password

    def register_2(self):
        self.phone = input("请输入电话号码:")
        self.address = input("请输入地址:")
        return self.phone, self.address

    def add_register_inf(self):
        sql = "insert into user values (0, '{}', now(), {}, '{}', {});".format(self.account, self.phone
                                                                               , self.address, self.confirm_password)
        self.cursor.execute(sql)
        self.connection.commit()
        # insert into user values (0, '测试账号', now(), 13488888888, '这是一个地址', 12345678912);
        print("恭喜你个吊毛注册成功")
        sql = "select User_id from user where User_phone={};".format(self.phone)
        self.cursor.execute(sql)
        print_uid = self.cursor.fetchall()[0].get("User_id")
        print("您的UID为:{}请牢记，之后将使用UID登录".format(print_uid))

    def login(self):
        self.user_id = input("请输入登录ID:")
        self.login_password = input("请输入登录密码:")
        return self.user_id, self.login_password

    def run(self):
        while True:
            self.num = self.start_menu()
            if self.num == "1":
                # 进入注册
                self.register()
                if len(self.password) < 11 and self.password == self.confirm_password and \
                        len(self.password) != 0 and self.password != " " and len(self.account) < 6:
                    '''判断两次输入密码一致，及其长度限制，用户名长度'''
                    self.register_2()
                    if len(self.phone) != 0 and len(self.phone) < 12 and \
                            len(self.address) != 0 and self.address != " " and len(self.address) < 30:
                        '''判断电话及其地址是否符合规范'''
                        sc_phone = "select * from user where User_phone={};".format(self.phone)
                        self.cursor.execute(sc_phone)
                        if self.cursor.fetchall() != 0:
                            print("该手机号已被注册，请更换其他手机号完成注册")
                            continue
                        else:
                            self.add_register_inf()
                    else:
                        print("填写内容不符合规范,请重新填写")
                        continue
                else:
                    print("填写内容不符合规范,请重新填写")
                    continue
            elif self.num == "2":
                # 进入登录
                self.login()
                sql = "select User_password from user where User_id={};".format(self.user_id)
                self.cursor.execute(sql)
                password = self.cursor.fetchall()
                if len(password) != 0 and password[0].get("User_password") == self.login_password:
                    print("登录成功！")
                else:
                    print("账号密码不匹配,登陆失败,请重新输入")
                    continue
            elif self.num == "3":
                # 退出
                print("退出")
                break
            else:
                print("请重新输入")
                continue

            self.num = self.print_menu()
            if self.num == "1":
                # 查询图书分类
                self.Decorate()
                self.show_cates()
            elif self.num == "2":
                # 查询书籍作者
                self.Decorate()
                self.show_author()
            elif self.num == "3":
                # 借书模式
                while True:
                    self.num = self.print_borrow_menu()
                    if self.num == "exit":
                        break
                    else:
                        # 输入书籍ID
                        sql = "select * from map where Book_id='{}';".format(self.num)  # 获取输入ID书籍数据
                        self.cursor.execute(sql)
                        content = self.cursor.fetchall()
                        if len(content) == 0:   # 判断剩余书籍数量
                            print("该书籍不存在，请重新搜索")
                        elif content[0].get("Book_quantity") > 0:
                            print("书籍名称:{}\t作者:{}\t==数量充足==".format(content[0].get("Book_name"),
                                                                    content[0].get("Book_author")))
                            self.num = self.sure_borrew()
                            if self.num == "1":     # 确认借书
                                self.cursor.execute("select count(*) from borrow where User_id={}".format(self.user_id))
                                # 用户确认借书    # 未写确认借用的部分的函数
                                borrow_num = self.cursor.fetchall()[0].get("count(*)")
                                print(borrow_num)
                                if borrow_num < 3:
                                    self.cursor.execute("select * from user where User_id={};".format(self.user_id))
                                    content2 = self.cursor.fetchall()[0]
                                    sql = "insert into borrow values ({}, '{}', {}, '{}', now(), {}, 0);"\
                                        .format(self.BID, content[0].get("Book_name"), self.user_id, content2.
                                                get("User_name"), content2.get("User_phone"), 0)
                                    self.cursor.execute(sql)
                                    self.connection.commit()
                                    sql = "update map set Book_quantity={} where Book_id={};".\
                                        format(content[0].get("Book_quantity")-1, self.BID)
                                    self.cursor.execute(sql)
                                    self.connection.commit()
                                    print("借阅成功!")
                                else:
                                    print("借书失败，借用书籍数量上限")
                                    continue
                            elif self.num == "2":
                                print("取消借书成功")
                                break
                        else:
                            print("图书数量不足")
            elif self.num == "4":
                # 还书模式
                while True:
                    print("========还书模式========")
                    self.num = self.un_borrow()
                    if self.num == '1':   # 查询已借用书籍
                        sql = "select * from borrow where User_id={}".format(self.user_id)
                        self.cursor.execute(sql)
                        inf = self.cursor.fetchall()
                        for element in inf:
                            print("书籍名称:{}\t书籍ID:{}\t订单编号:{}".format(
                                element.get("Book_name"), element.get("Book_id"), element.get("Borrow_id")))
                    elif self.num == '2':   # 进入 序号还书模式
                        self.num = self.id_un_borrow()
                        sql = "select * from borrow where Borrow_id={}".format(self.num)
                        self.cursor.execute(sql)
                        inf2 = self.cursor.fetchall()
                        if inf2 == 0:
                            print("未查询到该订单")
                            continue
                        else:
                            sql = "delete from borrow where Borrow_id={}".format(self.num)
                            self.cursor.execute(sql)
                            self.connection.commit()
                            sql = "select Book_quantity from map where Book_id={}".format(inf2[0].get("Book_id"))
                            self.cursor.execute(sql)
                            inf3 = self.cursor.fetchall()
                            sql = "update map set Book_quantity={} where Book_id={};".format(
                                inf3[0].get("Book_quantity") + 1, inf2[0].get("Book_id"))
                            self.cursor.execute(sql)
                            self.connection.commit()
                            print("已成功还书,欢迎下次光临")
                    else:
                        print("输入有误请重新输入")
                        continue
            elif self.num == "5":
                # 退出查询
                print("+=+=+=+已退出系统+=+=+=+")
                break
            else:
                # 根据文字查询
                self.Decorate()
                self.show_inf()

def main():
    # 1.创建图书管理对象
    Book_manage = BM()
    # 2.调用对象run方法，运行
    Book_manage.run()

if __name__ == "__main__":
    main()