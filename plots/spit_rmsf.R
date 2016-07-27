library("ggplot2", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.2")

rmsf <- read.table("./data/split_rmsf.data", head=T)

# c2a
sub1 <- filter(rmsf, mutant == 'wt' & c2 == 'c2a')
sub1 <- filter(rmsf, mutant == 'Y180N' & c2 == 'c2a')

# loop 3
for(i in 1:3){for(j in 1:3){loop3_c2a_unbound <- c(loop3_c2a_unbound,sub1[sub1$run == i & sub2$resid %in% 231:237,]$rmsf_unbound)}}
for(i in 1:3){for(j in 1:3){loop3_c2a_bound <- c(loop3_c2_bound,sub1[sub1$run == i & sub2$resid %in% 231:237,]$rmsf_bound)}}

# loop1
for(i in 1:3){for(j in 1:3){loop1_c2a_unbound <- c(loop1_c2a_unbound,sub1[sub1$run == i & sub2$resid %in% 170:176,]$rmsf_unbound)}}
for(i in 1:3){for(j in 1:3){loop1_c2a_bound <- c(loop1_c2a_bound,sub1[sub1$run == i & sub2$resid %in% 170:176,]$rmsf_bound)}}

# c2b
sub1 <- filter(rmsf, mutant == 'wt' & c2 == 'c2b')
sub1 <- filter(rmsf, mutant == 'Y311N' & c2 == 'c2b')

# loop3
for(i in 1:3){for(j in 1:3){loop3_c2b_unbound <- c(loop3_c2b_unbound,sub1[sub1$run == i & sub2$resid %in% 300:307,]$rmsf_unbound)}}
for(i in 1:3){for(j in 1:3){loop3_c2b_bound <- c(loop3_c2b_bound,sub1[sub1$run == i & sub2$resid %in% 300:307,]$rmsf_bound)}}

# loop1
for(i in 1:3){for(j in 1:3){loop1_c2b_unbound <- c(loop1_c2b_unbound,sub1[sub1$run == i & sub2$resid %in% 364:371,]$rmsf_unbound)}}
for(i in 1:3){for(j in 1:3){loop1_c2b_bound <- c(loop1_c2b_bound,sub1[sub1$run == i & sub2$resid %in% 364:371,]$rmsf_bound)}}

qplot()
