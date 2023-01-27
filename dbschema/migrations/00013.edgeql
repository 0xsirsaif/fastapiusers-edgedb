CREATE MIGRATION m15nichsypgzzktvee5unsyhaouwwqzpbqf6xpbcueliipfqfmseoq
    ONTO m15suwutxgmoccj6oipu2w4om4boasa7at2wwv7mdxarzaaxuosoua
{
  ALTER TYPE default::EdgeBaseOAuthUser {
      CREATE PROPERTY account_email -> std::str;
  };
};
