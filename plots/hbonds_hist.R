#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

hbonds <- read.csv("~/Desktop/AD3_syt_sim/data/hbonds.data", sep="")
p <- ggplot(hbonds) + geom_density(aes(x=hbonds, color=mutant), alpha=0.5) +
  facet_wrap(~c2)
show(p)
