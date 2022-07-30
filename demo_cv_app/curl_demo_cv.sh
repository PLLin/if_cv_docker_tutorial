command="curl -X POST 'http://127.0.0.1:8000/get_shape' -H 'Content-Type: application/json' --data-raw '{\"image\": \"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\"}'"
echo $command
eval $command