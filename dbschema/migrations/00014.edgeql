CREATE MIGRATION m1r7r2bjrjvblcparbcazrkwaogcv7gpved545n3uso2bdhnbzpf7q
    ONTO m15nichsypgzzktvee5unsyhaouwwqzpbqf6xpbcueliipfqfmseoq
{
  ALTER TYPE default::EdgeBaseOAuthUser {
      DROP LINK account_id;
  };
  ALTER TYPE default::EdgeBaseOAuthUser {
      CREATE PROPERTY account_id -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
