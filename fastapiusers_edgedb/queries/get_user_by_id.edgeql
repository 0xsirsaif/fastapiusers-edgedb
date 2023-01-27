select EdgeBaseUser {id, username, email, is_active, is_superuser}
filter .id = <uuid>$id;
