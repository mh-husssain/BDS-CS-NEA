###Hashing Algorithm###
#Programmed by Hisham Hussain

def hash_bcrypt(password):
    import bcrypt
    ###Input validation###
    password = password.encode('utf-8') # Convert str to bytes using (UTF-8)

    # Applying hashing library to argument
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt( ))
    return hashedPassword

def bcryptCheck(userPassword, password):
    import bcrypt # Import Library
    userPassword = userPassword.encode('utf-8')
    password = userPassword.encode('utf-8')
    if bcrypt.checkpw(userPassword, password):
        return True # Password is correct
    else:
        return False # Password Mismatch!

'''
def procedure(): #Arbitrary procedure to get password
    password = str(input("Please enter your password: "))
    print (hash_bcrypt(password))
    procedure()
procedure()
'''
