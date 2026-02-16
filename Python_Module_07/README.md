# py07

## Concept
This module is about object-oriented design. The exercises build a card game style system with inheritance, interfaces, and strategies.

## Goals
- Model entities with classes and inheritance.
- Use interfaces or mixins to share behavior.
- Separate rules, strategies, and engine logic.

## Key Concepts
- Classes, inheritance, and polymorphism
- Composition and delegation
- Strategy pattern
- Ranking and tournament flow

## Inputs and Outputs
- Inputs: card definitions, deck lists, or match results.
- Outputs: game state changes or ranked results.

## Edge Cases
- Invalid card data should be rejected clearly.
- Strategy logic should handle empty decks.
- Ranking should handle ties consistently.

## Usage Examples
- Create a small deck and run a simulated match.
- Swap strategies and observe different outcomes.

## Exercises
- [ex0](ex0): define base card classes and simple gameplay.
- [ex1](ex1): extend cards and manage decks.
- [ex2](ex2): add combat and magical traits.
- [ex3](ex3): implement strategies and a game engine.
- [ex4](ex4): add ranking and tournament logic.
