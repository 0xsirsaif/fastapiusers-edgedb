CREATE MIGRATION m15msdy4qkwk3xzkzcsbmacq4xn7irjyiumybrtvxsdkfarghyt54a
    ONTO m1hnhdxrq5js2w4xpah6ustax4slz3cpvaucxxuyrv2wfk3bk2uceq
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          DROP CONSTRAINT std::exclusive;
      };
  };
};
