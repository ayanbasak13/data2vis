import pandas as pd
import numpy as np
import data_utils as utils

values = [{
    "age": "18",
    "education": "1. < HS Grad",
    "health": "1. <=Good",
    "health_ins": "2. No",
    "jobclass": "1. Industrial",
    "logwage": "4.31806333496276",
    "maritl": "1. Never Married",
    "race": "1. White",
    "region": "2. Middle Atlantic",
    "wage": "75.0431540173515",
    "year": "2006"
}, {
    "age": "24",
    "education": "4. College Grad",
    "health": "2. >=Very Good",
    "health_ins": "2. No",
    "jobclass": "2. Information",
    "logwage": "4.25527250510331",
    "maritl": "1. Never Married",
    "race": "1. White",
    "region": "2. Middle Atlantic",
    "wage": "70.4760196469445",
    "year": "Wed Jan 25"
}]

df = pd.DataFrame(values)
# print(df.dtypes)

print(utils.is_date("1-2-2019"))
