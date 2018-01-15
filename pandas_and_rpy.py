from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import pandas as pd

pandas2ri.activate()

utils = importr("utils")
dplyr = importr("dplyr", on_conflict="warn")


rstring="""
    data = read.csv('http://www.fdrennan.net/pages/pages2/datasets/housetrain.csv')
    x <- data
"""

r(rstring)

updated_df = r['x'].head(10)

r_dataframe = pandas2ri.py2ri(updated_df)


dplyr.mutate(r_dataframe, x = LotArea)

utils.head(r_dataframe)
from numpy import *
import scipy as sp
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects import r
import pandas as pd
# Necessary to use rpy2

pandas2ri.activate()

# Functions to make my life easier
def write_r(code):
    return ro.r(code)

# Get variable
def get_r(object_name):
    return pandas2ri.ri2py(r[object_name])

def load_r(package_name):
    importr(package_name)



test  = pd.read_csv('http://www.fdrennan.net/pages/pages2/datasets/housetrain.csv')


r_dataframe = pandas2ri.py2ri()



# Load R packages.
stats = importr('stats')
base  = importr('base')
dplyr = importr('dplyr', on_conflict='warn')

