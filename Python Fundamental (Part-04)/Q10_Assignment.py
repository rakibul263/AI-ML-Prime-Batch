class User:
    def __init__(self, name):
        self.name = name

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined {self.room_name}")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.name} left {self.room_name}")

    def send_message(self, user, content):
        if user in self.users:
            self.messages.append(f"{user.name}: {content}")
            print(f"{user.name}: {content}")
        else:
            print(f"{user.name} is not in the chatroom!")

    def show_history(self):
        print(f"\n--- Chat History of {self.room_name} ---")
        for msg in self.messages:
            print(msg)
        print("--- End of History ---\n")

# Example usage
u1 = User("Rakibul")
u2 = User("Shuvo")

room = ChatRoom("Bachelor")
room.join(u1)
room.join(u2)

room.send_message(u1, "Hello Shuvo!")
room.send_message(u2, "Hi Rakibul!")
room.show_history()
room.leave(u1)
room.send_message(u1, "Am I still here?")
