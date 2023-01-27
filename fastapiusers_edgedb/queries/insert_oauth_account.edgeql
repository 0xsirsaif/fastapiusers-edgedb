with
  oauth_name := <str>$oauth_name,
  access_token := <str>$access_token,
  expires_at := <int32>$expires_at,
  refresh_token := <str>$refresh_token,
  account_id := <str>$account_id,
  account_email := <str>$account_email,
select (
    insert EdgeBaseOAuthUser {
        oauth_name := oauth_name,
        access_token := access_token,
        expires_at := expires_at,
        refresh_token := refresh_token,
        account_email := account_email,
        account_id := account_id,
    }
) {oauth_name, access_token, expires_at, refresh_token, account_id};
