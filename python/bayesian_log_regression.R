install.packages("here")
library(here)

df <- read.csv(here("data", "cleaned", "nyts_2021_2023_clean.csv"))
df
