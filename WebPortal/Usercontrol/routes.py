from WebPortal.Usercontrol.Entities.ProfilePictureChanger import ProfilePictureChangerClass
from flask.globals import request
from flask_login.utils import logout_user
from werkzeug.utils import redirect
from WebPortal.models import users
from flask import Blueprint, render_template
from flask.helpers import flash, url_for
from flask_login import current_user

from WebPortal.Usercontrol.Entities.UsernameChanger import UsernameChangerClass
from WebPortal.Usercontrol.Entities.PasswordChanger import PasswordChangerClass
from WebPortal.Usercontrol.Entities.Registrator import RegistratorClass
from WebPortal.Usercontrol.Entities.AdminPanel import AdminPanelClass
from WebPortal.Usercontrol.Entities.RightsChanger import RightsChangerClass
from WebPortal.Usercontrol.Entities.DeleteUser import DeleteUserClass
from WebPortal.Usercontrol.Entities.ProfilePictureChanger import ProfilePictureChangerClass


UserControl = Blueprint('UserControl', __name__)

# The ones that end with <user> in the end get the username string value`

# the main page of the usercontrol blueprint visible even to normal users
@UserControl.route('/userinfo')
def Userinfo():
    return render_template('UserInfo.html')

# the admin panel page
@UserControl.route('/userinfo/AdminPanel')
def AdminPanel():
    return AdminPanelClass.AdminPanel()

# Gives admin rights to the given user.
@UserControl.route('/userinfo/AdminPanel/GiveAdminRights/<user>', methods=['GET', 'POST'])
def GiveAdminRights(user):
    RightsChanger = RightsChangerClass(user)
    return RightsChanger.Main()

# Deletes the given user
@UserControl.route('/userinfo/AdminPanel/DeleteUser/<user>', methods=['GET', 'POST'])
def DeleteUser(user):
    DelUser = DeleteUserClass(user)
    return DelUser.Main()

# Registers a user
@UserControl.route('/userinfo/AdminPanel/Register', methods=['GET', 'POST'])
def RegisterUser():
    registrator = RegistratorClass()
    return registrator.RegisterUser()

# Changes username to the given user
@UserControl.route('/userinfo/UsernameChanger/<user>', methods=['GET', 'POST'])
def UsernameChange(user):
    usernamechanger = UsernameChangerClass(user)
    return usernamechanger.Main()

# Changes the password to the given user
@UserControl.route('/userinfo/ChangePassword/<user>', methods=['GET', 'POST'])
def PasswordChange(user):
    passwordchanger = PasswordChangerClass(user)
    return passwordchanger.Main()

# Changes the profile to the given user
@UserControl.route('/userinfo/ProfilePictureChange/<user>', methods=['GET', 'POST'])
def ChangeProfilePicture(user):
    profilePictureChanger = ProfilePictureChangerClass(user)
    return profilePictureChanger.Main()
    
# logs out the current user
@UserControl.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Authentication.Login'))
