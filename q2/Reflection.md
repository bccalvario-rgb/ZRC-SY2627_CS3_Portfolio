# Encapsulation Assignment Reflection

# Activity 1: Access Modifier Declarations
* GameCharacter (username): Public | self.username = username
* BankAccount (balance): Private | self.__balance = balance
* Vehicle (engineCode): Protected | self._engineCode = engineCode
* Student (schoolName): Public | self.schoolName = schoolName
* VotingSystem (voterID): Private | self.__voterID = voterID

# Activity 2: Reflection Question
# How does using @property make your code easier to read compared to using traditional get_ and set_ methods?

Using the @property decorator allows us to access and modify private variables using standard dot notation (obj.variable = value) instead of calling traditional methods with parentheses (obj.set_variable(value)). This makes the syntax much cleaner and more intuitive by removing bulky function calls, allowing our methods to read like natural variables while safely handling data validation in the background.
