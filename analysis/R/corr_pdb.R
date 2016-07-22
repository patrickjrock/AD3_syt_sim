require(bio3d)
require(parallel)
args = commandArgs(trailingOnly=TRUE)

print("loading files")
dcd <- read.dcd(args[1])
pdb <- read.pdb(args[2])

print("fitting xyz")
ca.inds <- atom.select(pdb, elety="CA")
xyz <- fit.xyz(fixed=pdb$xyz, mobile=dcd,
               fixed.inds=ca.inds$xyz,
               mobile.inds=ca.inds$xyz, ncore=16)


cij<-dccm(xyz[,ca.inds$xyz], ncore=16)
out<-paste("/home/prock/Desktop/AD3_syt_sim/analysis/R/jpgs/", basename(args[2]), ".jpg", sep="")

#write.table(cij, file='cij.data', row.names=FALSE, col.names=FALSE)

#jpeg(out)
#plot(cij)
#dev.off()

view.dccm(cij, pdb)
