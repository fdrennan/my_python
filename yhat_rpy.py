import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import r, pandas2ri
import os as os
import pandas as pd


"""
cp -r /Library/Frameworks/R.framework/Versions/3.4/Resources/library/readr /Users/freddydrennan/anaconda/lib/R/library/readr
"""

# Makes conversions happen. Just write it.
pandas2ri.activate()

# Import R's version of mean to run on R objects.
mean  = robjects.r('mean')
# Import R's stats library. Like running library(stats)
stats = importr('stats')

# Use rnorm function from stats library in R
# In R this would just be rnorm(1000)
r_object = stats.rnorm(1000)

# Using our mean function imported from R
# as well as running the mean function on the r object called from R
mean(r_object)


test  = pd.read_csv('http://www.fdrennan.net/pages/pages2/datasets/housetrain.csv')

pd.DataFrame.to_csv(test, 'data/test.csv')

current_path = os.getcwd()

r_script = """
    library(dplyr, warn.conflicts = FALSE)
    x <- read.csv('/Users/freddydrennan/PycharmProjects/my_python/data/test.csv')
    x %>%
      head
"""

r(r_script)



