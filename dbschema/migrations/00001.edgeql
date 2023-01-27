CREATE MIGRATION m1qfuchkgu2kcprg7eh5onqzepi4ili7igp3dq6ekroembndc3mowa
    ONTO initial
{
  CREATE FUTURE nonrecursive_access_policies;
  CREATE ABSTRACT TYPE default::AbstractBaseUser {
      CREATE REQUIRED PROPERTY email -> std::str {
          CREATE CONSTRAINT std::regexp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
      };
      CREATE REQUIRED PROPERTY hashed_password -> std::str;
      CREATE REQUIRED PROPERTY is_active -> std::bool;
      CREATE REQUIRED PROPERTY is_superuser -> std::bool;
      CREATE REQUIRED PROPERTY is_verified -> std::bool;
      CREATE REQUIRED PROPERTY username -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  CREATE TYPE default::BaseUser EXTENDING default::AbstractBaseUser;
};
