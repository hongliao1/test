
#devices='adb devices |grep : |awk "{print $1}"'
#adb devices|grep 5|awk '{print $1}'

devices=`adb devices|grep 5|awk '{print $1}'`
for device in $devices;
do
  { nohup adb  -s $device shell monkey -p com.rantion.ns.pda -v -s 20 --pct-touch 30 --pct-trackball 20 --pct-nav 30 --pct-syskeys 20  --throttle 300 200 & }
done