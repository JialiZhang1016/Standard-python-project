## Standard-python-project

The purpose of the repository is to improve the existing structure of the project with the intention of enhancing its maintainability, reusability, collaboration, documentation, and testing capabilities.

### RL-manufacturing
#### 02/26 Rewrite the structure
- add `setup.py` `Makefile` to the root directory
- create some folders for different types files

```
|   Makefile
|   README.md
|   requirements.txt
|   setup.py
|
+---data
|       1st_on.npy
|       2nd_on.npy
|       both_off.npy
|       both_on.npy
|       mip-solver.xlsx
|       rate_consumption_charge.csv
|       real-case parameters-experimental-use.xlsx
|       SolarIrradiance.csv
|       WindSpeed.csv
|
+---notebooks
|       mip_plot.ipynb
|       plot_average_experiments.ipynb
|
+---scripts
|       MDP_paper_20220220_AppliedEnergyERevise.docx
|       microgrid_manufacturing_system.txt
|       sample_mixed_integer_programming_solution.txt
|
\---src
    +---RL-MANUFACTURING
    |       experiments_comparison.py
    |       microgrid_manufacturing_system.py
    |       projectionSimplex.py
    |       reinforcement_learning.py
    |       Simple_Manufacturing_System-Pure_Q-Learning.py
    |       Simple_Manufacturing_System_routine_strategy.py
    |       __init__.py
    |
    \---tests
            test_my_project.py

``` 

**Need to do**: 
- change the path of the data in the python files
- test the `Makefile`
- refine the command in `setup` and `Makefile`
