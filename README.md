# Immigration and Crime

This is a recently refactored, old project presenting a small enquiry into the relationship between immigration and crime. It was created as a practice exercise for a small data science project, and is not intended to be a comprehensive report on the issue.
Please treat it as a technical exploration rather than definitive research.

# Project Description
This project takes publically available ONS data for crime rates and immigration rates in the UK, explores and visualises the data, and models the relationship between the two.
The data are available on:
- Crimes: https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/datasets/policeforceareadatatables
- PFA population: https://discovery.ucl.ac.uk/id/eprint/10196619/1/pdd_quantitative_protocol_v2.0.pdf


# Repository structure:
```
─ data/
   └── external/
        ├── Crime_rates_December2022.csv <-- crime rates from December 2021 to December 2022
        ├── Crime_rates_December2023.csv <-- crime rates from December 2022 to December 2023
        ├── Crime_rates_June2015.txt     <-- crime rates from June 2014 to June 2015
        ├── Crime_rates_June2016.txt     <-- crime rates from June 2015 to June 2016
        ├── Crime_rates_June2017.txt     <-- crime rates from June 2016 to June 2017
        ├── Crime_rates_June2018.txt     <-- crime rates from June 2017 to June 2018
        ├── Crime_rates_June2019.txt     <-- crime rates from June 2018 to June 2019
        ├── Crime_rates_June2020.txt     <-- crime rates from June 2019 to June 2020
        ├── Crime_rates_June2021.txt     <-- crime rates from June 2020 to June 2021
        ├── Immigration_rates.txt        <-- immigration rates between 2010 and 2020
        ├── PFA_population.txt           <-- population data for police for areas in the UK mid 2022
        ├── georef-united-kingdom-local-authority-district/
              └── georef-united-kingdom-local-authority-district-millesime.shp <-- shapefile for UK's local authority districts
        └── Police_Force_Areas_December_2023_EW_BSC_-6977498269682743281/
              └── PFA_DEC_2023_EW_BSC.shp <-- shapefile for UK's police force areas
─ notebooks/
   └── Immigration_and_Crime_JupyterNotebook <-- report generated from the work
─ src/
   └── immigration_and_crime_src/
         └── utils.py                    <-- outsourced utility functions used in the notebooks
```

# Requirements
All the necessary requirements are listed in requirements.txt
Install these requirements using:
`pip install -r requirements.txt`

# Deliverables
The report had been compressed into a single jupyter notebook (notebooks/immigration_and_crime.ipynb).

# Contributors
@burysek

date created: 30/10/2024;
last update: 10/05/2025