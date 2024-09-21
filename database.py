import mysql.connector
mydb = mysql.connector.connect(
user="root",
password="dimpu123",
database="demo9"
)
c = mydb.cursor()
def create_tables():
    c.execute('create table IF NOT EXISTS user_details(user_no varchar(56) not null primary key, fname varchar(255) not null,lname varchar(255) not null, sex varchar(255), phone_no varchar(255), dob date,age int ,email varchar(255))')
    c.execute('create table IF NOT EXISTS product(user_no varchar(56) not null,prod_id varchar(56) primary key not null,name varchar(255) ,slot_booking_date date not null,need_it_by date not null, problem varchar(255) not null, foreign key (user_no) references user_details(user_no));')
    c.execute('create table IF NOT EXISTS services(user_no varchar(56) not null,prod_id varchar(56) not null,ser_no varchar(56) not null primary key, qty int(255), estimated_price int(255) not null, foreign key (user_no) references user_details(user_no), foreign key (prod_id) references product(prod_id));')
    c.execute('create table IF NOT EXISTS payment(user_no varchar(56) not null,prod_id varchar(56) not null,payment_no varchar(78) not null primary key,payment_type varchar(152) not null, total_price int(255) not null,foreign key (user_no) references user_details(user_no),foreign key (prod_id) references product(prod_id));')
    c.execute('create table IF NOT EXISTS employee(emp_no varchar(56) not null primary key, fname varchar(255) not null,lname varchar(255) not null, sex varchar(50),ser_no varchar(89) not null,foreign key (ser_no) references services(ser_no));')

def add_data_user(user_no , fname ,lname , sex , phone_no , dob, age ,email):
    c.execute("insert into user_details(user_no , fname ,lname , sex , phone_no , dob, age ,email) VALUES (%s, %s, %s, %s, %s, %s,%s, %s)", (user_no , fname ,lname , sex , phone_no , dob, age , email))
    mydb.commit()

def add_data_product(user_no,prod_id,name, slot_booking_date, need_it_by, problem):
    c.execute("insert into product (user_no,prod_id,name, slot_booking_date, need_it_by,problem ) VALUES (%s, %s, %s, %s, %s, %s)", (user_no,prod_id,name, slot_booking_date, need_it_by,problem))
    mydb.commit()

def add_data_service(user_no, prod_id,ser_no, qty,estimated_price):
    c.execute("insert into services(user_no, prod_id,ser_no, qty,estimated_price) VALUES (%s, %s, %s, %s, %s)", (user_no, prod_id,ser_no, qty,estimated_price))
    mydb.commit()

def add_data_employee(emp_no,fname,lname,sex,ser_no):
    c.execute("insert into employee (emp_no,fname,lname,sex,ser_no) VALUES (%s, %s, %s, %s, %s)", (emp_no,fname,lname,sex,ser_no))
    mydb.commit()

def add_data_payment(user_no,prod_id,payment_no,payment_type,total_price):
    c.execute("insert into payment(user_no,prod_id,payment_no,payment_type,total_price) VALUES (%s, %s, %s, %s, %s)", (user_no,prod_id,payment_no,payment_type,total_price))
    mydb.commit()

def view_all_data_user():
    c.execute('SELECT * FROM user_details')
    data = c.fetchall()
    return data

def view_all_data_prod_detail():
    c.execute('SELECT * FROM product ORDER BY slot_booking_date ASC')
    data = c.fetchall()
    return data

def view_all_data_service():
    c.execute('SELECT * FROM services')
    data = c.fetchall()
    return data

def view_all_data_employee():
    c.execute('SELECT * FROM employee')
    data = c.fetchall()
    return data

def view_all_data_payment():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data

def view_only_user_no():
    c.execute('SELECT user_no FROM user_details')
    data = c.fetchall()
    return data

def view_only_prod_id():
    c.execute('SELECT prod_id FROM product ')
    data = c.fetchall()
    return data

def view_only_service_id():
    c.execute('SELECT ser_no FROM services')
    data = c.fetchall()
    return data

def view_only_emp_no():
    c.execute('SELECT emp_no FROM employee')
    data = c.fetchall()
    return data

def view_only_payment_no():
    c.execute('SELECT payment_no FROM payment')
    data = c.fetchall()
    return data

def get_user(user_no):
    c.execute('SELECT * FROM user_details WHERE user_no="{}"'.format(user_no))
    data = c.fetchall()
    return data

