# 01_OpenSourceModeling

Copyright Josef Zeininger

This project is released under an MIT LICENSE. [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

I Created this repository for the lecture Open-Source Energy System Modeling, TU Wien, VU 370.062.

AI was used for structuring and coding syntax assistance. [![AIuse: cgatGPT](https://img.shields.io/badge/AI_used-chatGPT-blue)](chatgpt.com)

## Funtions

1. celsius_to_fahrenheit()

   Converts a given temperature from degree Celsius into Fahrenheit.
3. fill_missing_mean()
   
   Fills empty data points in a pandas.DataFrame with the column mean value.
5. normalize_column()
   
   Normalizes a column in between -1 and 1 by dividing by the absolute maximum value in the column.
   
## Installations

The code in this project requires the pandas library.

pip install -r requirements.txt

## Running Test
Test for each function have been implemented.

pytest

## Continuous Integration 

Tests are automatically executed using GitHub Actions on every push. ![CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)




