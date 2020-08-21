# Big-Data
Trabajo Final Big Data


Para correr el codigo, por favor acceder al servidor master-hadoop y correr el siguiente comando:


bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file /home/hadoop/mapper.py    -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py   -reducer /home/hadoop/reducer.py \
-input /user/ts/Z/* -output /user/ts/Z-output
