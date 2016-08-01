# RMSF plots
require(ggplot2)
require(cowplot)

location <- function(resid, rmsf, bound, mutant, c2) {
  if(resid %in% 170:176) {
    return("loop1")
  }
  if(resid %in% 231:237) {
    return("loop3")
  }
  if(resid %in% 300:307) {
    return("loop1")
  }
  if(resid %in% 364:371) {
    return("loop3")
  }
  return("none")
}

rmsf_plot <- function(lp, data, title, xlab, ylab) {
  x <- subset(data, mutant=="wt" & loop==lp )
  y <- subset(data, mutant!="wt" & loop==lp )
  p <- qplot(x$rmsf, y$rmsf, color=factor(x$resid)) + xlim(0,3) + ylim(0,3) + ggtitle(title) + xlab(xlab) + ylab(ylab) +
    geom_abline(intercept=0, slope=1) + guides(color=guide_legend(title="Residue ID"))
  return(p)
}

bound_rmsf <- read.table("data/rmsf_bound.data", head=T) 
unbound_rmsf <- read.table("data/rmsf_unbound.data", head=T)

bound_rmsf <- cbind(bound_rmsf, loop = apply(bound_rmsf, 1, location))
unbound_rmsf <- cbind(unbound_rmsf, loop = apply(unbound_rmsf, 1, location))


c2a_bound <- subset(bound_rmsf, c2=="c2a")
c2b_bound <- subset(bound_rmsf, c2=="c2b")
c2a_unbound <- subset(unbound_rmsf, c2=="c2a")
c2b_unbound <- subset(unbound_rmsf, c2=="c2b")

# loop-1
#x <- subset(c2a_bound, mutant=="wt" & loop=="loop1" )
#y <- subset(c2a_bound, mutant=="Y180N" & loop=="loop1" )
#p <- qplot(x$rmsf, y$rmsf) + xlim(0,3) + ylim(0,3) + ggtitle("C2A loop1 bound") + xlab("Wild Type RMSF") + ylab("Y180N RMSF") +
#  geom_abline(intercept=0, slope=1) 
#show(p)

p1 <- rmsf_plot("loop1", c2a_bound, "C2A loop1 bound", "Wild Type RMSF", "Y180N RMSF")
p2 <- rmsf_plot("loop1", c2a_unbound, "C2A loop1 unbound", "Wild Type RMSF", "Y180N RMSF")

p3 <- rmsf_plot("loop1", c2b_bound, "C2B loop1 bound", "Wild Type RMSF", "Y311N RMSF")
p4 <- rmsf_plot("loop1", c2b_unbound, "C2B loop1 unbound", "Wild Type RMSF", "Y311N RMSF")

p5 <- rmsf_plot("loop3", c2a_bound, "C2A loop3 bound", "Wild Type RMSF", "Y180N RMSF")
p6 <- rmsf_plot("loop3", c2a_unbound, "C2A loop3 unbound", "Wild Type RMSF", "Y180N RMSF")

p7 <- rmsf_plot("loop3", c2b_bound, "C2B loop3 bound", "Wild Type RMSF", "Y311N RMSF")
p8 <- rmsf_plot("loop3", c2b_unbound, "C2B loop3 unbound", "Wild Type RMSF", "Y311N RMSF")

grid1 <- plot_grid(p1,p3,p5,p7)
grid2 <- plot_grid(p2,p4,p6,p8)
