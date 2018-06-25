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
docker run -it test python solution.py --host <redis-host> --port <redis-port> --db <redis-db>
```
* Replace placeholders in the above command with appropriate values.
* For local testing where redis is running on a host machine, use `host.docker.internal` as host