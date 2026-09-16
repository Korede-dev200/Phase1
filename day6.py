import sqlite3


conn = sqlite3.connect("school.db")
cur = conn.cursor()

print("Connected")

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade_level INTEGER
)
""")

print("Table created")

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

#---cur.execute("""
#INSERT INTO students (id, name, grade_level) VALUES
 #   (1, 'Ama', 10),
  #  (2, 'Ben', 11),
   # (3, 'Chidi', 10),
    #(4, 'Dara', 11),
    #(5, 'Eze', 10)
#""")

conn.commit()
print("Inserted")

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.execute("DROP TABLE IF EXISTS enrollments")

cur.execute("""
CREATE TABLE enrollments(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    score INTEGER
)
""")

cur.execute("SELECT name FROM  sqlite_master WHERE type='table'")
print(cur.fetchall())

cur.execute("PRAGMA table_info(enrollments)")
for col in cur.fetchall():
    print(col)

cur.execute("""
INSERT INTO enrollments (student_id, subject, score) VALUES
    (1, 'Math', 78),
    (1, 'Science', 85),
    (2, 'Math', 92),
    (3, 'Science', 65),
    (3, 'Math', 70),
    (4, 'Science', 88)
""")

conn.commit()
print("Enrollments inserted")

cur.execute("SELECT * FROM enrollments")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT enrollments.score FROM enrollments WHERE enrollments.score > 80")
scores = cur.fetchall()
for score in scores:
    print(score)

cur.execute("SELECT students.name, enrollments.score FROM  students JOIN enrollments ON students.id = enrollments.student_id ")  
print(cur.fetchall())

cur.execute("SELECT students.name, enrollments.score FROM  students LEFT JOIN enrollments ON students.id = enrollments.student_id ")  
print(cur.fetchall())


import pandas as pd


query = """
SELECT students.name, students.grade_level, enrollments.subject, enrollments.score
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
"""

df = pd.read_sql_query(query, conn)
print(df)

print(df.groupby("name")["score"].mean())



df["passed"] = df["score"] >= 70
print(df)

subject_avg = df.groupby("name")["score"].mean()
print(subject_avg)
print(subject_avg.idxmax())

df["passed"] = (df["score"] >= 70)
df["passed"] = df["passed"].astype(object)
df.loc[df["score"].isna(), "passed"] = None
print(df)

df.to_csv("students_report.csv", index=False)
print("Saved")