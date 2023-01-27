CREATE MIGRATION m1nng42nf6jyq6eb2mnvcl7xfesbi5gfbrmmserku47th5pp55dqqq
    ONTO m1xucmrm6yr6trwomndqcgufbgyw2rkyqh2we63nr63oiha7zmnftq
{
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY user_id {
          RESET OPTIONALITY;
      };
  };
};
