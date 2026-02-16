# py02

## Concept
This module is about exceptions and robust error handling. The exercises cover built-in errors, custom exceptions, and safe control flow.

## Goals
- Understand how Python raises and handles exceptions.
- Create custom exceptions for domain rules.
- Ensure cleanup or final steps always run.

## Key Concepts
- `try`/`except`/`finally`
- Built-in exception types
- Custom exception classes
- Raising errors intentionally

## Inputs and Outputs
- Inputs: values that may be invalid or unexpected.
- Outputs: error messages, fallback values, or successful results.

## Edge Cases
- Catch only the exceptions you expect.
- Avoid swallowing errors without logging or handling.
- Ensure `finally` runs for cleanup logic.

## Usage Examples
- Trigger an error path and confirm the message.
- Test a valid path to ensure normal output still works.

## Exercises
- [ex0](ex0): raise and handle a first exception.
- [ex1](ex1): compare different error types.
- [ex2](ex2): define and use custom errors.
- [ex3](ex3): use a `finally` block correctly.
- [ex4](ex4): raise errors intentionally when rules fail.
- [ex5](ex5): apply error handling to a small management task.
