[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/27410/group-assignment-2021-group_10_rhb_cerevisiae/main)

# 27410 - Group assignment - Group 10 - Production of hemoglobin in *Saccharomyces cerevisiae*
> Dear students, thank you for accepting the group assignment. Please fill in the
> requested information below and above ([Group Number] and [TITLE]) and remove this quoted part before submission (everything prepended with a >).
> Please also replace `[PUT-YOUR-REPOSITORY-HERE]` up in the first line 👆 with the name of your repository here on GitHub.

> That way someone can click on the Binder badge icon and open your project in Jupyter lab to explore it.
> For this to work you will also have to keep `requirements.txt` up to date (by running `pip freeze > requirements.txt`).
> Furthermore, this will only work if you decide to make your repository public (which you can do under Settings -> Options),
> which I would encourage you to do – up to you. A lot of good science happens out in the open these days.
> Good luck!

## Project summary (<300 words)
> Describe the overall aim of your project and what you have achieved.

The aim of this project was to find potential metabolic targets to optimize the production of heterologously expressed human hemoglobin in a microbial host. This can potentialy lower the price of recombinant hemoglobin to make it competitive with blood donations, and ultimately ensure a stable supply of blood for transfusions. For the production of hemoglobin we chose to use *Saccharomyces cerevisiae* as a production host, mainly because of its ability to correcty process hemoglobin. 


*S. cerevisiae* was modelled with the GSM yeast-8 and the heterologous pathway for hemoglobin was inserted as a “pseudo-reaction”. This was necessary because hemoglobin is a protein, so it could not be captured in a standard metabolic reaction. 

The main cell factory engineering strategies applied to reach the aim was gene knockouts based on literature and computational algorithms, as well as identification of over-expression and downregulation targets. Unfortunately, the outcome of these strategies did not provide convincing evidence on how to optimise hemoglobin production in S. cerevisiae. For example, most of the manual knockouts resulted in reduced growth and no improvement in hemoglobin production even though other results had been observed in experimental studies. This highlighted a major limitation of the model, that it could not switch to anaerobic growth. In contrast to the manually derived knockout targets, the one found computationally with the FSEOF algorithm did identify over-expression targets with a positive impact on hemoglobin production. One of these were HemB, which could increase hemoglobin production to 81% of its maximim, while reducing growth to 20% of its maximum. 

Additional targets of the FSEOF, that were out of scope for this project may be promising to explore in the future. Importantly, further effort is needed to reach the goal of cost-efficient recombinant hemoglobin to meet the blood demands of the future safely.  



## Project overview
The repository is set up with a main report dokument detailing the main anaysis and findings
* The main report for this project can be found in the Report.ipynb file. Here the background, analysis and key results are presented. links that references supplementary code are located in the Analysis folder.  Here in debth descriptions and calcuations of the sections can be found.
* Pictures for the report is found in the pics folder.
* Requirements.txt contains the needed Python packages needed to reproduce the environment for this work.
* The Analysis folder contains...
    * ...
    * ...

