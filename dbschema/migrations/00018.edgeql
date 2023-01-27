CREATE MIGRATION m14l7mwkormbzzdk35mu7kmhhlnnkpoxjwh5sajfri6p3uxniw3lca
    ONTO m1pdd6dxr44u2po2i5kdiftmg4vzueifphjqeoinzm3uxfi56o3q4q
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::regexp(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$');
      };
      ALTER PROPERTY email {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY access_token {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY account_email {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY account_id {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY oauth_name {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY first_name {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY last_name {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      CREATE PROPERTY full_name := (((.first_name ++ ' ') ++ .last_name));
      ALTER PROPERTY username {
          SET REQUIRED USING ('');
      };
  };
};
