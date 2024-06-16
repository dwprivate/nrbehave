#language: en
@fixture.browser.firefox
Feature: Demo MyDesk - Devis Auto

  Scenario: Login to MyDesk
    When I visit "https://mydesk-tst.ethias.be/login"
    And I fill in element "input[placeholder="Nom d'utilisateur"]" with value "P61186"
    And I fill in element "input[placeholder="Mot de passe"]" with value "DWE12345"
    And I press element "button[type="submit"]"
    Then the browser's URL should match "https://mydesk-tst.ethias.be/home" within 30 seconds



    When I visit "https://mydesk-tst.ethias.be/terminal?actionKey=S1GSI&actionType=100"
    When I setup MyDesk
    Then zone 1,2 should have value "ETHI" within 30 seconds

    When I fill in zone 4,41 with value "702217<F1>"
    Then zone 2,2 should have value "702217" within 10 seconds

    # RETURN MUST BE MAPPED AS Entrer
    When I send to MyDesk "<RETURN>"
    Then zone 1,45 should have value "S1GSIeE" within 10 seconds

    When I send to MyDesk "SIDEVA2<RETURN>"
    Then zone 4,17 should have value "ORIGINE DE L'INTERVENTION No" within 10 seconds

    When I send to MyDesk "<RETURN><F1>"
    # il n'y a pas toujours de conjoint, mais s'il y en a un il faut encore un return
    And I send to MyDesk "<RETURN>"
    Then zone 24,2 should have value "GI3904: Commande ex{cut{e" within 10 seconds

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

    And I send to MyDesk "<F1>"

    And I log out