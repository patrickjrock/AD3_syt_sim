#!bin/sh
#copy with name replace
#use to fetch dcds from lonestar

fname=$(basename "${1}" .dcd)

for i in `seq 1 10`; do 
  cpname="${fname}_${i}.dcd"
  if  [ -f "$2$cpname" ]; then 
    echo "$2$cpname exists"
    else 
    echo "copying"
    cp $1 $2$cpname
    break
  fi
done
