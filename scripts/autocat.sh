cd /home/prock/Desktop/AD3_syt_sim/data/dcds/cal
for f in *.dcd
do 
  base=${f%.dcd}  
  echo $base
  catdcd -o "cat/$f" ${base}* restart/${base}*
done
