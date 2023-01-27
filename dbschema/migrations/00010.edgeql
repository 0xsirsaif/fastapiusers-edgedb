CREATE MIGRATION m1hxxophubejyuhure5xejuwx6h7emk6lzx3hrsvnws5kfx2jtgwxa
    ONTO m14zz5wdplhlbtdnjdmec6rw4ocushc4ulqbgtoh225dp3auc65d4a
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY created_at {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY token {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY access_token {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY account_id {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY expires_at {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY oauth_name {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY refresh_token {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY first_name {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY last_name {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      ALTER PROPERTY username {
          RESET OPTIONALITY;
      };
  };
};
