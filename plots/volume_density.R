#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

volume <- read.csv("~/Desktop/AD3_syt_sim/data/volume.data", sep="")
p <- ggplot(volume) + geom_density(aes(x=volume, color=factor(mutant), fill=factor(mutant)), alpha=.3)  + theme_classic() + facet_grid(run ~ c2)
show(p)
