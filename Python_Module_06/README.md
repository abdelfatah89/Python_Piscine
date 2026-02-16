# py06

## Concept
This module teaches Python imports and package structure. The exercises cover circular imports, module paths, and package layout.

## Goals
- Understand how Python resolves imports.
- Avoid circular import errors by structuring modules.
- Build a small package with clean boundaries.

## Key Concepts
- Module search path and `sys.path`
- Relative vs absolute imports
- Package initialization with `__init__.py`
- Circular dependency avoidance

## Inputs and Outputs
- Inputs: module names or package paths.
- Outputs: successful imports or clear error messages.

## Edge Cases
- Circular references must be refactored or delayed.
- Running modules directly can change import context.

## Usage Examples
- Import a package module and call a function.
- Compare behavior when a module is run vs imported.

## Exercises
- ft_circular_curse: explore circular import issues.
- ft_import_transmutation: practice explicit imports.
- ft_pathway_debate: inspect module search paths.
- ft_sacred_scroll: build a small package and use its modules.
