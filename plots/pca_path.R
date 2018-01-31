#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library("cowplot")

pca_path <- function(data) {
  pca <- read.csv(data, sep="")
  c2a <- subset(pca, c2=="c2a")
  c2b <- subset(pca, c2=="c2b") 
  p <- ggplot(c2a) + geom_point(aes(x=pc1, y=pc2, color=mutant)) + 
    theme_classic() + facet_grid(mutant ~ c2) + ggtitle("pca path")
#  p2 <- ggplot(c2b) + geom_point(aes(x=pc1, y=pc2, color=mutant)) + 
#    theme_classic() + facet_grid(mutant ~ c2) + ggtitle("pca path")
  
#  p <- plot_grid(p1,p2)
  show(p)
}
