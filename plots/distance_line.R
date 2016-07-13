library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

distance <- read.csv("~/Desktop/AD3_syt_sim/data/alphadist.data", sep="")
p <- ggplot(distance) + geom_point(aes(x=frame, y=distance, color=mutant), alpha=.11) + stat_smooth(aes(x=frame, y=distance, color=mutant), method="loess") +
  facet_grid(. ~ c2)

show(p)
