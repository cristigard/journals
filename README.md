For testing email functionality please set email and password env. vars in settings.py:

	*EMAIL_HOST_USER = os.environ.get('')

	*EMAIL_HOST_PASSWORD = os.environ.get('')


Journals:

	host/journal/create -> create journal
	
	host/journal/excel -> download journals in excel format
	
	host/journal/pdf -> download journals in pdf format
	
	host/journal/mail -> send journals file in excel format by email
	
	host/journal/list -> list all created journals
	
	*users can retrive/download only their jurnals
	*admin user can retrive/download journals from all users


Users:

	host/users -> user login
	
	host/users/register -> user registration
	
	host/users/logout -> user logout
	
	host/users/profile -> edit user profile
	
	host/users/password_change -> change user password
	
	host/users/password_reset -> reset user password
	
