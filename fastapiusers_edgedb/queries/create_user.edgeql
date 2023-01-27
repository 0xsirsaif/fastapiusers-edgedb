with
  first_name := <str>$first_name,
  last_name := <str>$last_name,
  username := <str>$username,
  email := <str>$email,
  is_active := <bool>$is_active,
  is_superuser := <bool>$is_superuser,
  is_verified := <bool>$is_verified,
  hashed_password := <str>$hashed_password
select (
  insert EdgeBaseUser {
    first_name := first_name,
    last_name := last_name,
    username := username,
    email := email,
    is_active := is_active,
    is_superuser := is_superuser,
    is_verified := is_verified,
    hashed_password := hashed_password
  }
) {first_name, last_name, username, email, is_active, is_superuser, is_verified};
