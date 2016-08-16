cd /home/prock/Desktop/AD3_syt_sim/data/dcds/$1
for f in *_1.dcd
do 
  base=${f%_1.dcd}  
  echo $base
  catdcd -stride 5 -o "cat/$f" ${base}* 
done
