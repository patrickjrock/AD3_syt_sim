#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

volume <- read.csv("~/Desktop/AD3_syt_sim/data/alphavol.data", sep="")
p <- ggplot(volume) + geom_point(aes(x=frame, y=volume, color=mutant), alpha=.11) + stat_smooth(aes(x=frame, y=volume, color=mutant), method="loess")
show(p)