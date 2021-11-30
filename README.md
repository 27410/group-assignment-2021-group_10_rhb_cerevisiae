[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/27410/group-assignment-2021-group_10_rhb_cerevisiae/main)

# 27410 - Group assignment - Group 10 - Production of hemoglobin in *Saccharomyces cerevisiae*

## Project summary

The aim of this project was to find potential metabolic targets to optimize the production of heterologously expressed human hemoglobin in a microbial host. This can potentialy lower the price of recombinant hemoglobin to make it competitive with blood donations, and ultimately ensure a stable supply of blood for transfusions. For the production of hemoglobin we chose to use *Saccharomyces cerevisiae* as a production host, mainly because of its ability to correcty process hemoglobin. 


*S. cerevisiae* was modelled with the GSM yeast-8 and the heterologous pathway for hemoglobin was inserted as a “pseudo-reaction”. This was necessary because hemoglobin is a protein, so it could not be captured in a standard metabolic reaction. 

The main cell factory engineering strategies applied to reach the aim was gene knockouts based on the literature and computational algorithms, as well as identification of over-expression and downregulation targets. Unfortunately, the outcome of these strategies did not provide convincing evidence on how to optimise hemoglobin production in *S. cerevisiae*. For example, most of the manual knockouts resulted in reduced growth and no improvement in hemoglobin production even though other results had been observed in experimental studies. This highlighted a major limitation of the model, that it could not switch to anaerobic growth. In contrast to the manually derived knockout targets, the one found computationally with the FSEOF algorithm did identify over-expression targets with a positive impact on hemoglobin production. One of these were HemB, which could increase hemoglobin production to 81% of its maximim, while reducing growth to 20% of its maximum. 

Additional targets of the FSEOF, that were out of scope for this project may be promising to explore in the future. Importantly, further effort is needed to reach the goal of cost-efficient recombinant hemoglobin to meet the blood demands of the future safely.  



## Project overview
The repository is set up with a main report dokument detailing the main anaysis and findings
* The main report for this project can be found in the `Report.ipynb` file. Here the background, analysis and key results are presented. links that references supplementary code are located in the `Analysis` folder.  Here in debth descriptions and calcuations of the sections can be found.
* Pictures for the report is found in the `pics` folder.
* `Requirements.txt` contains the needed Python packages needed to reproduce the environment for this work.
* The `Analysis` folder contains relevant files cited in the report.  **The most relevant files are listed here.**
    * `analysis_yeast8.ipynb` contains an analysis for the main GSMM we investigated in this project. Other models investigated are names with similar nomenclature `analysis_[GSMM name]`.
    * `functions.py` contains functions we used in different notebook files
    * The subfolder `models` contains .html files of Memote reports of each GEMM we've looked at
    * `Mutant_regulation_targets2.ipynb` identifies overexpression and downregulation targets for the model `model_yeast8_rhb.xml`

