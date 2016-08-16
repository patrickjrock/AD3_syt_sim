# RMSF plots
require(ggplot2)
require(cowplot)
require(plyr)

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
  if(resid %in% 330:337) {
    return("loop2")
  }
  if(resid %in% 197:204) {
    return("loop2")
  }
  return("none")
}

rmsf_plot <- function(lp, data, title, xlab, ylab) {
  x <- subset(data, mutant=="wt" & loop==lp )
  y <- subset(data, mutant!="wt" & loop==lp )
  p <- qplot(x$rmsf, y$rmsf) + xlim(0,3) + ylim(0,3) + xlab("") + ylab("") +
    geom_abline(intercept=0, slope=1)
  return(p)
}

all_residuals <- function(data, title) {
  x <- data$rmsf[data$mutant=="wt"]
  y <- data$rmsf[data$mutant!="wt"]
  residuals <- y-x
  r <- data.frame(residuals = residuals, title = title) 
  return(r)
}


get_residuals <- function(lp, data, title) {
  x <- data$rmsf[data$mutant=="wt" & data$loop==lp]
  y <- data$rmsf[data$mutant!="wt" & data$loop==lp]
  residuals <- y-x
  r <- data.frame(residuals = residuals, title = title) 
  return(r)
}

rmsf_total <- read.table("~/Desktop/AD3_syt_sim/data/rmsf_pot.data", head=T)
bound_rmsf <- subset(rmsf_total, bound=="bound") 
unbound_rmsf <- subset(rmsf_total, bound=="unbound")

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

p5 <- rmsf_plot("loop2", c2a_bound, "C2A loop2 bound", "Wild Type RMSF", "Y180N RMSF")
p6 <- rmsf_plot("loop2", c2a_unbound, "C2A loop2 unbound", "Wild Type RMSF", "Y180N RMSF")

p7 <- rmsf_plot("loop2", c2b_bound, "C2B loop2 bound", "Wild Type RMSF", "Y311N RMSF")
p8 <- rmsf_plot("loop2", c2b_unbound, "C2B loop2 unbound", "Wild Type RMSF", "Y311N RMSF")

p9 <- rmsf_plot("loop3", c2a_bound, "C2A loop3 bound", "Wild Type RMSF", "Y180N RMSF")
p10 <- rmsf_plot("loop3", c2a_unbound, "C2A loop3 unbound", "Wild Type RMSF", "Y180N RMSF")

p11 <- rmsf_plot("loop3", c2b_bound, "C2B loop3 bound", "Wild Type RMSF", "Y311N RMSF")
p12 <- rmsf_plot("loop3", c2b_unbound, "C2B loop3 unbound", "Wild Type RMSF", "Y311N RMSF")




grid1 <- plot_grid(p5,p6)
grid2 <- plot_grid(p7,p8)
grid3 <- plot_grid(p1,p2)
grid4 <- plot_grid(p3,p4)

grid5 <- plot_grid(p9,p10)
grid6 <- plot_grid(p11,p12)

r1 <- get_residuals("loop1", c2a_bound, "C2A loop1 bound")
r2 <- get_residuals("loop1", c2a_unbound, "C2A loop1 unbound")

r3 <- get_residuals("loop1", c2b_bound, "C2B loop1 bound")
r4 <- get_residuals("loop1", c2b_unbound, "C2B loop1 unbound")

r5 <- get_residuals("loop3", c2a_bound, "C2A loop3 bound")
r6 <- get_residuals("loop3", c2a_unbound, "C2A loop3 unbound")

r7 <- get_residuals("loop3", c2b_bound, "C2B loop3 bound")
r8 <- get_residuals("loop3", c2b_unbound, "C2B loop3 unbound")

r9 <- get_residuals("none", c2b_bound,  "C2B calphas bound")
r10 <- get_residuals("none", c2b_unbound, "C2B calphas unbound")


r11 <- get_residuals("loop2", c2b_bound,  "C2B loop2 bound")
r12 <- get_residuals("loop2", c2b_unbound,  "C2B loop2 unbound")

