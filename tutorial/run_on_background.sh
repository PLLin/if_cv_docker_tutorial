command="docker run -d ubuntu:18.04 /bin/sh -c 'while true; do date; sleep 10; done;'"
echo $command
eval $command
