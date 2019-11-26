# Version Control
  
  
## Linux 'diff'  
The diff utility is a data comparison tool that calculates the differences between two files using line-by-line comparison.
  
## My versionControl  
versionControl was implemented using typical dynamic programming practices, a 2D array of all Longest Common Subsequence subproblems was constructed and a traversal backwards storing all shared lines allowed the desired output to be constructed.
Due to assignment specifications, the output of my algorithm follows the structure:
  
  
Mismatch: &nbsp;&nbsp;&nbsp; File 1 : None &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <1 .. 1>
    
Match: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 1 : <1 .. 3> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : < 2 .. 4>
  
Mismatch: &nbsp;&nbsp;&nbsp; File 1 : <4 .. 81> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <5 .. 106>
  
Match: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 1 : <82 .. 85> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <107 .. 110>
  
Mismatch: &nbsp;&nbsp;&nbsp; File 1 : <86 .. 174> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : None
  
Match: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 1 : <175 .. 175> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <111 .. 111>
  
Mismatch: &nbsp;&nbsp;&nbsp; File 1 : <176 .. 307> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <112 .. 210>
  
Match: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 1 : <308 .. 309> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <211 .. 212>
  
Mismatch: &nbsp;&nbsp;&nbsp; File 1 : <310 .. 583> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; File 2 : <213 .. 450>
  
  
This output is far less useful in practice, but does provide an easy way to visualize file differences.
  
  
#### stringHashing
  
As seen at the top of my program, I implemented 2 string hashing functions rather than using python's built in 'hash'. This as well was a specification of the assignment. To ensure the functions were called only once per line for each file, all lines of both files were hashed twice and stored in a list of tuples. 
