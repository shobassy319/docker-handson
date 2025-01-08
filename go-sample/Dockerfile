FROM golang:1.23

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o /simple-http

EXPOSE 8080

ENTRYPOINT ["/simple-http"]
