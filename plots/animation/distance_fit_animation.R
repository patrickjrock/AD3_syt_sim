#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)
library(animation)

distance_fit_animation <- function(data) {
  distance <- read.csv(data, sep="")
  saveGIF({
  for (i in 1:100) {
    sub <- subset(distance, frame < i*20)
    print(ggplot(sub) + geom_point(aes(x=frame, y=distance, color=mutant), alpha=.02) + stat_smooth(aes(x=frame, y=distance, color=mutant), method="loess") +
      facet_grid(. ~ c2) + xlim(c(0,2000)) + ylim(c(5,25)))
  }}, movie.name="~/Desktop/AD3_syt_sim/README_files/dist_fit.gif", interval=.1)
}
