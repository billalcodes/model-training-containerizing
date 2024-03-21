build:
    docker build -t movie-revenue-predictor .

run:
    docker run -p 5000:5000 movie-revenue-predictor

stop:
    docker stop $(docker ps -aq --filter ancestor=movie-revenue-predictor)

clean:
    docker system prune -a
