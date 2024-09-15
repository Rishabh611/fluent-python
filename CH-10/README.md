# Design Pattern with First-class Functions

## Strategy Pattern
- context -> strategy -> concrete starategy

- Define a family of algorithms, encapsulate each one, and make them interchangable. Strategy lets the algorithm vary independently from clients that use it.
- context
    - provides a service by delagating some computation to interchangable components that implements alternative algorithms. 
- strategy
    - the interface common to the components that implement the different algorithms
- concrete strategy
    - one of the concrete subclass of strategy
    