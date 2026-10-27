Activity 1: Inheritance Hierarchy Analysis

1. What is/are the parent class/es of the Programmer class in the video?

Based on the inheritance hierarchy shown in the video, the immediate parent class of Programmer is Employee. Since Employee itself inherits from the Person class, Person acts as the indirect parent or grandparent class to Programmer.

2. If you were to add a new role called Intern, where would you place it in the inheritance hierarchy? Why?

The Intern class should be placed as a subclass of the Employee class, sitting parallel to Programmer, Manager, and Cleaner. 

This makes sense because an intern is a type of employee within a business environment. Placing it here allows the Intern class to seamlessly reuse common properties like name, age, job title, and salary from Person and Employee, while letting you add custom attributes unique to interns like internship duration or school affiliation.
