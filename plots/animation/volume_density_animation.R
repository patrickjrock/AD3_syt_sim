#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)
library(animation)

volume <- read.csv("~/Desktop/AD3_syt_sim/data/alphavol.data", sep="")

saveGIF({
for (i in 1:100) {
  sub <- subset(volume, frame < i*20)
  print(ggplot() + geom_density(data = sub, aes(x=volume, fill=mutant), alpha=.3) + facet_grid(. ~ c2)  + theme_classic() + xlim(c(400,1050)) + ylim(c(0,0.0150)) )
}}, movie.name="../../README_files/vol_density.gif", interval=.1)
# movie.name="vol.gif", interval=.1, nmax=200)
