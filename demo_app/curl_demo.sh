command="curl -X POST 'http://127.0.0.1:8000/multiply' -H 'Content-Type: application/json' --data-raw '{\"num1\":10,\"num2\":20}'"
echo $command
eval $command
