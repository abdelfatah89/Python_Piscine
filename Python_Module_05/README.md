# py05

## Concept
This module centers on streaming data and pipelines. The exercises show how to read, transform, and pass data through stages.

## Goals
- Build small stream processors with clear stages.
- Transform records with predictable outputs.
- Compose pipeline steps for reuse.

## Key Concepts
- Iteration over streams
- Transform and filter steps
- Pipeline composition

## Inputs and Outputs
- Inputs: sequences of records or lines.
- Outputs: transformed records or aggregated results.

## Edge Cases
- Empty streams should yield empty outputs.
- Invalid records should be skipped or flagged.

## Usage Examples
- Process a short list of records and inspect output.
- Compose two steps and verify final results.

## Exercises
- [ex0](ex0): process a stream of records.
- [ex1](ex1): build a data stream helper.
- [ex2](ex2): run a simple pipeline.
