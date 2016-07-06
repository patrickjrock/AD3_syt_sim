phipsi <- read.csv("~/Desktop/AD3_syt_sim/data/phipsi.data", sep="")
sub <- subset(phipsi, label=="c2a_wt_3" & (frame %% 10 == 0))
p <- ggplot(sub, aes(x=phi, y=psi))+ geom_point(aes(color=frame)) + geom_path(aes(color=frame), alpha=.1) + xlim(c(-180,180)) + ylim(c(-180,180)) + stat_density2d()
show(p)
