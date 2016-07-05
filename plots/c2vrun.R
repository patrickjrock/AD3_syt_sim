require(ggplot2)

volume <- read.csv("~/Desktop/AD3_syt_sim/data/volume.data", sep="")

sub <- subset(volume, mutant=="wt")
p <- ggplot(sub) + geom_density(aes(x=volume, color=factor(run), fill=factor(run)), alpha=.05)  + theme_classic() + facet_grid(. ~ c2)
show(p)
