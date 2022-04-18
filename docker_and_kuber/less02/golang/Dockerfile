FROM golang:latest

RUN mkdir /app

WORKDIR /app

COPY go.mod ./

COPY go.sum ./

RUN go mod download

COPY *.go ./

RUN go build -o /golang_app

EXPOSE 8080

ENTRYPOINT [ "/golang_app" ]
