from datetime import datetime
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Registration:
    def __init__(self):
        self.users = []

    def Signup(self, username, password):
        for user in self.users:
            if username == user.username:
                return "User already exists"
        new_user = User(username, password)
        self.users.append(new_user)
        return "Registered successfully"

    def Login(self, user_name, user_password):
        for user in self.users:
            if user_name == user.username and user_password == user.password:
                return "Login successfully"

        return "Invalid username or password"
class Sender:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()
class Room:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.messages = []
    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
    
    def add_user(self, user):
        self.users[user.username] = user
    def send_message(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)

    def display_messages(self):
        for message in self.messages:
            print(f"[{message.timestamp}] {message.sender.username}: {message.content}")

class ChatSystem:
    def __init__(self):
        self.rooms = {}
    def create_room(self, room_name):
        if room_name not in self.rooms:
            self.rooms[room_name] = Room(room_name)
            print(f"Room '{room_name}' created successfully!")
        else:
            print(f"Room '{room_name}' already exists!")
    def join_room(self, user, room_name):
        room = self.rooms.get(room_name)
        if room:
            room.add_user(user)
            print(f"{user.username} joined '{room_name}' room.")
        else:
            print(f"Room '{room_name}' does not exist!")
    def exit_room(self, user, room_name):
        room = self.rooms.get(room_name)
        if room:
            room.remove_user(user.username)
            print(f"{user.username} exited '{room_name}' room.")
        else:
            print(f"Room '{room_name}' does not exist!")
    def verify_user(self,room_name):
        room = self.rooms.get(room_name)
        if room:
            return "true"
        else:
            return "false"
login_system = Registration()
chat_system = ChatSystem()
while True:
    print("------------------------------")
    print("        Login System  ")
    print("------------------------------")
    print("      1: Registration ")
    print("      2: Login ")
    print("      e: Exit  ")
    print("------------------------------")
    login_selection = input("Select an Option: ")
    if login_selection == '1':
        print("")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        response = login_system.Signup(username, password)
        print(response)
    elif login_selection == '2':
        print("")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        response = login_system.Login(username, password)
        print("")
        if(response == "Login successfully"):
            print(response)
            while True:
                user = Sender(username)
                print("------------------------------")
                print("            Menu  ")
                print("------------------------------")
                print("       1: Create Room ")
                print("       2: Join Room ")
                print("       3: Send Message  ")
                print("       4: Display Message  ")
                print("       5: Exit Room  ")
                print("       6: Exit   ")
                print("------------------------------")
                user_selection = input("Select The One Option : ")
                if(user_selection == '1'):
                    room_name = input("Enter room name: ")
                    chat_system.create_room(room_name)
                elif(user_selection == '2'):
                    if 'user' not in locals():
                        print("Please add a user first.")
                    else:
                        room_name = input("Enter room name to join: ")
                        chat_system.join_room(user, room_name)
                elif(user_selection=='3'):
                    if 'user' not in locals():
                        print("Please add a user first.")
                    else:
                        while True: 
                            room_name = input("Enter room name to send message: ");
                            check_room =chat_system.verify_user(room_name);
                            if( check_room =='true'):
                                message_content = input("Enter message: ")
                                chat_system.rooms[room_name].send_message(user, message_content);
                                break
                            else:
                                print("Room not exist, Try again")
                elif(user_selection == '4'):
                    room_name = input("Enter room name to display messages: ")
                    if room_name in chat_system.rooms:
                        chat_system.rooms[room_name].display_messages()
                    else:
                        print(f"Room '{room_name}' does not exist!")
                elif(user_selection == '5'):
                    if 'user' not in locals():
                         print("Please add a user first.")
                    else:
                        room_name = input("Enter room name to exit: ")
                        chat_system.exit_room(user, room_name)
                elif(user_selection =='6'):
                    break;
                else:
                    print("Invalid inputs")
    

    elif login_selection == 'e':
        break

    else:
        print("Invalid Selection")
