#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

distance <- read.csv("~/Desktop/AD3_syt_sim/data/volume.data", sep="")
sub <- subset(distance, label=="c2a_wt_1" | label=="c2a_Y180F_1" | label=="c2a_Y180N_1")
p <- ggplot(sub) + geom_density(aes(x=volume, color=label, fill=label), alpha=.3) + theme_classic() + labs(title="Approximate volume of loop1-loop3 pocket")
show(p)
