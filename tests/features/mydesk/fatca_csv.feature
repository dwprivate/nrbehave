@autoLogout @fixture.browser.firefox
Feature: CSV Demo


  Scenario Outline: Check S1GSI - CSV - subset (with failure)
    Given a csv file "<filename>" with encoding "latin-1"
    And I run scenario "mydesk_multi_steps" "Login to MyDesk"
    And a scenario outline "mydesk/fatca_csv" "S1GSI (once logged)"
    Then check all CSV rows

    Examples:
    | filename |
    | tests/data/subset.csv |

#    @skip
#    Examples:
#      | filename |
#      | data/FSMH.SRP.WFI121.FFILTRE.csv |


  @skip
  Scenario Outline: S1GSI (once logged)
   # When I run scenario "mydesk_multi_steps" "Login to MyDesk"
    When I go to screen "S1GSI"
    And I fill in zone after "NO. AFFILIE" with value "<AFFILIE><RETURN>"
    Then zone "email" 10,14 should equals value "<MAIL> "
    Then zone "entête" 3,2 should equals value "<ENTETE> "
    Then zone "nom" 3,15 should equals value "<NOM> "
    Then la zone "langue" 5,2 correspond à l'initiale de la valeur "<LANGUE>"
    Then textshot

    Examples:
      | AFFILIE | POLICE   | NOM                | MAIL                    | ENTETE       | LANGUE |
      | 3677854 | 30233455 | TOUSSAINT  Aurélie |                         | Mademoiselle | F      |
      | 3974766 | 30443076 | SCHEER  Laurent    | 4fantastiques@orange.fr | Monsieur     | F      |
