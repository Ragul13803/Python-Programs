import re
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
def check(email):
    if(re.fullmatch(pattern, email)):
        print("Email is valid")
    else:
        print("invalid Email")
if __name__ == '__main__':
    email = (input("Enter the mail id:\n"))
    check(email)
