# Big-Data
Big Data Research Paper

To follow the apprpiate procedures, please read Access-servers, then Access-MillionSongDataset, then Hadoop-Install.


To run our code, please download mapper.py and reducer.py and move them to /home/hadoop within hadoop-master. access the hadoop-master server an run the following script:


bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file /home/hadoop/mapper.py    -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py   -reducer /home/hadoop/reducer.py \
-input /user/ts/data -output /user/ts/data-output
