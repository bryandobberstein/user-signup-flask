from flask import Flask, render_template, request
import string

app = Flask(__name__)
app.config["DEBUG"] = True

def valid_username(uname):
    valid = True
    if len(uname) <= 3:
        result = False
    for i in uname:
        if i not in string.ascii_letters or i not in string.digit or i not in "_-.":
            result = False
    return result

def valid_password(pword):
    result = True
    if len(pword) <= 3:
        result = False
    for i in password:
        if i not in string.ascii_letters or i not in string.digits or i not in string.punctiation:
            result = False
    return result

@app.route("/", methods = ["GET", "POST"])
def index():
    username = ""
    password = ""
    verify = ""
    email = ""
    unameerr = ""
    pwderr = ""
    verr = ""
    emerr = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]
        if not valid_username:
            invalid = True
            unameerr = "Username must be at least 4 characters and can only contain letters, numbers, _, -, and ."
        if not valid_password:
            invalid = True
            pwderr = "Password must be at least 4 characters and can only contain letters, numbers and punctuation"
        if password != verify:
            invalid = True
            verr = "Password and verify do not match"
        if len(email) > 0:
            if "@" not in email:
                invalid = True
                emerr = "Invalid email address"
            elif "." not in email:
                invalid = True
                emerr = "Invalid email address"
        if invalid == False:
            return render_template("success.html", username = username)
    return render_template("index.html", username = username, password = password, verr = verr, unameerr = unameerr, pwderr = pwderr, emerr = emerr)

def main():
    app.run()

if __name__ == "__main__":
    main()
