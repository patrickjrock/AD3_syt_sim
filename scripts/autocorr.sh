FILES=/home/prock/Desktop/AD3_syt_sim/structures/pdb/*
RDIR=/home/prock/Desktop/AD3_syt_sim/analysis/R/py/
for f in $FILES
do 
  cd /home/prock/Desktop/AD3_syt_sim/data/dcds/control/cat
  b=$(basename $f)
  base=${b%.pdb} 
  echo $base
  Rscript ~/Desktop/AD3_syt_sim/analysis/R/corr_pdb.R "${base}_1.dcd" $f
  mkdir "${RDIR}${base}"
  mv corr.py "${RDIR}${base}"
  mv corr.inpcrd.pdb "${RDIR}${base}"
done
