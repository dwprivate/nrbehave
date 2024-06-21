#language: en
@autoLogout @fixture.browser.firefox
Feature: Demo MyDesk - Devis Auto

  Scenario: Création Devis Auto
    When I run scenario "mydesk_multi_steps" "Login to MyDesk"
    And I go to screen "S1GSI"
    Then textshot

    When I fill in zone 4,41 with value "702217<RETURN>"
    Then zone 2,2 should contains value "702217" within 10 seconds

  #    # RETURN MUST BE MAPPED AS Entrer (dont by setupMyDesk in Login to MyDesk)
    When I press keys "<RETURN>" in MyDesk
    Then zone 1,45 should contains value "S1GSIeE" within 10 seconds

    When I press keys "SIDEVA2<RETURN>" in MyDesk
    Then zone 4,17 should contains value "ORIGINE DE L'INTERVENTION No" within 10 seconds

    When I press keys "<RETURN><F1>" in MyDesk
#    # il n'y a pas toujours de conjoint, mais s'il y en a un il faut encore un return
    And I press keys "<RETURN>" in MyDesk
    Then zone 24,2 should contains value "GI3904: Commande ex{cut{e" within 10 seconds

    #CATEGORIE DE VEHICULE
    When I fill in zone 5,26 with value "110"
    #Date de permis de conduire
    And I fill in zone 13,31 with value "10102000"
    #Expérience de conduite
    And I fill in zone 13,68 with value "10"
    # Nombre de sinistre(s) sur 5 ans
    And I fill in zone 14,36 with value "00"
      # Nombre d'années sans sinistre
    And I fill in zone 14,72 with value "10"
      # Nombre d'années sans sinistre
    And I fill in zone 15,32 with value "N"
      # Nb. assureurs antérieurs
    And I fill in zone 23,29 with value "00"

    And I press keys "<F1>" in MyDesk

    # RECHERCHE MARQUE
    Then zone 12,2 should contains value "VARIABLES DE RISQUES"
    When I fill in zone following "Marque/type" with value "OPE?<RETURN>"
    Then zone 3,26 should contains value "MARQUES ET TYPES DE VEHICULES"
    When I fill in zone preceding "ASTRA  " with value "S<RETURN>"
    Then zone 12,2 should contains value "VARIABLES DE RISQUES"
    And zone 14,40 should contains value "ASTRA"

    When I fill in zone following "An.constr." with value "2000"
    When I fill in zone following "Puissance Kw" with value "125"
    # todo: auto replace NPSB + datatable ?
    When I fill in zone following "Nb. Pers. Transp." with value "5"
    When I fill in zone following "KM est./a" with value "5000"
    When I fill in zone following "Usage prof." with value "N"
    When I fill in zone following "BM actu.:" with value "00"
    When I fill in zone following "Véh. Occ." with value "N"
    When I fill in zone following "Val. catalogue" with value "1000"
    And breakpoint
    And I press keys "<RETURN><F1>" in myDesk
    # F1 ? le devis est créé ??
