# SetCoveringProblem-eng
An algorithm to solve TheSetCoveringProblem

## Overview

The set coverage problem (SCP) is a combinatorial optimization problem used to find the most
efficient way to cover a set of elements with a set of subsets. Formally, the problem can be
defined as follows:
Given a set of elements E and a set of subsets S that cover E, find the subset of S that uses as few
elements as possible to cover all E.

For example:

E = {1, 2, 3, 4, 5} (Set of elements to cover)
S = {{1, 2}, {2, 3}, {3, 4}, {4, 5}} (Set of subsets)

In the first iteration, the subset {1, 2} is selected because it covers elements {1, 2}. In the second
iteration, the {3, 4} subset is selected because it covers {3, 4} elements. In the third iteration, the
{4, 5} subset is selected because it covers the remaining {5} elements. Therefore, the solution is
{{1, 2}, {3, 4}, {4, 5}}. In case each subset has a cost, the solution has to select the subset that have
the lowest cost and fill the set E.
This problem is NP-complete, which means that there is no known algorithm that can solve this
problem in polynomial time. However, there are approximation algorithms that can provide nearoptimal solutions.
Selected heuristics
The heuristic that I will be working on basically what it does is:
1. Search within the universe set for the subset that has the highest value using the formula:
number 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 𝑡ℎ𝑎𝑡 𝑐𝑜𝑣𝑒𝑟𝑠 𝑖𝑛 𝑡ℎ𝑒 𝑢𝑛𝑖𝑣𝑒𝑟𝑠𝑒
𝑐𝑜𝑠𝑡
2. Select the subset that gives a higher result
3. Delete the selected subset from the universe set.
4. Repeat the cycle until the universe is empty.
5. Print the result

## Pseudocode:

Start
Initialize U = (Universe set)
Initialize S = (Set of subsets)
Initialize C = (Set of subsets)
i=0, costo_total = 0, selected_sets = []
max_value = 0
#temporal Variables:
Cost_temp = 0, Selected_temp = []
While U is not empty
  max_value = length(S[ 0 ] & U) / cost[ 0 ]
  While j ≤ length(s)
    If length(S[ j ] & U / cost[ j ]) >= max_value :
      max_value = length(S[ 0 ] & U) / cost[ 0 ]
      Selected_temp = S[ j ]
      Cost_temp = C[ j ]
      j = j+1
  selected_sets += Selected_temp
  costo_total += Cost_temp
Print conjuntos_seleccionados and costo_total
End

## Instance benchmark

The dataset I used to perform my tests of the algorithm was from the OR library, of which I take as
a base the scp41 instances ... scp410

Link: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html

The format of these files is:
number of rows (m), number of columns (n)
The cost of each column C(J), J=1,..,n
For each row i (i=1,...,m): the number of columns that cover
row i followed by a list of the columns that cover row i
