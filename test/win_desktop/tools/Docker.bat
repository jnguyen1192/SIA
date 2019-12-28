docker-machine start default
docker-machine env default
@FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i