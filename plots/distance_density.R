#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

distance_density <- function(data) {
  distance <- read.csv(data, sep="")
  p <- ggplot(distance) + geom_density(aes(x=distance, fill=mutant), alpha=.3) + 
    theme_classic() + facet_grid(. ~ c2) + ggtitle("Distance density")
  show(p)
}
