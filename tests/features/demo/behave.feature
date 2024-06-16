Feature: Behaving demo

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

  Scenario: execute_steps
    Given a scenario
    """
      Given first operand is 10
      And second operand is 15
      When I sum all operands
      Then result should be 25
    """
    When I execute it
    Then it should return success
    Given a scenario
    """
      Given first operand is 10
      And second operand is 15
      When I sum all operands
      Then result should be 32
    """
    When I execute it
    Then it should return failed

  Scenario: execute_steps with rowData
    Given a scenario
    """
      Given first operand is <first>
      And second operand is <second>
      When I sum all operands
      Then result should be <result>
    """
    When I execute it with data
    | first | second | result |
    | 10    | 15     | 25     |
    Then it should return success

    Scenario: Find feature file and execute one scenario
      Given a glob "**/behave.feature"
      When I search for files using this glob
      Then I should find 1 file
      When I search for scenario "sum operands" in this file
      Then I should find 1 scenario
      When I execute this scenario
      Then it should return success
