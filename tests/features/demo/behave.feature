@tf
Feature: Behaving demo

  @t1 @t2
  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

    Scenario: sum operands
      Given first operand is 10
      And second operand is 15
      When I sum all operands
      Then result should be 25

  Scenario Outline: sum operands with examples
    Given first operand is <first>
    And second operand is <second>
    When I sum all operands
    Then result should be <sum>

    Examples:
    | first | second | sum |
    | 10    | 15     | 25  |
    | 0     | 0      | 0   |

    Scenario: Execute single scenario from feature file
      # Rename this step, to avoid confusion between feature file name and feature title ?
      When I run scenario "behave" "run a simple test"
      Then It should succeed

  Scenario: Execute scenario outline from feature file
      When I run scenario "behave" "sum operands with examples" with data
        | first | second | sum |
        | 10    | 15     | 25  |
      Then It should succeed
