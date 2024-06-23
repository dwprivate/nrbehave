Feature: Trikcy demo

  @autoLogout @fixture.browser.firefox
  Scenario: CSV
    Given a csv file "data/FSMH.SRP.WFI121.FFILTRE.csv" with encoding "latin-1"
    And a scenario outline "mydesk/fatca" "Check Fatca"
    Then check all CSV rows
