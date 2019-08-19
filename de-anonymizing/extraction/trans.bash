sourcea activate python2
cd Desktop/Replication/de-anonymizing/extraction/
python main.py
java -cp /Users/weiguo/Desktop/weka-3-8-3/weka.jar weka.core.converters.CSVLoader /Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0818_forweka.csv > /Users/weiguo/Desktop/Replication/de-anonymizing/data/data_weka.arff
java -cp /Users/weiguo/Desktop/weka-3-8-3/weka.jar weka.filters.supervised.attribute.AttributeSelection -E "weka.attributeSelection.InfoGainAttributeEval" -S "weka.attributeSelection.Ranker -T 0 -N -1" -i /Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0818_forweka.csv -o /Users/weiguo/Desktop/Replication/de-anonymizing//data/data1.arff
java -cp /Users/weiguo/Desktop/weka-3-8-3/weka.jar weka.core.converters.CSVSaver -i /Users/weiguo/Desktop/Replication/de-anonymizing/data/data.arff -o /Users/weiguo/Desktop/Replication/de-anonymizing/data/data.csv
python classifier1.py


java -cp /Users/weiguo/Desktop/weka-3-8-3/weka.jar weka.core.converters.CSVSaver -i /Users/weiguo/Desktop/Replication/de-anonymizing/data/data0819_50.arff -o /Users/weiguo/Desktop/Replication/de-anonymizing/data/data0819_50.csv
