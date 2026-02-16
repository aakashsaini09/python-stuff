import sqlite3
conn = sqlite3.connect("yt_manager.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
        )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("*" * 50)
    for row in cursor.fetchall():
        print(row)
def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
def update_videos(vid_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, vid_id))
    conn.commit()
def delete_videos(id):
    cursor.execute("DELETE FROM videos where id = ?", (id,))
    conn.commit()
def load_videos():
    pass
def main():
    videos = load_videos()
    while True:
        print("\n Youtube Manager with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exot App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
            print("Video added.")
        elif choice == '3':
            list_videos()
            vid_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(vid_id, name, time)
            print("Video updated.")
        elif choice == '4':
            list_videos()
            vid_id = input("Enter video ID to delete: ")
            delete_videos(vid_id)
            print("Video deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, Please select the correct choice.")
    conn.close()
if __name__ == "__main__":
    main()