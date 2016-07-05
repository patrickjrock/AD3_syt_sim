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
  theme_classic() +
  ggtitle(title) +
  labs(x="Frame", y="Hydrogen bonds")
  return(plot)
}

p1 <- makeplot("data/hbonds/hbonds_1.dat", "red", "alpha=100, dual=off")
p2 <- makeplot("data/hbonds/hbonds_2.dat", "blue", "alpha=150, dual=off")
p3 <- makeplot("data/hbonds/hbonds_3.dat", "green", "alpha=200, dual=off")
p4 <- makeplot("data/hbonds/hbonds_4.dat", "yellow", "alpha=150, dual=on")
p5 <- makeplot("data/hbonds/hbonds_5.dat", "purple", "alpha=200, dual=on")

p <- plot_grid(p1, NULL, p2, p4, p3, p5, labels=c('A', 'B', 'C', 'D', 'E', 'F'), ncol = 2)

show(p)
