library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")

rmsf <- read.csv("./data/rmsf.data", sep="")
rsa <- read.csv("./data/rsa.data", sep="")
merge <- merge(rmsf,rsa)


lm_eqn <- function(df){
    m <- lm(rmsf ~ rsa, df);
    eq <- substitute(italic(y) == a + b %.% italic(x)*","~~italic(r)^2~"="~r2, 
         list(a = format(coef(m)[1], digits = 2), 
              b = format(coef(m)[2], digits = 2), 
             r2 = format(summary(m)$r.squared, digits = 3)))
    as.character(as.expression(eq));                 
}


p <- ggplot(merge, aes(x=as.numeric(rsa), y=rmsf, color=mutant)) + geom_point() + geom_smooth(method='lm', se=TRUE, level=0.9, color="black") + facet_wrap(~ c2 + mutant) + theme_classic()
p1 <- p + geom_text(x = 25, y = 300, label = "TEST", parse = TRUE)
show(p1)
