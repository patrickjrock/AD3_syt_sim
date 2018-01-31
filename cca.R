library(bio3d)
library(igraph)
library(parallel)

setwd("/media/prock/data/AD3_syt_sim")
dcd <- read.dcd("data/dcds/unbound/cat/c2a_Y180N_cat.dcd")
pdb <- read.pdb("structures/pdb/c2a_Y180Ncalunbound.pdb")


inds <- atom.select(pdb, elety = c("CA"))
trj <- fit.xyz(fixed = pdb$xyz, mobile = dcd,
               fixed.inds = inds$xyz, mobile.inds = inds$xyz)


important.inds <- atom.select(pdb, resno=c(300:315, 360:375), elety = c("CA"))

cij <- dccm(trj[,inds$xyz], ncore=16)
net <- cna(cij, cutoff.cij=0.35)
plot(net, pdb)

pymol.dccm(cij, pdb, launch = TRUE)

