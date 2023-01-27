CREATE MIGRATION m1id7mwktgazfcw4imscnlsvafjofjyn5omcedhosu4pec4hsiloaq
    ONTO m172hlezw2cenxqsxggjb2irgszjqy2vqgqyieg4svepdbx46lnbxq
{
  ALTER TYPE default::EdgeAccessTokenUser {
      CREATE REQUIRED PROPERTY user_id -> std::str {
          SET REQUIRED USING ('');
      };
  };
  ALTER TYPE default::EdgeBaseUser {
      CREATE MULTI LINK access_tokens -> default::EdgeAccessTokenUser {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
