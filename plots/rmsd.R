#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

rmsd <- function(data) {
  rmsd <- read.csv(data, sep="")
  p <- ggplot(rmsd, aes(x=frame, y=rmsd, color=c2)) + geom_line(alpha=.5) + theme_classic() + facet_grid(mutant ~.) +
    ggtitle("RMSD")
  show(p)
}
