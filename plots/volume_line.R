#first arg is hbond input, second file is graph output name
library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")
library(cowplot)

volume_line <- function(data) {
  volume <- read.csv(data, sep="")
  p <- ggplot(volume) + geom_line(aes(x=frame, y=volume, color=mutant)) + ylab("Cubic Angstroms") + xlab("Frame") +
    facet_grid(. ~ c2) + guides(colour = guide_legend(override.aes = list(alpha = 1))) + ggtitle("Volume of Calcium Binding Atoms") 
  show(p)
}
