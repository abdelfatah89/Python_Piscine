# py10

## Concept
This module introduces decorators and higher-order functions. The exercises show how to wrap behavior cleanly.

## Goals
- Understand how functions can accept and return functions.
- Implement decorators that add behavior without changing core logic.
- Combine decorators while keeping code readable.

## Key Concepts
- Higher-order functions
- Decorator syntax and `functools.wraps`
- Stacking multiple decorators
- Logging and measurement wrappers

## Inputs and Outputs
- Inputs: functions and optional decorator parameters.
- Outputs: wrapped functions with added behavior.

## Edge Cases
- Preserve function metadata with `wraps`.
- Ensure decorators pass through arguments safely.

## Usage Examples
- Wrap a function to add timing or logging.
- Stack two decorators and verify call order.

## Exercises
- decorator.py: define and apply a decorator.
- [ex0](ex0): wrap a basic function.
- [ex1](ex1): add parameter handling to a decorator.
- [ex2](ex2): combine multiple decorators.
- [ex3](ex3): measure or log function calls.
- [ex4](ex4): apply decorators to a small workflow.
