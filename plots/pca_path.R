#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")

pca_path <- function(data) {
  pca <- read.csv(data, sep="")
  c2a <- subset(pca, c2=="c2a")
  c2b <- subset(pca, c2=="c2b") 
  p <- ggplot(c2a) + geom_point(aes(x=pc1, y=pc2, color=frame)) + 
    theme_classic() + facet_grid(mutant ~ run) + ggtitle("pca path")
  show(p)
}
