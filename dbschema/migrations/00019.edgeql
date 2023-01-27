CREATE MIGRATION m1hnhdxrq5js2w4xpah6ustax4slz3cpvaucxxuyrv2wfk3bk2uceq
    ONTO m14l7mwkormbzzdk35mu7kmhhlnnkpoxjwh5sajfri6p3uxniw3lca
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          DROP CONSTRAINT std::regexp(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$');
      };
      ALTER PROPERTY email {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY token {
          SET REQUIRED USING ('');
      };
  };
};
