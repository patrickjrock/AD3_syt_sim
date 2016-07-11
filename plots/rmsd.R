#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

rmsd <- read.csv("~/Desktop/AD3_syt_sim/data/alpharmsd.data", sep="")
p <- ggplot(rmsd, aes(x=frame, y=rmsd, color=mutant)) + geom_line(alpha=.5) + theme_classic() + facet_grid(run ~ c2) +
  ggtitle("RMSD")
show(p)
