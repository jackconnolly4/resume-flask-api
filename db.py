import sqlite3




def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS students;
        """
    )
    conn.execute(
        """
   CREATE TABLE students (
 id INTEGER PRIMARY KEY,
        first_name TINYTEXT NOT NULL,
        last_name TINYTEXT NOT NULL,
        email TINYTEXT UNIQUE NOT NULL,
        phone_number TINYTEXT,
        short_bio TEXT,
        linkedin_url TINYTEXT,
        twitter_handle TINYTEXT,
        personal_url TINYTEXT,
        resume_url TINYTEXT,
        github_url TINYTEXT,
        photo TINYTEXT,
        password TINYTEXT NOT NULL
);
        """
    )
    conn.commit()
    print("Table created successfully")

    students_seed_data = [
     (
        "Steven", "Ungaro", "steven@test.com", "555-222-1234",
         "Blah blah blah blah...",  "stevenlinkedin.url", "@steventwitter",
        "steven.url", "stevenresume.url",  "stevengit.url",
         "https://freerangestock.com/sample/2230/childs-drawing-of-happy-face.jpg", "password1"
     ),
    ]
    conn.executemany(
        """
        INSERT INTO students (first_name, last_name, email, phone_number, short_bio, linkedin_url, twitter_handle, personal_url, resume_url, github_url, photo, password)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        students_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()
    

def students_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM students
        """
    ).fetchall()
    return [dict(row) for row in rows]