# Encapsulation Assignment Reflection

## 📝 Activity 1: Access Modifier Declarations
Below are the conceptual choices and code statements for the 5 scenarios given in Activity 1:

1. **GameCharacter (username):** Public (Accessible to everyone)
   ```python
   self.username = username
   ```
2. **BankAccount (balance):** Private (Strict protection against direct modification)
   ```python
   self.__balance = balance
   ```
3. **Vehicle (engineCode):** Protected (Accessible only within the class and its subclasses)
   ```python
   self._engineCode = engineCode
   ```
4. **Student (schoolName):** Public (Safe for all to view and alter)
   ```python
   self.schoolName = schoolName
   ```
5. **VotingSystem (voterID):** Private (Hidden securely for data protection)
   ```python
   self.__voterID = voterID
   ```

---

## 🔍 Activity 2 Reflection Question
**Question:** *How does using `@property` make your code easier to read compared to using traditional `get_` and `set_` methods?*

**Answer:**
Using the `@property` decorator allows us to access and modify an object's internal private variables using standard dot notation (`obj.variable = value`) instead of calling traditional methods with parentheses (`obj.set_variable(value)`). 

This benefits code readability in two major ways:
1. **Cleaner Syntax:** It eliminates explicit function call syntax `()`, making the code look like it is interacting with clean, readable data attributes while secretly maintaining background data validation or protection logic.
2. **Backward Compatibility:** It allows a developer to turn a public field into a private protected field later without breaking the public interface API for any external code already using the class.
