require(bio3d)
args = commandArgs(trailingOnly=TRUE)

print("loading files")
dcd <- read.dcd(args[1])
pdb <- read.pdb(args[2])
pn  <- as.numeric(args[3])

print("fitting xyz")
ca.inds <- atom.select(pdb, elety="CA")
xyz <- fit.xyz(fixed=pdb$xyz, mobile=dcd,
               fixed.inds=ca.inds$xyz,
               mobile.inds=ca.inds$xyz)

print("computing principle component")
pc <- pca.xyz(xyz[,ca.inds$xyz])
print("making trajectory")
p1 <- mktrj.pca(pc, pc=pn, b=pc$au[,1], file="pc.pdb")
