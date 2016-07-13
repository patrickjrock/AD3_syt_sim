#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)
library(animation)

distance <- read.csv("~/Desktop/AD3_syt_sim/data/alphadist.data", sep="")
saveGIF({
for (i in 1:100) {
  sub <- subset(distance, frame < i*20)
  print(ggplot(sub) + geom_density(aes(x=distance, fill=mutant), alpha=.3) + 
    theme_classic() + facet_grid(. ~ c2) + xlim(c(5,25)) + ylim(c(0, 0.35))+ ggtitle("Distance density"))
}}, movie.name="dist_density.gif", interval=.1) 

