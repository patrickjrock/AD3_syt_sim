#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)
library(animation)

volume <- read.csv("~/Desktop/AD3_syt_sim/data/alphavol.data", sep="")
ani.record(reset=TRUE)
for (i in 1:200) {
  sub <- subset(volume, frame < i*10)
  ggplot(sub) + geom_point(aes(x=frame, y=volume, color=mutant), alpha=.11) + stat_smooth(aes(x=frame, y=volume, color=mutant), method="loess")
}

saveGIF({
for (i in 1:100) {
  sub <- subset(volume, frame < i*20)
  print(ggplot(sub) + geom_point(aes(x=frame, y=volume, color=mutant), alpha=.2) + stat_smooth(aes(x=frame, y=volume, color=mutant), method="loess") + xlim(c(0,2000)) + ylim(c(0,1000)))
}}, movie.name="vol.gif", interval=.1)
# movie.name="vol.gif", interval=.1, nmax=200)
