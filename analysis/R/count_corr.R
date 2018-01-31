require(bio3d)
require(parallel)
require(ggplot2)

count_connections <- function(row) {
  vect <- row[abs(row) > 0.6]
  return(length(vect))
}

count_corr <- function(dcd, pdb, name){
  dcd <- read.dcd(dcd)
  pdb <- read.pdb(pdb)

  print("fitting xyz")
  ca.inds <- atom.select(pdb, elety=c("CA"))
  xyz <- fit.xyz(fixed=pdb$xyz, mobile=dcd,
		 fixed.inds=ca.inds$xyz,
		 mobile.inds=ca.inds$xyz, ncore=16, nseg.scale=8)

  print("xyz fit")

  cij<-dccm(xyz[,ca.inds$xyz], ncore=16)
  counts <- apply(cij, 2, count_connections)
  label <- rep(name, times=length(counts))  
  resid <- seq(from=272, to=418)

  # add distance column for sorting by 311 proximity
  ca.inds <- atom.select(pdb, elety="CA")
  d <- dm(pdb, ca.inds)
  dist <- c(na.omit(d[,40]), 0, na.omit(d[40,]))

  df <- data.frame(resid, counts, label, dist)
  sorted <- df[with(df, order(dist)), ]
  return(sorted)
}

wt <- count_corr("../../data/dcds/final/cat/c2b_wtcalunbound_1.dcd", "../../structures/pdb/c2b_wtcalunbound.pdb", "wt unbound")
y311n <- count_corr("../../data/dcds/final/cat/c2b_Y311Ncalunbound_1.dcd", "../../structures/pdb/c2b_Y311Ncalunbound.pdb", "Y311N unbound")

df <- rbind(wt, y311n)

#p <- ggplot(df, aes(x=resid, y=counts, color=label)) + geom_hist() 
