# Go simple HTTP server 

Please inspect `Dockerfile` and apply best practices.   
If you are new with _Docker_ and _Go_, see and go through [this page](https://docs.docker.com/language/golang/build-images/) by docker official.

Read this page in other language: [_English_](https://github.com/AvintonCode/docker-handson/blob/main/go-sample/README.md), [_日本語_](https://github.com/AvintonCode/docker-handson/blob/main/go-sample/README-ja.md)

## How to build and run the application 
1. Build container image 
```
docker build -t go-simple:v01 . 
```

2. Run container image
```
docker run --rm --name go-simple-app -p 8080:8080 -d go-simple:v01
```

3. The application has two endpoints `/` and `/ping`
```
curl -X GET http://localhost:8080/
curl -X GET http://localhost:8080/ping
```

4. Stop container
```
docker stop go-simple-app
```

## Tasks 

### 1. Minimize docker image size 
Docker image size is over 1 GB.  

### 2. Use non-root user for container process 
Container process is using a root user. 

### 3. Fix vulnerabilities 
Container image has some vulnerabilities
Resolve all of the vulnerabilities. 
> Note: you can ignore some vulnerabilities for which the fix is not yet available. 

### 4. Improve build time 
When you edit the `server.go` file, the docker build will run `go mod download` again.  
`go mod download` should be triggered only when `go.mod` has been updated.  
Fix Dockerfile to improve the build speed.  