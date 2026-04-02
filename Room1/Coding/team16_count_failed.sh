if [ $# -ne 1 ]; then 
	echo "Usage: $0< log_file_path>"
	exit 1
fi
LOG_FILE="$1"

if [ ! -f  "$LOG_FILE" ]; then
	echo "Error: File does not exist"
	exit 1
fi
COUNT=$(grep -i -o "failed" "$LOG_FILE"| wc -l)
echo "Number of failed entries:  $COUNT"
