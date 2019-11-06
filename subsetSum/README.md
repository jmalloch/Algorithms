# Subset Sum  
  
Implementations of the Brute Force & Ignorance as well as Horowitz & Sanhi subset sum algorithms. Neither algorithm runs in polynomial time, but an experiment was done to examine the relative efficienies of each algorithm.

#### Efficiency:  
The logic behind Horowitz & Sanhi's slight optimization is in the division of the overall set size `n`. Theoretically, BFI should follow O(2ⁿ) & Horowitz & Sanhi should follow O(2nⁿ/²). I tested this and plotted them against the graphs of 2ⁿ & 2nⁿ/².
![alt text](https://github.com/jmalloch/Algorithms/blob/master/subsetSum/efficiency/plot.png "Large Image")  
The timing of my algorithms was calculated using "subsetSumOperations.py", and based on the plot above, the theoretical timings appear roughly accurate.
