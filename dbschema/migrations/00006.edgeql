CREATE MIGRATION m1ribasvfeapw6caixpjalxeswpjdryuruo2pi5d7ox62m73z75lla
    ONTO m1scnve6o3stvwpunk3luvgazdrs6ksufp5o6kvwnltzgsnloknlra
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          DROP CONSTRAINT std::regexp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
      };
  };
};
