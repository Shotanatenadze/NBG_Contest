#installing packages

install.packages("dplyr")
install.packages("tidyr")
install.packages("ggplot2")
install.packages("magrittr")
install.packages("PerformanceAnalytics")
install.packages("hrbrthemes")
install.packages("viridis")
install.packages("cowplot")
install.packages("aTSA")

#activating packages
library(dplyr)
library(tidyr)
library(ggplot2)
library(magrittr)
library(PerformanceAnalytics)
library(hrbrthemes)
library(viridis)
library(cowplot)
library(aTSA)

#import the data

data <- read.csv(file.choose())

#transform the first column to the class of date

data$month <- strptime(data$month, format = "%m/%d/%Y")
data$month <- as.Date(data$month)

#basic descriptive statistics

mean(data$inflation)

sd(data$inflation)

quantile(data$inflation, probs = c(0.25, 0.5, 0.75))

skewness(data$inflation)

kurtosis(data$inflation)

min(data$inflation)
max(data$inflation)

#distribution plot

ggplot(data, aes(x=inflation)) +
  geom_histogram(fill="#69b3a2", color="#e9ecef", alpha=0.9) +
  ggtitle("Empirical Distribution of Inflation Rates") +
  theme_ipsum() +
  ylab(label = "") +
  xlab(label = "")+
  theme(
    plot.title = element_text(size=15)
  )


#density plot

ggplot(data, aes(x=inflation)) +
  geom_density(fill="#69b3a2", color="#e9ecef", alpha=0.9) +
  ggtitle("Density Estimation of Distribution of Inflation Rates") +
  theme_ipsum() +
  ylab(label = "") +
  xlab(label = "") + 
  theme(
    plot.title = element_text(size=15)
  )


#boxplot

ggplot(data = data, aes(x =" ", y=inflation)) + 
  geom_boxplot(fill="#69b3a2", outlier.colour = "red", outlier.shape = 8) +
  ylab("") +
  xlab("") +
  ggtitle("Boxplot")+
  scale_x_discrete(breaks = NULL) +
  theme_ipsum()


#quantile-quantile plot

ggplot(data, aes(sample = inflation)) + 
  stat_qq(color ="#69b3a2" ) + stat_qq_line() +
  theme_ipsum() +
  ggtitle("Q-Q Plot") +
  ylab("Sample") +
  xlab("Theoretical")


#time series plot

ggplot(data, aes(x = month, y = inflation)) +
  geom_line( color="#69b3a2", linetype = 'solid') + 
  xlab("") +
  theme_ipsum() +
  ylim(-5,15) +
  ggtitle("Inflation rates 1996-2020") +
  ylab("") +
  annotate(geom="text", x=as.Date("1998-12-31"), y=12.1383, 
           label="Asian financial crisis and \n the largest m/m inflation", size = 3.5) +
  annotate(geom="text", x=as.Date("2010-08-31	"), y=2.3253, 
           label="Period after the global financial crisis and \n Russo-Georgian war", size = 3.5)
  
  


#statistical dependence: ACF, PACF

acf(data$inflation)


#testing for stationarity

adf.test(data$inflation)





