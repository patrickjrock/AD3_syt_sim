#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

rmsd_hist <- function(data) {
  rmsd <- read.csv(data, sep="")
  p <- ggplot(subset(rmsd, c2=="c2b"), aes(x=rmsd, fill=mutant)) + geom_density() + theme_classic() + facet_grid(c2 ~.) +
    ggtitle("RMSD") 
  show(p)
}
