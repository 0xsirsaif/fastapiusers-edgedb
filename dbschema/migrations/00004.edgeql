CREATE MIGRATION m1gq2rsbcrvw5srn6xgbtix4zqwyle5qr6daxx6qxc6674eq54plxa
    ONTO m13yjgdimbdaap4resc7hxt3mzt2hmaocssjj7whdy7b5c4357crtq
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY is_active {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY is_superuser {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY is_verified {
          RESET OPTIONALITY;
      };
  };
};
