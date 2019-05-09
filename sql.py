import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor();
    c.execute("CREATE TABLE posts(title TEXT, desc TEXT)")
    c.execute('INSERT INTO posts VALUES("Good","I am a good human")')
    c.execute('INSERT INTO posts VALUES("bad","I am a bad human")')
