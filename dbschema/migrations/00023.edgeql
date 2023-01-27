CREATE MIGRATION m1xucmrm6yr6trwomndqcgufbgyw2rkyqh2we63nr63oiha7zmnftq
    ONTO m1id7mwktgazfcw4imscnlsvafjofjyn5omcedhosu4pec4hsiloaq
{
  ALTER TYPE default::EdgeAccessTokenUser {
      ALTER PROPERTY token {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
