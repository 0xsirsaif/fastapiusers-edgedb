CREATE MIGRATION m1pwmjpte5jtueqmkaneuljtzpiesec7abt2xvamd3eyvfko77bbeq
    ONTO m1qfuchkgu2kcprg7eh5onqzepi4ili7igp3dq6ekroembndc3mowa
{
  ALTER TYPE default::BaseUser {
      CREATE REQUIRED PROPERTY first_name -> std::str {
          SET REQUIRED USING ('');
      };
      CREATE REQUIRED PROPERTY last_name -> std::str {
          SET REQUIRED USING ('');
      };
  };
};
