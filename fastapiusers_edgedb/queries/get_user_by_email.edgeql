select EdgeBaseUser {id, username, email, is_active, is_superuser}
filter .email = <str>$email;
