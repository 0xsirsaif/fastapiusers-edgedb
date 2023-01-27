CREATE MIGRATION m1scnve6o3stvwpunk3luvgazdrs6ksufp5o6kvwnltzgsnloknlra
    ONTO m1gq2rsbcrvw5srn6xgbtix4zqwyle5qr6daxx6qxc6674eq54plxa
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY hashed_password {
          RESET OPTIONALITY;
      };
  };
};
