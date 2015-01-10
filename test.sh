for i in $(seq 1 30)
do
   curl http://<HOSTNAME>/bottle && echo && echo
   sleep 2
done
