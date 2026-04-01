import pandas as pd

from utils import celsius_to_fahrenheit
from utils import fill_missing_mean
from utils import normalize_column


def test_celsius_to_fahrenheit():
    #Checks if 0C is really 32F -> conversion rate
    assert celsius_to_fahrenheit(5) == 41




def test_fill_missing_mean():
    df = pd.DataFrame({"test":[10,20,None]})

    result = fill_missing_mean(df, "test")

    assert result["test"].isnull().sum() == 0
    #Checks if the column has any empty values

    assert result.loc[2, "test"] == (10 + 20) / 2
    #Checks if the set value is the mean of the other values


def test_normalize_column():
    df = pd.DataFrame({"temp":[2,4,6]})

    result = normalize_column(df,"temp")

    assert result.loc[0, "temp"] == 2/6
    assert result.loc[1, "temp"] == 4/6
    assert result.loc[2, "temp"] == 1