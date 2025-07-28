FROM golang:1.22

WORKDIR /app

# Only copy go.mod since go.sum doesn't exist
COPY go.mod ./

# No need to run go mod download if no external modules
COPY . .

RUN go build -o app

EXPOSE 8080

CMD ["./app"]
