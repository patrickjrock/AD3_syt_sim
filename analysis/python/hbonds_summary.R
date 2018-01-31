require(ggplot2)

summarize_by <- function(m){
  s <- subset(hbonds, mutant==m)
  c2a <- subset(s, c2=="c2a")$hbonds
  c2b <- subset(s, c2=="c2b")$hbonds
  cat(sprintf("Means of %s: C2A: %f    C2B: %f\n", m, mean(c2a), mean(c2b)))
  cat(sprintf("Difference of means: %f\n", mean(c2b)-mean(c2a)))
}

summarize_hbonds <- function(f){
  hbonds <- read.table(f, head=T)
  summarize_by("wtcalunbound")
  summarize_by("wtcalbound")
  summarize_by("mutantcalunbound")
  summarize_by("mutantcalbound")
}
