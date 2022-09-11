#!/usr/bin/env python3

import flask_env
import subprocess
from flask import Flask, request

# create the Flask app
app = Flask(__name__)
variable = subprocess.check_output(['uname', '-a'])

def check_user_login_and_password(login, password):
    """
    Use for cheking if input login and password in Flask login page is correct (compare with flask_env vars)
    :param login, password:
    :return str ([Failed_Login] | [Failed_Password] | [Successful] | [Some_problem]):
    """
    if login != flask_env.admin_login:
        return '[Failed_Login]'
    elif password != flask_env.admin_password:
        return '[Failed_Password]'
    elif login == flask_env.admin_login and password == flask_env.admin_password:
        return '[Successful]'
    else:
        return '[Some_problem]'

@app.route('/', methods=['GET', 'POST'])
def auth_form():
    """
    Use for handling web link /
    :param None:
    :return str ([Failed_Login] | [Failed_Password] | [Some_problem] | [{}]):
    """
    if request.method == 'POST':
        user_status = check_user_login_and_password(request.form.get('user'), request.form.get('pasw'))
        if user_status == '[Failed_Login]' or user_status == '[Failed_Password]' or user_status == '[Some_problem]':
                return user_status
        else:
                return variable
    else:
        return '<html><body> <form method=post >login:<input type=text name=user /><br/> password:<input type=password name=pasw /> <br /> <input type=submit /> </form> </body></html>'

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=flask_env.flask_port)
