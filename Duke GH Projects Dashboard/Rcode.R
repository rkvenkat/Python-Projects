library(tidyverse)
library(tidyr)
library(stringr)


data <- read.csv("./Downloads/python_projects/Duke Global Health Projects/final_data.tsv",sep ='\t')

data <-  rename(data,department = Dept...School)

data <- data %>% 
  janitor::clean_names()

data <- data %>% 
  mutate(faculty_a = str_replace_all(faculty,", ",";"))


df <- separate_rows(data,department,sep=",")
df <- separate_rows(df,topics,sep=",")
df <- separate_rows(df,faculty_a,sep=",")
df <- separate_rows(df,countries,sep=",")
df <- separate_rows(df,sponsors,sep=",")

df <- df %>% 
  mutate(department = str_to_title(department),
         topics = str_to_title(topics),
         faculty_a = str_to_title(faculty_a),
         contries = str_to_title(countries),
         sponsors = str_to_title(sponsors)
         )

unique(df$faculty_a)


data %>% 
  filter(str_detect(faculty,"Hy")) %>% 
  select(faculty)


df %>% 
  mutate(topics = str_to_title(topics)) %>% 
  select(topics) %>% 
  unique()



write.csv(data,"./Downloads/project_data_raw.csv")
write.csv(df,"./Downloads/project_data_split.csv")

# # of projects
n_distinct(df$id)


View(data)




