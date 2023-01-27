CREATE MIGRATION m1pdd6dxr44u2po2i5kdiftmg4vzueifphjqeoinzm3uxfi56o3q4q
    ONTO m1c6sxgpzwmccb3jvavgcvcbj3niwogvhtjbjshtalwr5jti2m7bza
{
  ALTER TYPE default::EdgeBaseOAuthUser {
      ALTER PROPERTY oauth_name {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
