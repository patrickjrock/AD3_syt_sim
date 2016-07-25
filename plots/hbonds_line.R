#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

hbonds <- read.csv("~/Desktop/AD3_syt_sim/data/hbonds.data", sep="")
p <- ggplot(hbonds) + geom_point(aes(x=frame, y=hbonds, color=mutant), alpha=.02) + stat_smooth(aes(x=frame, y=hbonds, color=mutant), method="loess", alpha=.5)+ 
  facet_grid(. ~ c2) + guides(colour = guide_legend(override.aes = list(alpha = 1)))
show(p)
