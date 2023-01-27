select EdgeBaseOAuthUser {
    id,
    account_id,
    oauth_name,
    account_email,
    access_token,
    expires_at,
    refresh_token,
}
filter .account_id = <str>$account_id and .oauth_name = <str>$oauth_name;
