CREATE MIGRATION m1her3yymnuiwh5azx4a7yu36wb2lo32dsjnxlybizg2pwfv3pgqfa
    ONTO m17zlocuiw2zpkeu2vetdz23c4wmkcxwaawghorlcx637yibadceza
{
  ALTER TYPE default::BaseUser {
      DROP PROPERTY full_name;
  };
};
