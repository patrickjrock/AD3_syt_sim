library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

distance_line <- function(data) {
  distance <- read.csv(data, sep="")
  p <- ggplot(distance) + geom_point(aes(x=frame, y=distance, color=mutant), alpha=.05) +
    facet_grid(run ~ c2) + guides(colour = guide_legend(override.aes = list(alpha = 1)))
  
  show(p)
}
