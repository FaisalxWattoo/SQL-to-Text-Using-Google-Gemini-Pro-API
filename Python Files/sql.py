import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
GRADE VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Faisal Riaz','Data Engineering','B+','90')''')
cursor.execute('''Insert Into STUDENT values('Muhammad Waqas','Web Developer','A','100')''')
cursor.execute('''Insert Into STUDENT values('Naveed Riaz','Web Development','B','80')''')
cursor.execute('''Insert Into STUDENT values('Waheed Ahmad','Data Analytics','A+','100')''')
cursor.execute('''Insert Into STUDENT values('Muhammad Idrees','AI Engineer','B+','75')''')
cursor.execute('''Insert Into STUDENT values('Muhammad Saqib','Data Engineering','B','70')''')
cursor.execute('''Insert Into STUDENT values('Ali Raza','Computer Science','B+','85')''')
cursor.execute('''Insert Into STUDENT values('Ahmad Nawaz','Cyber Security','A','98')''')
cursor.execute('''Insert Into STUDENT values('Faizan Khan','Machine Learning','B','82')''')
cursor.execute('''Insert Into STUDENT values('Rashid Ali','Data Science','A+','92')''')
cursor.execute('''Insert Into STUDENT values('Hassan Ali','Web Development','B+','88')''')
cursor.execute('''Insert Into STUDENT values('Zahid iqbal','Database Management','A','95')''')
cursor.execute('''Insert Into STUDENT values('Muhammad Shahid','Networking','B','80')''')
cursor.execute('''Insert Into STUDENT values('Aadil Khan','Artificial Intelligence','A+','99')''')
cursor.execute('''Insert Into STUDENT values('Imran Ahmad','Computer Networks','B+','86')''')
cursor.execute('''Insert Into STUDENT values('Sajid Khan','Information Security','A','96')''')
cursor.execute('''Insert Into STUDENT values('Wahab Ali','Software Engineering','B','83')''')
cursor.execute('''Insert Into STUDENT values('Ahmed Hasan','Data Analysis','A+','90')''')
cursor.execute('''Insert Into STUDENT values('Zain-ul-Abideen','Web Designing','B+','84')''')
cursor.execute('''Insert Into STUDENT values('Muhammad Uzair','Database Systems','A','91')''')
cursor.execute('''Insert Into STUDENT values('Imran Ullah','Computer Architecture','B','79')''')
cursor.execute('''Insert Into STUDENT values('Faheem Ud-Din','Algorithm Design','A+','98')''')
cursor.execute('''Insert Into STUDENT values('Faisal Mehmood','Data Structures','B+','85')''')
cursor.execute('''Insert Into STUDENT values('Syed Umer','Computer Vision','A','94')''')
cursor.execute('''Insert Into STUDENT values('Haroon Rasheed','Machine Learning Algorithms','B','81')''')
cursor.execute('''Insert Into STUDENT values('Rana Muhammad Umer','Human-Computer Interaction','A+','97')''')
cursor.execute('''Insert Into STUDENT values('Shafique Ahmad','Network Security','B+','87')''')
cursor.execute('''Insert Into STUDENT values('Kashif Mehmood','Computer Communications','A','93')''')
cursor.execute('''Insert Into STUDENT values('Kamran Ahmad','Data Mining','B','78')''')
cursor.execute('''Insert Into STUDENT values('Tayyab Riaz','Database Administration','A+','99')''')
cursor.execute('''Insert Into STUDENT values('Asad Shehzad','Image Processing','B+','89')''')
cursor.execute('''Insert Into STUDENT values('Umair Khalid','Software Project Management','A','95')''')
cursor.execute('''Insert Into STUDENT values('Hassan Ali Shah','Network Administration','B','77')''')
cursor.execute('''Insert Into STUDENT values('Rao Muhammad Abdullah','Digital Logic Design','A+','96')''')
cursor.execute('''Insert Into STUDENT values('Asad Rehman Khan','Pattern Recognition','B+','88')''')
cursor.execute('''Insert Into STUDENT values('Saleem Ullah','Artificial Neural Networks','A','90')''')
cursor.execute('''Insert Into STUDENT values('Jameel Ud-Din','Automata Theory','B','75')''')
cursor.execute('''Insert Into STUDENT values('Mohammad Ali','Data Warehousing','A+','97')''')
cursor.execute('''Insert Into STUDENT values('Syed Husnain Raza','Web Programming','B+','86')''')
cursor.execute('''Insert Into STUDENT values('Aslam Pervez','Expert Systems','A','94')''')
cursor.execute('''Insert Into STUDENT values('Abdul Rehman','Decision Support Systems','B','76')''')
cursor.execute('''Insert Into STUDENT values('Javed Iqbal','Software Quality Assurance','A+','96')''')
cursor.execute('''Insert Into STUDENT values('Nasir Ud-Din','Information Systems','B+','87')''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()