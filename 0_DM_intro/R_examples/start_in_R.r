# Initialize renv environment
getwd()


renv::init()

# Install tidyverse package
renv::install("tidyverse")

# Take a snapshot to lock the package versions
renv::snapshot()

# Handbook
# https://r4ds.hadley.nz/