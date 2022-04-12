For testing email functionality please set email and password env. vars in settings.py:

	*EMAIL_HOST_USER = os.environ.get('')

	*EMAIL_HOST_PASSWORD = os.environ.get('')


Journals:

	path/create -> create journal
	
	path/excel -> download journals in excel format
	
	path/pdf -> download journals in pdf format
	
	path/mail -> send journals file in excel format by email
	
	path/list -> list all created journals
	
	*admin user can see journals from all users


Users:

	path/ -> user login
	
	path/register -> user registration
	
	path/logout -> user logout
	
	path/profile -> edit user profile
	
	path/password_change -> change user password
	
	path/password_reset -> reset user password
	
