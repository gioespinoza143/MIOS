# Experiment 02 — Connection

## Research Question

What is the smallest possible representation of a relationship between two MIOS Modules?

## Current Understanding

SignalType defines the shared language of MIOS.

Signals represent musical information exchanged between Modules.

Modules declare the SignalTypes they accept and produce.

The Connection must now describe how independent Modules become related without assuming the responsibilities of the Signal, Module, or MIOS Core.

## Hypothesis

A Connection describes a relationship between the output of one Module and the input of another Module.

A Connection does not process Signals, determine Module compatibility, or enforce architectural validity.

These responsibilities remain with their appropriate architectural objects.

## Experiment

Determine the minimum information a Connection must contain to truthfully describe a relationship between two Modules.