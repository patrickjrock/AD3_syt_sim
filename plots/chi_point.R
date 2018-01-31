#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

chi_point <- function(data) {
  chi <- read.csv(data, sep="")
  p <- ggplot(chi) + geom_line(aes(x=frame, y=chi2, color=mutant)) + 
    theme_classic() + facet_grid(mutant ~ c2) + ggtitle("chi density")
  show(p)
}
