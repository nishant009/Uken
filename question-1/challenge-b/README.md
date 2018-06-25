# How to run the solution
* Navigate to the directory
```shell
cd question-1/challenge-b
```
* Build the docker container by running a command like:
```shell
docker build -t test .
```
* Run the container using the following command:
```shell
docker run -d -p 5000:5000 -e HOST=<redis-host> -e PORT=<redis-port> -e DB=<redis-db> test
```
* Replace placeholders in the above command with appropriate values.
* For local testing where redis is running on a host machine, use `host.docker.internal` as host