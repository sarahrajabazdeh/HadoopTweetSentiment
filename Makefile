printf = @printf "%-20s%s\n"
help:
	@echo "Commands available:"
	$(printf) "initialization" "Initializes the project directories and copies the file in the Hadoop file system"
	$(printf) "" "Usage: make initialization path=<path>"
	$(printf) "test-mapper" "Tests the mapper and reducer scripts with a sample input"

initialization:
	sh ./shell_scripts/initialization.sh $(path)

test-mapper:
	echo -e "1\tfoo foo labs a is are foo bar\n0\tfoo bar labs" | ./scripts/mapper.py | sort | ./scripts/reducer.py

hadoop-mapper:
	sh ./shell_scripts/hadoop_mapper.sh