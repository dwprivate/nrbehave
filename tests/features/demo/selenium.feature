#language: fr
  @web
Fonctionnalité: Demo Selenium

  Tagguer un test ou une fonctionnalité avec @web permet d'utiliser un navigateur.

  Actuellement, un navigateur est initié au début de la fonctionnalité et réinitialisé
  à la fin du dernier test. Les tests ne sont donc pas strictement indépendants !

  Actuellement, le seul navigateur supporté est Chrome via Selenium Manager, il n'est
  donc pas nécessaire d'installer de drivers spécifiques, ils seront téléchargés
  automatiquement (pour autant que les sites requis soient accessibles).

  Actuellement, ils n'est pas possible d'utiliser plusieurs webdrivers en même temps.

  Scénario: Accéder à un site web et cliquer sur un bouton
    Les étapes utilsées ici sont de très bas niveau, il est généralement préférable
    d'utiliser un langage plus naturel et/ou de regrouper des étapes en action ou
    intention utilisateur

    Soit j'ouvre la page "https://fr.wikipedia.org/"
    Alors un élément "h1" contenant le texte "Bienvenue sur Wikipédia" apparait en moins de 10 secondes
    Lorsque j'encode la valeur "python<enter>" dans le champs "input[name='search']"
    Alors un élément "h1" contenant le texte "Python" apparait en moins de 10 secondes
