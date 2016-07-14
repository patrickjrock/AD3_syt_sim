library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

distance_line <- function(data) {
  distance <- read.csv(data, sep="")
  p <- ggplot(distance) + geom_point(aes(x=frame, y=distance, color=mutant), alpha=.02) + stat_smooth(aes(x=frame, y=distance, color=mutant), method="loess") +
    facet_grid(. ~ c2)
  
  show(p)
}
