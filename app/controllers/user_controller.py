def get_users():
    return [
        {"id": 1, "name": "Jigar Veera"},
        {"id": 2, "name": "Shubham Shukla"},
        {"id": 3, "name": "Rohit Dubey"},
        {"id": 4, "name": "Amey Yenpure"},
    ]

def create_user(name: str):
    return {
        "message": "User created",
        "name": name
    }