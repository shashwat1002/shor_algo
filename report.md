# Report 

## Content in the submission 

This is a document can be considered as a collection of proofs and lemmas leading up to the Shor's algorithm. The math discussed in the document uses the Linear Algebra computational basis abstraction for quantum phenomena as opposed to wave mechanics. At this point, we must note that they're equivalent in what they can express regarding things we will be talking about but the authors feel that the abstraction is more expressive when it comes to discussing algorithms. 

## Visualizations?

While we believe that the document in the submission represents a rigorous and exhaustive build up to the Shor's algorithm, we must note that this wasn't the original goal of the project. 

The original goal of the project was to provide an intuitive visualization to quantum algorithms (and the math behind them). On this count, we have failed and the report is a summary of our efforts throughout the project and attempts that were abandoned  (and reasons for abandon). 

### Approaches considered 

#### Circuits 

One must note here that there are several good ways of visualizing a quantum circuit. One, that caught our attention is a visual language called z-x calculus. The calculus provides a set of rules to represent, simplify, and optimize quantum circuits while keeping the logic intact. 

The reason we abandoned z-x calculus or any other representation concerning quantum circuits is because they give little no intuition on how the algorithms work or how one must approach a problem from the quantum computing perspective.

Resource: <https://zxcalculus.com/>



#### Matrices 

The second approach we considered was showing the state vectors as the transformations were applied. The motivation behind this was, seeing the matrices evolve would give the viewer an idea idea of how collapses and partial collapses of entangled states manifest themselves. 

This approach was abandoned due a constraint of the Shor's algorithm:

As mentioned in the submission documents, the Shor's algorithm requires an input register with at least $2n$ qubits (where $n = \lfloor \log_2 N \rfloor$ and $N$ is the number being factorized ) and one $n$ qubit output register. This implies that at any point in the computation, the state vector is a member of $\mathbb{C} ^{2^{3n}}$ vector space. So Hypothetically if we wanted to follow the computational space during the factorization of a relatively small number like $15$, we would have a vector of $4096$ elements on the screen. 

We even considered showing the input registers and the output registers separately somehow (which is not always possible neatly because the Shor's algorithm at a particular entangles them), even in this case we would be dealing with a vector of $256$ elements which is still a bad option. 



#### Bloch sphere 

The most popularly used visualization of qubits is the bloch sphere sphere representation. We considered whether several Bloch spheres or some version thereof can be used to track the qubits through the computation. 

This poses very similar problems as the last proposed approach: 

- There are points during computation of the Shor's algorithm where individual qubits (or registers) can't be shown independently of each other. 

- A bloch sphere deals with one qubit _only_

# General challenges we faced 

One of the primary challenges of this undertaking was to understand the basics of quantum computing and quantum parallelism enough so as to make comprehensive connections and proofs. 

One thing was clear to from the get go: any visualization we thought up should be rigorous as well as intuitive. This required to us have a very good grasp of the new paradigm before we could even start brainstorming. 

# Conclusion

Our initial project proposal was an ambitious one, which we had known from the beginning,
but it seems we had still grossly underestimating the scope of what we had undertaken.
However, despite not being able to achieve a rigorous visualization of Shor's algorithm,
we do not regret taking this up as our project, and learnt a lot and hope that product
of our work is nonetheless useful to anyone entering the field.
