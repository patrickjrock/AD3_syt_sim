#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

chi_point <- function(data) {
  chi <- read.csv(data, sep="")
  p <- ggplot(chi) + geom_histogram(aes(x=chi2), alpha=.8) + 
    theme_classic() + facet_grid(c2 ~ mutant) + ggtitle("His 237 Chi 2")
  show(p)
}
