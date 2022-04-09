For testing email functionality please set email and password env. vars in settings.py:
EMAIL_HOST_USER = os.environ.get('')
EMAIL_HOST_PASSWORD = os.environ.get('')

Journals:
	/create - create journal
	/download - download journals in excel format
	/mail - send journals file in excel format by email
	/list - list all created journals

Users:
	/ - user login
	/register - user registration
	/logout - user logout
	/profile - edit user profile
	/password_change - change user password
	/password_reset - reset user password
