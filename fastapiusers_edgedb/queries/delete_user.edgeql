with user := (delete EdgeBaseUser filter .id = <uuid>$id)
select user {id, username};
