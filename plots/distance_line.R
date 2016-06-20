#!/usr/bin/env Rsript 

#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

makeplot <- function(data, color, title){
  hbonds <- read.table(data, quote="\"", comment.char="")
  plot <- ggplot(hbonds, aes(x=V1, y=V2)) +
  geom_smooth() +
  geom_point(alpha=0.1) +
  xlim(0, 300) +
  ylim(0, 40) + 
  theme_classic() +
  ggtitle(title) +
  labs(x="Frame", y="Angstroms")
  return(plot)
}

p <- makeplot("distance.dat", "purple", "alpha=200, dual=on")
show(p)
