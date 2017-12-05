## Getting Started: Basic Usage

This is for basic usage of pyLemma, i.e. you already have printers, parsers and inference rules to use

For more advanced usage of pyLemma see [Inference Rules](Inference Rules) or the API

Before continuing please look at the Notation page to understand the notation used if you haven't already

The include keyword allows system variables. It is recommended to define the "Lemma" system variable to point to the Examples directory. This is used in many of the examples, like: "$Lemma/Rules/F Rules"

First, let's look at some inference rules from the system F using the default parsers:

```
inference              #- This denotes the start of an inference
Or Intro Left          #- This denotes the name of the inference
@A                     #- The @ interprets the symbol as a wff
#----                  #- This is a comment, '#' comments out the rest of the line
or(@A,@B)              #- This is the conclusion because it is the last line
done                   #- This concludes the inference rule
```

Let's break down what this means: The important lines are the 3rd and 4th lines. They mean that if we have any sentence '@A' then we can conclude 'or(@A, @B)' where '@B' is any sentence, but '@A' must be the same as line 3

Here is an example from a proof:

```
include ../Rules/F Rules.inf

proof
Ex Mid sub2
1	A										Assumption
2	not(or(A, not(A)))						Assumption
3	or(A, not(A))							Or Intro Left			1
.	Contradiction							Contradiction Intro		3, 2
done
```

Let's break this down
```
include ../Rules/F Rules.inf
```

The first line tells the parser to include all the inference rules in the file '../Rules/F Rules.inf'

```
proof
Ex Mid sub2
...
done
```
These lines tell the parser to start the proof, what the name of the proof should be and when to end
```
1	A										Assumption
2	not(or(A, not(A)))						Assumption
These are the assumptions we made for this proof

3	or(A, not(A))							Or Intro Left			1
We used the 'Or Intro Left' rule to or together line 1 with 'not(a)'

.	Contradiction							Contradiction Intro		3, 2
```

We used 'Contradiction Intro' to create a Contradiction between lines 2 and 3

Notice that each line has a specific structure:

```
Line Index <tabs> Sentence <tabs> Inference Rule Used <tabs> Supporting Line Indexes
```
