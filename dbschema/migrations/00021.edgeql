CREATE MIGRATION m172hlezw2cenxqsxggjb2irgszjqy2vqgqyieg4svepdbx46lnbxq
    ONTO m15msdy4qkwk3xzkzcsbmacq4xn7irjyiumybrtvxsdkfarghyt54a
{
  ALTER TYPE default::AbstractBaseUser {
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::regexp(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$');
      };
  };
};
