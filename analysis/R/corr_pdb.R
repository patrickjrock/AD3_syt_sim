require(bio3d)
require(parallel)

args = commandArgs(trailingOnly=TRUE)

print("loading files")
dcd <- read.dcd(args[1])
pdb <- read.pdb(args[2])

print("fitting xyz")
ca.inds <- atom.select(pdb, elety=c("CA"))
xyz <- fit.xyz(fixed=pdb$xyz, mobile=dcd,
               fixed.inds=ca.inds$xyz,
               mobile.inds=ca.inds$xyz, ncore=16)

print("xyz fit")

cij<-dccm(xyz[,ca.inds$xyz], ncore=16)

#out<-paste("/home/prock/Desktop/AD3_syt_sim/analysis/R/jpgs/", basename(args[2]), ".jpg", sep="")

#jpeg(out)
#plot(cij)
#dev.off()

view.dccm(cij, pdb)
