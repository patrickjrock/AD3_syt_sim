#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

volume_density <- function(data) {
  volume <- read.csv(data, sep="")
  p <- ggplot() + geom_density(data = volume[volume$frame > 50, ], aes(x=volume, fill=mutant), alpha=.3)  + theme_classic() + facet_grid(. ~ c2) +
    ggtitle("Volume density")
  show(p)
}
