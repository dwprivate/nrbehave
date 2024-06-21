Feature: Demo MyDesk - Multi steps

Scenario: Login to MyDesk
  When I visit "https://mydesk-tst.ethias.be/login"
  And I fill in element "input[placeholder="Nom d'utilisateur"]" with value "P61186"
  And I fill in element "input[placeholder="Mot de passe"]" with value "DWE12345"
  And I press element "button[type="submit"]"
  Then the browser's URL should match "https://mydesk-tst.ethias.be/home" within 30 seconds
  When I visit "https://mydesk-tst.ethias.be/terminal?actionKey=S1GSI&actionType=100"
  Then zone 1,2 should contains value "ETHI" within 30 seconds
  When I setup MyDesk
