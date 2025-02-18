import mysql.connector, traceback
from datetime import datetime

#sandeep-codes-7
conn = mysql.connector.connect(
    host="localhost",   
    user="<user_name>",        
    password="<your-password>",  
    database="<database_name>"  
)

cursor = conn.cursor(buffered=True)

table_name="<your table name>"

def is_valid_date(date_string, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def check_id(table, id_value):
    q = f"SELECT exists(SELECT 1 FROM {table} WHERE id = %s)"
    cursor.execute(q, (id_value,))
    conn.commit()
    return cursor.fetchone()[0] == 1

def is_exist(task):
    q = f"SELECT exists(select 1 from todolist where task like %s)"
    #print(type(task))
    #v = f'%{task}%'
    cursor.execute(q, (task,))
    return cursor.fetchone()[0] == 1

def add_task():
    try:
        task = input("Enter task: ")
        date = input("Enter date(yyyy-mm-dd): ")
        status = False
        
        if task == '':
            print("Invalid!")
            return
        if not is_valid_date(date):
            print("Invalid date!")
            return
        else:
            q="insert into todolist(task,status,deadline) values(%s,%s,%s)"
            v=(task,status,date)
            cursor.execute(q,v)
            conn.commit()
            print("success!")
            
    except mysql.connector.Error as e:
        print("\nError occured!\n" + str(e) + '\n')
        #traceback.print_exc()
    

def view_task():
    try:
        cursor.execute("select * from todolist")
        rows = cursor.fetchall()
        print("id task status deadline")
        for i in rows:
            for j in i:
                print(j,end=', ' if i.index(j) != len(i)-1 else '')
            print()
        #cursor.close()
    except Exception as e:
        pass

def update_task():
    print("What to update?")
    user = input("id/task/status/deadline: ").lower()
    if 'id' in user:
        id_=int(input("Enter id: "))
        if check_id(table_name, id_):
            new_id = int(input("Enter new id: "))
            q=f"update {table_name} set id=%s where id=%s"
            v=(new_id,id_)
            cursor.execute(q,v)
            conn.commit()
            print("success!")
            return 'success'
        else:
            print("id not found!")
            return 'id not found'

    elif 'task' in user:
        task = input("Enter task: ")
        if is_exist(task):
            new_task = input("Enter new task: ")
            q=f"update {table_name} set task=%s where task=%s"
            v=(new_task,task)
            cursor.execute(q,v)
            conn.commit()
            print("success!")
            ans = input("wanna update deadline?(y/n): ").lower()
            if ans == 'y' or ans == 'yes':
                date = input("Enter deadline(yyyy-mm-dd): ")
                new_deadline = input("Enter new deadline(yyyy-mm-dd): ")
                q=f"update {table_name} set deadline=%s where id=%s"
                v=(new_deadline,13)
                cursor.execute(q,v)
                conn.commit()
                print("success!")
                return 'success!'
            else:
                print("updated!")
                return 'updated!'
        else:
            print("task not found!")
            return 'task not found'

    elif 'status' in user:
        task = input("Enter task: ")
        if is_exist(task):
            new_status = input("Enter new status(true/false): ").capitalize()
            if new_status == 'True' or new_status == 'False':
                q=f"update {table_name} set status=%s where task=%s"
                if new_status == 'True':
                    v=(True,task)
                else:
                    v=(False,task)
                cursor.execute(q,v)
                conn.commit()
                print("success!")
                return
        else:
            print("Invalid status!")

    elif 'deadline' in user:
        task = input("Enter task: ")
        if is_exist(task):
            new_deadline = input("Enter new deadline(yyyy-mm-dd): ")
            q=f"update {table_name} set deadline=%s where task=%s"
            v=(new_deadline,task)
            cursor.execute(q,v)
            conn.commit()
            print("success!")
            return 'success'
           
        else:
            print("deadline not found!")
            return 'deadline not found!'

    else:
        print("invalid option!")
        return
    
def mark_as_done():
    task = input("Enter task: ")
    if is_exist(task):
        q=f"update {table_name} set status=%s where task=%s"
        v=(True,task)
        cursor.execute(q,v)
        conn.commit()
        print("success!")
        return 'success!'
    else:
        print("task not found!")
        return 'task not found!'
    
def delete_task():
    task = input("Enter task: ")
    if is_exist(task):
        q=f"delete from {table_name} where task=%s"
        v=(task,)
        cursor.execute(q,v)
        conn.commit()
        print("success!")
        return 'success!'
    else:
        print("task not found!")
        return 'task not found!'
    
def delete_done_task():
    q=f"delete from {table_name} where status=%s"
    v=(True,)
    cursor.execute(q,v)
    conn.commit()
    print("success!")
    return 'success!'

def delete_all():
    user = input("are you sure?(y/n) ").lower()
    if user == 'y' or user == 'yes':
        q=f"truncate {table_name}"
        cursor.execute(q)
        conn.commit()
        print("success!")
        return 'success!'
    elif user == 'n' or user == 'no':
        print("deletion terminated!")
    else:
        return

    
#close
