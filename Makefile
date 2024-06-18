printf = @printf "%-30s%s\n"
help:
	@echo "Commands available:"
	$(printf) "initialization" "Initializes the project directories and copies the file in the Hadoop file system"
	$(printf) "" "Usage: make initialization path=<path>"
	$(printf) "test-mapper" "Tests the mapper and reducer scripts with a sample input string that contains two"
	$(printf) "" "records where as each record contains a label and a text separated by a tab"
	$(printf) "hadoop-mapper" "Runs the mapper and reducer scripts in the Hadoop file system"
	$(printf) "top-10-words" "Runs the MongoDB query to get the top 10 words"
	$(printf) "top-10-luw-gt-4-lte-7" "Runs the MongoDB query to get the top 10 words with length > 4 and <= 7"
	$(printf) "dump-tweets" "Dumps the tweets and dictionary collection in the MongoDB"
	$(printf) "restore-tweets" "Restores the tweets and dictionary collection in the MongoDB"
	$(printf) "count-class" "Runs the MongoDB query to get the count of each class"

initialization:
	sh ./shell_scripts/initialization.sh $(path)

test-mapper:
	echo -e "1\tfoo foo labs a is are foo bar\n0\tfoo bar labs" | ./scripts/mapper.py | sort | ./scripts/reducer.py

hadoop-mapper:
	sh ./shell_scripts/hadoop_mapper.sh

top-10-words:
	mongo ./mongodb_queries/top_10_words.js --quiet

top-10-luw-gt-4-lte-7:
	mongo ./mongodb_queries/top_10_luw.js --quiet

dump-database:
	mongodump --db ds_project --out ./data/ds_project

restore-database:
	mongorestore --drop --nsInclude "ds_project.*" ./data/ds_project
	
count-class:
	mongo ./mongodb_queries/count_class.js --quiet	
