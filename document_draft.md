# Introduction 

This document explains the several stages of the Quantum computing algorithm known as Shor's algorithm. 

The project comes with code for generating visualizations of a run-through of the algorithm. The document with the video should provide some rigorous mathematical and graphical intuition as to how the algorithm works. 

The document exclusively deals in describing the algorithm as rigorously and comprehensively as possible. 

Note: Majorly, we will be dealing with the Linear Algebra abstraction of quantum cicuits and states and we will rarely talk about the actual physical processes and hardware as that isn't in the scope of this project. 

# Organization: 

- A small primer on notation:
    - Explaining Dirac notation
    - The point of tensor products
    - Gates as unitary transforms

- The Actual algorithm, divided into the following parts:
    - The reduction to period finding (using number theory)
        - the mathematical reduction
        - accomplished in the run-through using a classical computer
    - Period finding using Quantum circuits
        - generating an appropriate $f$, the period of which will be relevant to the algorithm
        - Using the corresponding $U_f$ on the input state and sampling a register
        - Applying the quantum fourier transform and the motivation behind that 
        - sampling the other register
    - GCD of the multiple runs-throughs of the algorithm and conclusion (using classical hardware)

# A small primer on notation 

# The Actual algorithm

## Reduction to period finding. 

### The mathematical basis of the reduction

## Period finding using quantum circuits 

### Quantum fourier transform and general period finding 

First we will talk about Quantum fourier transform in general and talk about the approach to period finding. 

The formal statement of period finding is the following: 

we have a function $f(x)$ with the property $f(x_0) = f(x_0 + r) = f(x_0  + 2r) \ \forall x_0$ and for some $r$

It is required that we find $r$ 

Quantum Fourier transform comes with two very interesting properties that we will be using to solve this sub-problem 

- Linear Shift 
- 
