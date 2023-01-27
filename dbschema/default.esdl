module default {
    # User type that implements User Protocol
    abstract type AbstractBaseUser {
        property email -> str {
            constraint exclusive;
            constraint regexp(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$");
        }
    }

    type EdgeBaseUser extending AbstractBaseUser {
        required property first_name -> str;
        required property last_name -> str;
        property full_name := .first_name ++ ' ' ++ .last_name;

        property hashed_password -> str;
        property is_active -> bool;
        property is_superuser -> bool;
        property is_verified -> bool;

        required property username -> str {
            constraint exclusive;
        };

        multi link oauth_accounts -> EdgeBaseOAuthUser {
            # ensures a one-to-many relationship
            constraint exclusive;
        }

        multi link access_tokens -> EdgeAccessTokenUser {
            # ensures a one-to-many relationship
            constraint exclusive;
        }

        # required property birth_date -> cal::local_date;
        # property age := <Age>();
        # scalar type Age extending int16{
            # constraint max_value(120);
            # constraint min_value(0);
        # };
    }

    type EdgeBaseOAuthUser extending AbstractBaseUser {
        required property oauth_name -> str  {
            constraint exclusive;
        }
        required property account_id -> str {
            constraint exclusive;
        }
        property expires_at -> int32;
        property refresh_token -> str;
        required property access_token -> str;
        required property account_email -> str;
        
    }

    type EdgeAccessTokenUser extending AbstractBaseUser {
        required property token -> str {
            constraint exclusive;
        }
        property created_at -> datetime {
            default := std::datetime_current();
        };
        property user_id -> str;
    }

}
