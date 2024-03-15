//code demo to illustrate oop in data 

import 'dart:io';

// Define an interface
abstract class Animal {
  void makeSound();
}

// Implement the interface
class Dog implements Animal {
  @override
  void makeSound() {
    print("Woof!");
  }
}

// Create a base class with inheritance
class Shape {
  void draw() {
    print("Drawing a shape");
  }
}

// Create a subclass that overrides a method
class Circle extends Shape {
  @override
  void draw() {
    print("Drawing a circle");
  }
}

// Create a class that reads data from a file
class FileReader {
  void readDataFromFile(String filename) {
    final file = File(filename);
    final lines = file.readAsLinesSync();
    for (final line in lines) {
      print(line);
    }
  }
}

void main() {
  // Demonstrating inheritance
  final circle = Circle();
  circle.draw(); // Output: Drawing a circle

  // Demonstrating interface implementation
  final dog = Dog();
  dog.makeSound(); // Output: Woof!

  // Initializing an instance with data from a file
  final fileReader = FileReader();
  fileReader.readDataFromFile('data.txt');

  // Demonstrating the use of a loop
  for (var i = 0; i < 5; i++) {
    print("Loop iteration: $i");
  }
}