def get_prod(selected_prod):
    c.execute('SELECT * FROM product WHERE prod_id="{}"'.format(selected_prod))
    data = c.fetchall()
    return data

def get_service(selected_service):
    c.execute('SELECT * FROM services WHERE ser_no="{}"'.format(selected_service))
    data = c.fetchall()
    return data

def get_employee(selected_employee):
    c.execute('SELECT * FROM employee WHERE emp_no="{}"'.format(selected_employee))
    data = c.fetchall()
    return data

def get_payment(selected_payment):
    c.execute('SELECT * FROM payment WHERE payment_no="{}"'.format(selected_payment))
    data = c.fetchall()
    return data

def edit_user_data(new_user_no, new_fname, new_lname, new_sex, new_phone_no,new_dob,new_age ,new_email,user_no, fname, lname, sex, phone_no, dob,age ,email):
    c.execute("UPDATE user_details set user_no = %s, fname=%s, lname=%s, sex=%s, phone_no=%s, dob=%s,age=%s ,email=%s where user_no=%s and fname=%s and  lname=%s and sex=%s and phone_no=%s and dob=%s and age=%s and email=%s", (new_user_no, new_fname, new_lname, new_sex, new_phone_no,new_dob,new_age,new_email, user_no, fname, lname, sex, phone_no, dob,age ,email))
    mydb.commit()
    return

def edit_prod_data(new_user_no,new_prod_id, new_name, new_slot_booking_date, new_need_it_by,new_problem,user_no,prod_id, name, slot_booking_date, need_it_by,problem):
    c.execute("UPDATE product set user_no=%s,prod_id=%s, name=%s, slot_booking_date=%s, need_it_by=%s,problem=%s where user_no=%s and prod_id=%s and name=%s and slot_booking_date=%s and need_it_by=%s and problem=%s", (new_user_no,new_prod_id, new_name, new_slot_booking_date, new_need_it_by,new_problem,user_no,prod_id, name, slot_booking_date, need_it_by,problem))
    mydb.commit()
    return

def edit_service_data(new_user_no, new_prod_id, new_ser_no, new_qty, new_estimated_price, user_no, prod_id, ser_no, qty, estimated_price):
    c.execute("UPDATE services set user_no=%s, prod_id=%s, ser_no=%s, qty=%s, estimated_price=%s where user_no=%s and prod_id=%s and ser_no=%s and qty=%s and estimated_price=%s", (new_user_no, new_prod_id, new_ser_no, new_qty, new_estimated_price, user_no, prod_id, ser_no, qty, estimated_price))
    mydb.commit()
    return

def edit_employee(new_emp_no, new_fname, new_lname, new_sex, new_ser_no, emp_no, fname, lname, sex, ser_no):
    c.execute("UPDATE employee set emp_no=%s, fname=%s, lname=%s, sex=%s, ser_no=%s where emp_no=%s and fname=%s and lname=%s and sex=%s and ser_no=%s ", (new_emp_no, new_fname, new_lname, new_sex, new_ser_no, emp_no, fname, lname, sex, ser_no))
    mydb.commit()
    return

def edit_payment(new_user_no, new_prod_id,new_payment_no,new_payment_type,new_total_price,user_no, prod_id, payment_no, payment_type, total_price):
    c.execute("UPDATE payment set user_no=%s, prod_id=%s, payment_no=%s, payment_type=%s, total_price=%s where user_no=%s and prod_id=%s and payment_no=%s and payment_type=%s and total_price=%s", (new_user_no, new_prod_id,new_payment_no,new_payment_type,new_total_price,user_no, prod_id, payment_no, payment_type, total_price))
    mydb.commit()
    return


def delete_user_db(selected_user):
    c.execute('DELETE FROM user_details WHERE user_no="{}"'.format(selected_user))
    mydb.commit()

def delete_prod_db(selected_prod):
    c.execute('DELETE FROM product WHERE prod_id="{}"'.format(selected_prod))
    mydb.commit()

def delete_service_db(selected_service):
    c.execute('DELETE FROM services WHERE ser_no="{}"'.format(selected_service))
    mydb.commit()

def delete_employee_db(selected_employee):
    c.execute('DELETE FROM employee WHERE emp_no="{}"'.format(selected_employee))
    mydb.commit()

def delete_payment_db(selected_payment):
    c.execute('DELETE FROM payment WHERE payment_no="{}"'.format(selected_payment))
    mydb.commit()


def custom_query(query):
    c.execute(query)
    data = c.fetchall()
    return data

