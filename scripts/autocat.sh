cd /home/prock/Desktop/AD3_syt_sim/data/dcds/control
FILES=/home/prock/Desktop/AD3_syt_sim/structures/pdb/*
for f in $FILES
do 
  b=$(basename $f)
  base=${b%.pdb}  
  catdcd -stride 10 -o "cat/${base}_1.dcd" ${base}*
done
