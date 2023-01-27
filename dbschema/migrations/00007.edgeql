CREATE MIGRATION m17zlocuiw2zpkeu2vetdz23c4wmkcxwaawghorlcx637yibadceza
    ONTO m1ribasvfeapw6caixpjalxeswpjdryuruo2pi5d7ox62m73z75lla
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
