# Alive

Pings a list of IP's stored in the CSV file data.csv, the webpage refreshes every minute and re-pings the hosts.

## Docker Instructions
#### Install Docker
`apt-get install docker`

#### Download docker container
`docker pull knolls/alive`

#### Start docker container, open port 5000 in docker, run standalone
`docker run -d -p 5000:5000 knolls/alive`

#### Use docker ps to get the <container name>, be a string ex:c0cedd31a3
`docker ps`

#### Enter bash in the container to edit data.csv
`docker exec -it <container name> /bin/bash`

#### Edit data.csv
`vim data.csv`
