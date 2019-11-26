# Version Control
  
  
## Linux 'diff'  
The diff utility is a data comparison tool that calculates the differences between two files using line-by-line comparison.
  
## My versionControl  
versionControl was implemented using typical dynamic programming practices, a 2D array of all Longest Common Subsequence subproblems was constructed and a traversal backwards storing all shared lines allowed the desired output to be constructed.
Due to assignment specifications, the output of my algorithm follows the structure:
  
  
Mismatch: File 1 : None File 2 : <1 .. 1>
  
Match: File 1 : <1 .. 3> File 2 : < 2 .. 4>
  
Mismatch: File 1 : <4 .. 81> File 2 : <5 .. 106>
  
Match: File 1 : <82 .. 85> File 2 : <107 .. 110>
  
Mismatch: File 1 : <86 .. 174> File 2 : None
  
Match: File 1 : <175 .. 175> File 2 : <111 .. 111>
  
Mismatch: File 1 : <176 .. 307> File 2 : <112 .. 210>
  
Match: File 1 : <308 .. 309> File 2 : <211 .. 212>
  
Mismatch: File 1 : <310 .. 583> File 2 : <213 .. 450>
  
  
This output is far less useful in practice, but does provide an easy way to visualize file differences.
  
  
#### stringHashing
  
As seen at the top of my program, I implemented 2 string hashing functions rather than using python's built in 'hash'. This as well was a specification of the assignment. To ensure the functions were called only once per line for each file, all lines of both files were hashed twice and stored in a list of tuples. 
