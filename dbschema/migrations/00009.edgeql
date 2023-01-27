CREATE MIGRATION m14zz5wdplhlbtdnjdmec6rw4ocushc4ulqbgtoh225dp3auc65d4a
    ONTO m1her3yymnuiwh5azx4a7yu36wb2lo32dsjnxlybizg2pwfv3pgqfa
{
  ALTER TYPE default::AbstractBaseUser {
      DROP PROPERTY hashed_password;
      DROP PROPERTY is_active;
      DROP PROPERTY is_superuser;
      DROP PROPERTY is_verified;
      DROP PROPERTY username;
  };
  ALTER TYPE default::BaseUser RENAME TO default::EdgeBaseUser;
  CREATE TYPE default::EdgeAccessTokenUser EXTENDING default::AbstractBaseUser {
      CREATE REQUIRED PROPERTY created_at -> std::datetime {
          SET default := (std::datetime_current());
      };
      CREATE REQUIRED PROPERTY token -> std::str;
  };
  CREATE TYPE default::EdgeBaseOAuthUser EXTENDING default::AbstractBaseUser {
      CREATE REQUIRED PROPERTY access_token -> std::str;
      CREATE REQUIRED PROPERTY account_id -> std::str;
      CREATE REQUIRED PROPERTY expires_at -> std::int32;
      CREATE REQUIRED PROPERTY oauth_name -> std::str;
      CREATE REQUIRED PROPERTY refresh_token -> std::str;
  };
  ALTER TYPE default::EdgeBaseUser {
      CREATE PROPERTY hashed_password -> std::str;
      CREATE PROPERTY is_active -> std::bool;
      CREATE PROPERTY is_superuser -> std::bool;
      CREATE PROPERTY is_verified -> std::bool;
      CREATE REQUIRED PROPERTY username -> std::str {
          SET REQUIRED USING ('');
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
