CREATE MIGRATION m1eadqf3euyx5tpaogx55ntofdhuxp2vamka25sqvgzhqj7t3fukya
    ONTO m1nng42nf6jyq6eb2mnvcl7xfesbi5gfbrmmserku47th5pp55dqqq
{
  ALTER TYPE default::AbstractBaseUser {
      DROP PROPERTY email;
  };
  ALTER TYPE default::EdgeAccessTokenUser {
      DROP PROPERTY user_id;
      DROP EXTENDING default::AbstractBaseUser;
  };
  ALTER TYPE default::EdgeBaseOAuthUser DROP EXTENDING default::AbstractBaseUser;
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY account_email {
          CREATE CONSTRAINT std::regexp(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$');
      };
      ALTER PROPERTY account_id {
          DROP CONSTRAINT std::exclusive;
      };
      ALTER PROPERTY oauth_name {
          DROP CONSTRAINT std::exclusive;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY username {
          RENAME TO email;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      DROP PROPERTY full_name;
  };
  ALTER TYPE default::EdgeBaseUser {
      DROP PROPERTY first_name;
  };
  ALTER TYPE default::EdgeBaseUser {
      DROP PROPERTY last_name;
      DROP EXTENDING default::AbstractBaseUser;
  };
  DROP TYPE default::AbstractBaseUser;
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY created_at {
          SET REQUIRED USING (std::datetime_current());
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER LINK access_tokens {
          ON SOURCE DELETE DELETE TARGET;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER LINK oauth_accounts {
          ON SOURCE DELETE DELETE TARGET;
      };
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::regexp(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY hashed_password {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY is_active {
          SET REQUIRED USING (true);
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY is_superuser {
          SET REQUIRED USING (false);
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY is_verified {
          SET REQUIRED USING (false);
      };
  };
};
