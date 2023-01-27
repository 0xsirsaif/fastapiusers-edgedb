CREATE MIGRATION m15suwutxgmoccj6oipu2w4om4boasa7at2wwv7mdxarzaaxuosoua
    ONTO m1xhvcrpa2n3h775hjucnbgzvw3r75lehxutuvyzkeklgag5uz72vq
{
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER LINK account_id {
          CREATE CONSTRAINT std::exclusive;
      };
      ALTER LINK account_id {
          SET REQUIRED USING (SELECT
              default::EdgeBaseUser 
          LIMIT
              1
          );
      };
  };
};
