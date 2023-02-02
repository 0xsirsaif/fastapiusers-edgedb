CREATE MIGRATION m1ipv4lukstuo3uxkdsb4no26mmw6l27dto466begyinjsefibrfca
    ONTO m1eadqf3euyx5tpaogx55ntofdhuxp2vamka25sqvgzhqj7t3fukya
{
  ALTER TYPE default::EdgeBaseOAuthUser RENAME TO default::OAuthUser;
  ALTER TYPE default::EdgeBaseUser RENAME TO default::User;
};
