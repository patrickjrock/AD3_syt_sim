function(resid, rmsf, bound, mutant, c2) {
  if(resid %in% 170:176) {
    return("loop1")
  }
  if(resid %in% 231:237) {}
  if(resid %in% 231:237) {
    return("loop3")
  }
  return("none")
}

data <- read.table("data/split_format.data", head=T)
data <- cbind(data, apply(data, 1, location))

a <- data.frame(y = data$rmsf[data$bound_mutant == 'unbound_mutant' & data$loop == 'none' & data$c2 == 'c2a'], 
                x = data$rmsf[data$bound_mutant == 'unbound_wt'& data$loop == 'none' & data$c2 == 'c2a'])

fit <- lm(y ~ x, data = a)

new.x <- data.frame(x = data$rmsf[data$bound_mutant == 'bound_wt' & data$loop == 'none'  & data$c2 == 'c2a'])
new.x <- data.frame(x = new.x[new.x$x != -1, ])
new.y <- predict(fit, newdata = new.x)

residuals1 <- data$rmsf[data$bound == 'bound_mutant' & data$c2 == 'c2a'  & data$loop == 'none' & data$rmsf != -1] - new.y

hist(residuals1, xlim = c(-20, 20), ylim = c(0, 70))

a <- data.frame(y = data$rmsf[data$bound_mutant == 'unbound_mutant' & data$loop == 'loop1' & data$c2 == 'c2a'], 
                x = data$rmsf[data$bound_mutant == 'unbound_wt'& data$loop == 'loop1' & data$c2 == 'c2a'])

fit <- lm(y ~ x, data = a)

new.x <- data.frame(x = data$rmsf[data$bound_mutant == 'bound_wt' & data$loop == 'loop1'  & data$c2 == 'c2a'])
new.x <- data.frame(x = new.x[new.x$x != -1, ])
new.y <- predict(fit, newdata = new.x)

residuals2 <- data$rmsf[data$bound == 'bound_mutant' & data$c2 == 'c2a'  & data$loop == 'loop1' & data$rmsf != -1] - new.y

hist(residuals2, col = 'blue', xlim = c(-20, 20), ylim = c(0, 70))

a <- data.frame(y = data$rmsf[data$bound_mutant == 'unbound_mutant' & data$loop == 'loop3' & data$c2 == 'c2a'], 
                x = data$rmsf[data$bound_mutant == 'unbound_wt'& data$loop == 'loop3' & data$c2 == 'c2a'])

fit <- lm(y ~ x, data = a)

new.x <- data.frame(x = data$rmsf[data$bound_mutant == 'bound_wt' & data$loop == 'loop3'  & data$c2 == 'c2a'])
new.x <- data.frame(x = new.x[new.x$x != -1, ])
new.y <- predict(fit, newdata = new.x)

residuals3 <- data$rmsf[data$bound == 'bound_mutant' & data$c2 == 'c2a'  & data$loop == 'loop3' & data$rmsf != -1] - new.y

hist(residuals3, col = 'red', xlim = c(-20, 20), ylim = c(0, 70))

print(t.test(residuals1, residuals2))

x <- c(residuals1, residuals2, residuals3)
label <- c(rep('None', length(residuals1)), rep('Loop1', length(residuals2)), rep('Loop3', length(residuals3)))

dat <- data.frame(x = x, lab = label)

p <- ggplot() +
  geom_histogram(data = dat, aes(x = x, fill = lab), binwidth = 0.5) +
  theme_bw()
show(p)