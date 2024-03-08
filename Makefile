printf = @printf "%-20s%s\n"
help:
	@echo "Commands available:"
	$(printf) "initialization" "Initializes the project directories and copies the file in the Hadoop file system"
	$(printf) "" "Usage: make initialization path=<path>"

initialization:
	sh ./shell_scripts/initialization.sh $(path)