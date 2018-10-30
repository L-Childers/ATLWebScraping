library(tidyverse)
library(ggplot2)
library(ggthemes)


#import scraped articles csv with sentiment analysis from Python
df = read.csv('abovethelaw_articles_sentiment.csv')

#perform EDA
head(df )
summary(df)

#check for missing values
sum(df$author == '')
missing_ = sum(df$publish_date == '')
sum(df$sub_title == '')
sum(df$tags == '')
sum(df$title == '')

#subsect the data to include only 5 permanent authors
df_authors = filter(df, author %in% c('Staci Zaretsky','David Lat', 'Kathryn Rubino','Joe Patrice','Elie Mystal'))


#create subjectivity chart
subjectivity_chart = ggplot(data = df_authors, aes(x = df3$subjectivity)) + geom_density(aes(color = df3$author)) + theme(plot.subtitle = element_text(vjust = 1), 
    plot.caption = element_text(vjust = 1)) +labs(title = "Subjectivity Analysis, 5 Permanent Editors", 
    x = "Subjectivity", y = "Density") + theme_few() + theme(panel.grid.major = element_line(linetype = "blank")) +labs(colour = "Authors")
median(df_authors$subjectivity)
mean(df_authors$subjectivity)


#create polarity chart
polarity_chart = ggplot(data = df_authors, aes(x = df3$polarity)) + geom_density(aes(color = df3$author)) + 
  theme(plot.subtitle = element_text(vjust = 1), plot.caption = element_text(vjust = 1)) + 
  labs(title = "Polarity Analysis, 5 Permanent Editors", x = "Polarity", y = "Density") + theme_few() + 
  theme(panel.grid.major = element_line(linetype = "blank")) +labs(colour = "Authors")
median(df_authors$polarity)
mean(df_authors$polarity)