#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)
library(animation)

volume_fit_animation <- function(data) {
  volume <- read.csv(data, sep="")
  saveGIF({
  for (i in 1:100) {
    sub <- subset(volume, frame < i*20)
    print(ggplot(sub) + geom_point(aes(x=frame, y=volume, color=mutant), alpha=.02) + stat_smooth(aes(x=frame, y=volume, color=mutant), method="loess") +
      facet_grid(. ~ c2) + xlim(c(0,2000)) + ylim(c(400,1050)))
  }}, movie.name="/home/prock/Desktop/AD3_syt_sim/README_files/vol_fit.gif", interval=.1)
}
