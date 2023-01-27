with
    user_id := <uuid>$user_id,
    account := (
        insert EdgeBaseOAuthUser {
            oauth_name := <str>$oauth_name,
            access_token := <str>$access_token,
            expires_at := <int32>$expires_at,
            refresh_token := <str>$refresh_token,
            account_email := <str>$account_email,
            account_id := <str>$account_id,
        }
    ),
    user := (
      update EdgeBaseUser filter .id = <uuid>$user_id
      set {
        oauth_accounts += account
      }
  )
select (user_id, account, user)
