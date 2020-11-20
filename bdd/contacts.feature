Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <homephone> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname   | lastname   | address   | homephone   | email   |
  | firstname_1 | lastname_1 | address_1 | homephone_1 | email_1 |
  | firstname_2 | lastname_2 | address_2 | homephone_2 | email_2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from list
  Then the new contact list is quel to the old list without the deleted contact
