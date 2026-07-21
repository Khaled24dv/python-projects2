import sqlite3

#create database and connect
db =sqlite3.connect("app1.db")
# setting up the cursor
cr =db.cursor()

cr.execute("create table if not exists skills (name text ,progress integer , user_id integer )")

def commet_and_close():
    # save change 
    db.commit()
    # close database
    db.close()
    print("database is closed :")

# user id
uID = 1
input_massage = """
What do you want to do ?
"s" => show all skills 
"a" => add new skill
"d" => dalata a skill 
"u" => ubdate skill progress 
"q" => quit the app
choose option :
"""
# input option choose ;
user_input = input(input_massage).strip().lower()
# list option
option = ["s","a","d","u","q"]
# check option is exist or not 
if user_input in option:
    print(f"This Option Is Found {user_input}")
else:
    print(f"This Option Is Not Found {user_input}")

# define the method 

def show_skills():
    cr.execute("select * from skills ")
    res =cr.fetchall()
    print(f"the number of skills is {len(res)} ")
    
    if len(res)>0:
        print("showing skill and progress :")
    for row in res:
        print(f"skill => {row[0]},",end = " ")
        print(f"progress => {row[1]}%")
    commet_and_close()

def add_skill():
    skill =input("enter skill name  :").strip().capitalize()
  
    cr.execute(f"select from skills where  name = '{skill}' and user_id = '{uID}'")
    res = cr.fetchone()
    if skill ==None:
        print("this skill is not exist : and can be add this skill .")
        #skill = input("Write skill name :").strip().capitalize()
        progress = input("enter progress :").strip()
        cr.execute(f"insert into skills (name , progress , user_id)values('{skill}','{progress}','{uID}') ")
        print("skill and progress is added :")
        commet_and_close()
    else :
        print("this skill is exist : and cannot be add .")
        option = input("are you update this skill (yes or no)").strip()

        if option == "yes":
            skill = input("Write skill name :").strip().capitalize()
            #prog = input("enter progress :").strip()
            cr.execute(f"update skills set progress = '{progress}' where name = '{skill}' and user_id ='{uID}'")
        else:
            print("Ok .")
def delete_skill():
    sk =input("enter skill name is be deleted :")
  
    cr.execute(f"delete from skills where  name = '{sk}' and user_id = '{uID}'")
    
    commet_and_close()
def ubdate_skill():
    skill = input("Write skill name :").strip().capitalize()
    prog = input("enter progress :").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{skill}' and user_id ='{uID}'")
    
    commet_and_close()
def quit_app():
    print("quit the app ")

if user_input =="s":
    show_skills()
elif user_input== "a":
    add_skill()
elif user_input == "d":
    delete_skill()
elif user_input == "u":
    ubdate_skill()
elif user_input == "q":
    quit_app()
else:
    print("this option is not exist :")
