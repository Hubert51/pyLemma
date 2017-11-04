## Some basic rules:
1. The assumptions and derivations should be splitted into different steps(sub proof)

## Syntax of proof operation:
1. "not" syntax
```proof
"KS1" - Sub 1         
1	A	Assumption
done

proof
"KS1"
1	|-(@A, Contradiction)	"KS1" - Sub 1   #before we use not(A), we need to declear the not format.
2	not(A)	Not Intro	1
done
```
