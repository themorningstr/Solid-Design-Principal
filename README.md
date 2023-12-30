# Solid-Design-Principal



Solid Design Pattern
    1. Single Responsibility Principal - SRP or SOC
            a. A class should have one reason to change.
            b. Seperation of concern - different classes handling different. independent task/problems

    2. Open Close Principal- OCP
            a. Class should be open for extension but closed for modification.

    3. Liskov Substitution Principal - LSP
            a. you should be able to Substitute a base type for a subtype.

    4. Interface Segregation Principal - ISP
            a. Don't put too much into an inference; split into separate interfaces.
            b. YAGNI :- You Ain't Going to Need It.

    5. Dependency Inversion Principal - DIP
            a. High Level Module should not depend upon low level ones; use abstractions.




Gamma Categorization
    A. Design Pattern are typically split into three categories
    B. This is called Gamma Categorization after Erich Gamma.

            Creational Pattern
                a. Deal with the creation(Construction) of objects
                b. Explict(Constructor) Vs. Implict(DI, reflection)
                c. Wholesale (single statement) Vs. Piecewise(step by step)
                    1. Builder
                        a. Some objects are simple and can be created in a single initializer call, while other objects require a lot of ceremony to create, 
                            having an object with 10 initializer argument is not productive, hence opt for piecewise construction.
                        b. builder provides an API for constructing an object step by step.
                        c. When piecewise object constructions is complicated, provides an API for doing it more succinctly.
                    2. Factories
                        1. Abstract Factory
                        2. Factory Method
                    3. Prototype
                    4. Singleton

            Structural Pattern
                a. Concerned with the structure(e.g., class members)
                b. Many pattern are wrappers that mimic the underlying class inference
                c. Stress the importance of good API Design
                    1. Adapter
                    2. Bridge
                    3. Composite
                    4. Decorator
                    5. Facade
                    6. Flyweight
                    7. Proxy

            Behavioral Pattern
                a. They are all different; no central theme

                    1. Chain of Responsibility
                    2. Command
                    3. Interpreter
                    4. Iterator
                    5. Mediator
                    6. Observer
                    7. State
                    8. Stretegy
                    9. Template Memory
                    10. Visitor

    
