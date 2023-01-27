CREATE MIGRATION m1uryvoqbbjabmfcnv5m7k3yupptxbian7hz7tfs3wa2av7zvroirq
    ONTO m1r7r2bjrjvblcparbcazrkwaogcv7gpved545n3uso2bdhnbzpf7q
{
  ALTER TYPE default::EdgeBaseUser {
      CREATE MULTI LINK oauth_accounts -> default::EdgeBaseOAuthUser;
  };
};
