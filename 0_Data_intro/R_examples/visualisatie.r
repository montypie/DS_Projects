#%% importeer tidyverse
library(tidyverse)

#%% importeer data
library(palmerpenguins)

#%%
View(penguins)

#%%
dataset<-penguins

#%%
str(dataset) # structure

#%%
summary(dataset) # df_info

# Examples are taken from https://r4ds.hadley.nz/
#%% VISUALIZATION
library(ggplot2)

#%% making a graph
ggplot(data = penguins,
       mapping = aes(x = flipper_length_mm, y = body_mass_g)) +
       geom_point(mapping = aes(color = species, shape = sex)) +
       geom_smooth(method = "lm") +
       labs(title = "Flipper length vs Body mass",
            x = "Flipper length, mm",
            y = "Body mass, g",
            color = "Specie",
            shape = "Gender") +
       ggthemes::scale_color_colorblind() # (ggthemes:: - because lib ggthemes is not loaded)

#%% DATA TRANSFORMATIONS (with dplyr)
library(dplyr)
library(mtcars)
#%%
str(mtcars)

#%%
dataset<-mtcars
summary(dataset)

#%% Factors defineren (bv. nummers uit colomn 'cyl' naar een caterogy transformeren)
dataset$cyl<-as.factor(dataset$cyl)
summary(dataset) # vergelijk met de summary voor de transformatie

#%% Piping in dplyr (and put result in a variable):
dataset_summary<-dataset %>% group_by(cyl) %>%
  summarise(avg = mean(mpg))
# (in newer versie van dplyr %>% is replaced with |>)

# SELECT cyl, AVG(mpg)
# FROM mtcars
# GROUP BY cyl;

#%%
# Alternatively using SQL instead of dplyr (with duckdb)

# Create connection with duckdb
library(duckdb)
conn <- dbConnect(duckdb())

# Register dataset  (link to a table w/o loading it in the memory)
dbWriteTable(conn, "mtcars", mtcars)

# Execute a query
result <- dbGetQuery(conn, "SELECT cyl FROM mtcars")

#%%
# A bigger db: 
library(nycflights13)
str(flights)

#%%
flights |> 
  filter(dep_delay > 120)

#%%
jan1 <- flights |>
  filter(month == 1 & day == 1)

#%%
flights |>
  filter(dest == "IAH") |> 
  group_by(year, month, day) |> 
  summarize(
    arr_delay = mean(arr_delay, na.rm = TRUE)
  )

#%%
# Find all unique origin and destination pairs
flights |> 
  distinct(origin, dest)