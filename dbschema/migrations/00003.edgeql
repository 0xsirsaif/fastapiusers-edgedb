CREATE MIGRATION m13yjgdimbdaap4resc7hxt3mzt2hmaocssjj7whdy7b5c4357crtq
    ONTO m1pwmjpte5jtueqmkaneuljtzpiesec7abt2xvamd3eyvfko77bbeq
{
  ALTER TYPE default::BaseUser {
      CREATE PROPERTY full_name := (((.first_name ++ ' ') ++ .last_name));
  };
};
