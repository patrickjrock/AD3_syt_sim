FILES=/media/prock/data/AD3_syt_sim/data/dcds/final/cat/*
RDIR=/media/prock/data/AD3_syt_sim/analysis/R/py/
for f in $FILES
do 
  cd /home/prock/Desktop/AD3_syt_sim/data/dcds/final/cat
  b=$(basename $f)
  base=${b%_1.dcd} 
  echo $base
  Rscript ~/Desktop/AD3_syt_sim/analysis/R/corr_pdb.R $f "/media/prock/data/AD3_syt_sim/structures/pdb/${base}.pdb"
  mkdir "${RDIR}${base}"
  mv corr.py "${RDIR}${base}"
  mv corr.inpcrd.pdb "${RDIR}${base}"
done
