---
## Overview ##
This repository corresponds to the construction of the triality web of all the models found in [[1]](https://arxiv.org/pdf/2203.15816.pdf). The steps used to perform triality can be found in [[2]](https://arxiv.org/pdf/1602.01834.pdf#page=11). The triality web was constructed automatically using the algorithm found in [[this script]](https://github.com/mcarc011/Polytopes-TrialityWeb/blob/master/polytopes2.py). The code itself is commented which tries to give details of each step. Models whose triality web were not found (because they seemed unbounded/the algorithm kept constructing new theories) have a crossed out and broken link. The results are formatted so that each model has a link which takes you to a subdirectory and displays the results of the web. On the landing page you will see the initial phase followed by a table that shows how each phase is related. The number on the lookup table references the node that needs to be dualized to go from the phase referenced in a row to the phase referenced in the column. A negative number denotes inverse triality. Thus the numbers shown correspond to how the phases are labeled for the phase referenced for the row. For example:

<div align="center">
  
||Phase 1|Phase 2|
|---|---|---|
Phase 1||-2, -3, 4, 5|
Phase 2|2, -3||
  
</div>

This means that applying triality on node 5 of [[this phase]](https://github.com/mcarc011/Polytopes-TrialityWeb/blob/master/figs/model3/model3_phase_0.png) yields [[phase 2]](https://github.com/mcarc011/Polytopes-TrialityWeb/blob/master/figs/model3/model3_phase_1.png) when relabeled. Clicking on the phase in the tables found in the subdirectories will take you to the figure corresponding to that phase. [[This file]](https://github.com/mcarc011/Polytopes-TrialityWeb/blob/master/testmatrix.py) shows the matrices that were inputted for each of the corresponding models found in [[1]](https://arxiv.org/pdf/2203.15816.pdf). These can be use as input for [[this script]](https://github.com/mcarc011/Polytopes-TrialityWeb/blob/master/polytopes2.py) and was used to generate the results found in the subdirectories. Various other scripts not in the repository were used to generate these results including a graphing tool, a matrix input tool (generated the matrix input file), and some testing scripts which attempted to verify the results. These were left out to simplify the repository.

---
## Results ##

<div align="center">
  
|   |   |   |   |   |
|---|---|---|---|---|
[Model 1](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model1)|[Model 2](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model2)|[Model 3](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model3)|[Model 4](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model4)|[Model 5](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model5)|
[Model 6](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model6)|[Model 7](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model7)|[Model 8](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model8)|~~[Model 9](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model9)~~|~~[Model 10](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model10)~~|
[Model 11](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model11)|[Model 12](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model12)|~~[Model 13](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model13)~~|~~[Model 14](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model14)~~|~~[Model 15](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model15)~~|
~~[Model 16](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model16)~~|~~[Model 17](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model17)~~|~~[Model 18](https://github.com/mcarc011/Polytopes-TrialityWeb/tree/master/figs/model18)~~

</div>
  

----
## References ##
[[1] https://arxiv.org/pdf/2203.15816.pdf](https://arxiv.org/pdf/2203.15816.pdf)

[[2] https://arxiv.org/pdf/1602.01834.pdf](https://arxiv.org/pdf/1602.01834.pdf)

[[3] https://arxiv.org/pdf/1801.00799.pdf](https://arxiv.org/pdf/1801.00799.pdf)

[[4] https://link.springer.com/article/10.1007/JHEP01(2022)058](https://link.springer.com/article/10.1007/JHEP01(2022)058)
