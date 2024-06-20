#language: en
@autoLogOut @fixture.browser.firefox
Feature: Demo Selenium

  Tagguer un test ou une fonctionnalité avec @fixture.browser.firefox permet d'utiliser un navigateur.

  TO TEST: Actuellement, un navigateur est initié au début de la fonctionnalité et réinitialisé
  à la fin du dernier test. Les tests ne sont donc pas strictement indépendants !

  Actuellement, le seul navigateur supporté est Firefox via Selenium Manager, il n'est
  donc pas nécessaire d'installer de drivers spécifiques, ils seront téléchargés
  automatiquement (pour autant que les sites requis soient accessibles).

  Actuellement, ils n'est pas possible d'utiliser plusieurs webdrivers en même temps.

  Scenario: Accéder à un site web et cliquer sur un bouton
    Les étapes utilsées ici sont de très bas niveau, il est généralement préférable
    d'utiliser un langage plus naturel et/ou de regrouper des étapes en action ou
    intention utilisateur

    When j'ouvre la page "https://fr.wikipedia.org/"
    Then je devrais voir un élément "h1" contenant le texte "Bienvenue sur Wikipédia" en moins de 10 secondes
    When j'encode la valeur "python<RETURN>" dans le champs "input[name='search']"
    Then je devrais voir un élément "h1" contenant le texte "Python" en moins de 10 secondes

  Scenario: Accéder à un autre site web et cliquer sur un bouton
  Les étapes utilsées ici sont de très bas niveau, il est généralement préférable
  d'utiliser un langage plus naturel et/ou de regrouper des étapes en action ou
  intention utilisateur

    When j'ouvre la page "https://fr.wikipedia.org/"
    Then je devrais voir un élément "h1" contenant le texte "Bienvenue sur Wikipédia" en moins de 10 secondes
    When j'encode la valeur "python<RETURN>" dans le champs "input[name='search']"
    Then je devrais voir un élément "h1" contenant le texte "Python" en moins de 10 secondes
