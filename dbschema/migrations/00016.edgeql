CREATE MIGRATION m1c6sxgpzwmccb3jvavgcvcbj3niwogvhtjbjshtalwr5jti2m7bza
    ONTO m1uryvoqbbjabmfcnv5m7k3yupptxbian7hz7tfs3wa2av7zvroirq
{
  ALTER TYPE default::EdgeBaseUser {
      ALTER LINK oauth_accounts {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
