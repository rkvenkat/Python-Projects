
library(tidyverse)
library(tidytuesdayR)
library(scales)
library(gt)
library(ggtext)
library(lubridate)

theme_set(theme_light())


df <-  read_csv("./Downloads/python_projects/Priority Voucher/dataset - cleaned.csv")

View(df)

data <- df %>% 
        separate(title,c("a","category"),";") %>% 
        select(-a) %>% 
        mutate(category = str_trim(category),
               generic_name = str_trim(str_extract(drug,"(?<=\\()(.*?)(?=\\))")),
               brand_name = str_replace_all(drug,"(?=\\()(.*?)(?<=\\))",""),
               brand_name = str_to_upper(str_replace_all(str_to_lower(brand_name),c("injection",","),"")),
               brand_name = str_replace_all(brand_name,"INJECTION",""),
               brand_name = str_trim(brand_name)) %>% 
        select(-drug)



View(data) 

data %>% 
  select(-link) %>% 
  gt::gt() %>% 
  fmt_date(
    columns = pub_date,
    date_style = 5
  ) 


a <- data %>%
  group_by(year(pub_date),category) %>% 
  summarize(n()) %>% 
  rename("year" = 1,
         "count" = 3)

a %>% 
  ggplot(aes(fill = category,x=year,y=count)) +
  geom_bar(stat='identity') +
  scale_y_continuous(breaks = 0:10) +
  scale_x_continuous(breaks = 2014:2022) +
  theme_minimal() +
  labs(
    title = "Priority Review Vouchers issued by FDA for approved drugs*",
    subtitle = "*approved drug application meeting criteria for a priority review voucher",
    caption = "Source: Issuance of Priority Review Voucher notices scraped from federalregister.gov",
    fill = "Category"
  )  +
  xlab("Issuance Year") +
  scale_fill_discrete(labels = c("Material Threat\nMedical Countermeasure\nProduct","B")) +
  theme(axis.text.x = element_markdown(color = "black",
                                       hjust = 0.5,
                                       size = 12), 
        axis.text.y = element_markdown(color = "black",
                                       hjust = 0.5,
                                       size = 12),
        axis.title.x = element_markdown(color = "black",
                                      hjust = 0.5,
                                      size = 12),
        plot.caption = element_markdown(color = "black",
                                        size = 10.5,
                                        lineheight = 1.3,
                                        hjust = 0,
                                        margin = margin(30, 0, 20, 20)),
        plot.margin = margin(10, 20, 10, 20),
        plot.title = element_text(size = 19, color = "black", 
                               face = "bold"),
        axis.title.y = element_blank(),
        panel.grid.minor = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        ) 
  
  