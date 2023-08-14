0x00. AirBnB clone - The console:

This is our first step towards building our first full Web App: The AirBnB clone. The aim is to create a copy of the Airbnb Website using the original server. 

Task 0
 - README, AUTHORS
 - You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
Task 1
 - Be pycodestyle compliant!
 - Write beautiful code that passes the pycodestyle checks.
Task 2
 - Unittests
 - All your files, classes, functions must be tested with unit tests
Task 3
 - BaseModel
 - Write a class BaseModel that defines all common attributes/methods for other classes:
Task 4
 - Create BaseModel from dictionary
 - Previously we created a method to generate a dictionary representation of an instance (method to_dict()).
 - Now it’s time to re-create an instance with this dictionary representation.
Task 5
 - Store first object
 - Now we can recreate a BaseModel from another one by using a dictionary representation:
 - Writing the dictionary representation to a file won’t be relevant:
 - So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.
Task 6
 - Console 0.0.1
 - Write a program called console.py that contains the entry point of the command interpreter:
Task 7
 - Console 0.1
 - Update your command interpreter (console.py)
Task 8
 - First User
 - Write a class User that inherits from BaseModel:
 - Update FileStorage to manage correctly serialization and deserialization of User.
 - Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.
Task 9
 - More classes!
 - Write all those classes that inherit from BaseModel
Task 10 
 - Console 1.0
 - Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
 - Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.
Task 11
 - All instances by class name
 - Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().
Task 12
 - Count instances
 - Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
Task 13
 - Show
 - Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).
Task 14
 - Destroy
 - Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).
Task 15
 - Update
 - Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
Task 16
 - Update from dictionary
 - Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
Task 17
 - Unittests for the Console!
 - Write all unittests for console.py, all features!
