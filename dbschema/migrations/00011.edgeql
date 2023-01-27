CREATE MIGRATION m1xhvcrpa2n3h775hjucnbgzvw3r75lehxutuvyzkeklgag5uz72vq
    ONTO m1hxxophubejyuhure5xejuwx6h7emk6lzx3hrsvnws5kfx2jtgwxa
{
  ALTER TYPE default::EdgeBaseOAuthUser {
      DROP PROPERTY account_id;
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      CREATE LINK account_id -> default::EdgeBaseUser;
  };
};
