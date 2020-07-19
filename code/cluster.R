library(tidyverse)  # data manipulation
library(cluster)    # clustering algorithms
library(factoextra) # clustering visualization
library(dendextend) # for comparing two dendrograms
# 3 - 91
df <- read_csv("data/object-analysis.csv")
df <- data.frame(t(df[-1]))
df <- na.omit(df)
d <- dist(df, method = "euclidean")
hc1 <- hclust(d, method = "complete" )
par(cex = 0.5, mar=c(2, 2, 2, 12))
p <- plot(as.dendrogram(hc1), cex = 0.2, horiz = TRUE)

hc2 <- agnes(df, method = "complete")
# methods to assess
m <- c( "average", "single", "complete", "ward")
names(m) <- c( "average", "single", "complete", "ward")

# function to compute coefficient
ac <- function(x) {
  agnes(df, method = x)$ac
}

map_dbl(m, ac)
##   average    single  complete      ward 
## 0.7379371 0.6276128 0.8531583 0.9346210
hc3 <- agnes(df, method = "ward")
pltree(hc3, cex = 0.6, hang = -1, main = "Dendrogram of agnes") 
