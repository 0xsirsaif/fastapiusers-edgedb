module default {
    type User {
        required property email -> str {
            constraint exclusive;
            constraint regexp(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$");
        }

        required property hashed_password -> str;
        required property is_active -> bool;
        required property is_superuser -> bool;
        required property is_verified -> bool;

        multi link oauth_accounts -> OAuthUser {
            # ensures a one-to-many relationship
            constraint exclusive;
            # Deleting this Object (User) will unconditionally delete linked objects (oauth)
            on source delete delete target;
        }

        multi link access_tokens -> EdgeAccessTokenUser {
            # ensures a one-to-many relationship
            constraint exclusive;
            # Deleting this Object (User) will unconditionally delete linked objects (access)
            on source delete delete target;
        }

    }

    type OAuthUser {
        required property account_email -> str {
            constraint regexp(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$");
        }
        required property oauth_name -> str;
        required property account_id -> str;
        required property access_token -> str;
        property expires_at -> int32;
        property refresh_token -> str;

    }

    type EdgeAccessTokenUser {
        required property token -> str {
            constraint exclusive;
        }
        required property created_at -> datetime {
            default := std::datetime_current();
        };
    }

}
