#language: en
@autoLogout @fixture.browser.firefox
Feature: Demo MyDesk - FATCA

  Scenario Outline: Check Fatca
    When I run scenario "mydesk_multi_steps" "Login to MyDesk"
    And I go to screen "S1GSI"
    And I fill in zone after "NO. POLICE" with value "<Police><RETURN>"
    Then zone "email" 10,14 should equals value "<Mail> "
    Then textshot

    Examples:
      | Police   | Mail                    |
      | 30233455 |                         |
      | 30443076 | 4fantastiques@orange.fr |

#@should_fail
#    Examples:
#      | 30443076 |                         |
#      | 30443076 | 4fantastiques@orange.   |
#      | 30233455 | x                       |
#      | 30443076 | 4xantastiques@orange.fr |


  Scenario: notes
    * breakpoint
"""
nWqza6-iNiWcrryzmFEK
fichier d'entrée: CSV colonne fixe
sortie: liste des entrées vérifiées  + evidences

affilié ok
S1GSI
comparer adresse mail au fichier
vérifier xxx à csv
zone 3,2 <> entête (dans le CSV)
z 5,2 <> langue

ecran S1GCR (accessible via <HOME>S1GCR<RETURN> ou via menu mydesk)
tip: vérifier si on est en recheche ou en résultat, la destation apparait en haut à droite
zone 17,12 <> pays dans le CSV
attention mapping + trouver l'adresse actuelle s'il y en a plusieurs (i.e. date)

l'écran suivant dépend de la col TYPE POLICE + PGO
FI -> FIGPO (attention pas confondre 1 et )
F1 -> P1GPO, ...

on arrive sur l'écran de recherche (c'est juste des critères, ça ne veut pas dire qu'on est revenu en arrière)
remettre un affilié ou un n de police

il peut y avoir un écran intermédiaire mais uniquement s'il y a plusieurs polices (Identification d'une police)
S<RETURN>
pour l'auto il vaut mieux se baser sur le n de police
j'arrive sur l'écran memo = historique,  et TYPE OPER OBJET = "zone commande memo"

pour aller plus loin: demander "droits consultation sur les polices vie 3e pilier" à Fabian Amel
ou les memes que tiphaine
il faudra créer un"""
