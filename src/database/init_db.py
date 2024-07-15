from pymongo import MongoClient


def get_database():

    client = MongoClient("mongodb://localhost:27017/")

    db_name = "library_db"

    db_list = client.list_database_names()
    if db_name in db_list:
        print(f"Database '{db_name}' already exist.")
    else:

        db = client[db_name]
        db.create_collection("books")
        db.create_collection("users")
        db.create_collection("loans")
        print(f"Database '{db_name}' was created successfully.")

    return client[db_name]


if __name__ == "__main__":
    get_database()
