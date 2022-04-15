# Python simple HTTP server 

Please inspect `Dockerfile` and apply best practices.   
If you are new with _Docker_ and _Python_, see and go through [this page](https://docs.docker.com/language/python/build-images/) by docker official. 

Read this page in other language: [_English_](https://github.com/AvintonCode/docker-handson/blob/main/python-sample/README.md), [_日本語_](https://github.com/AvintonCode/docker-handson/blob/main/python-sample/README-ja.md)

## How to build and run the application 
1. Build container image 
```
docker build -t python-simple:v01 . 
```

2. Run container image
```
docker run --rm --name python-simple-app -p 8000:8000 -d python-simple:v01
```

3. The application has two endpoints `/` and `/ping`
```
curl -X GET http://localhost:8000/
curl -X GET http://localhost:8000/ping
```

4. Stop container
```
docker stop python-simple-app
```

## Tasks 

### 1. Minimize docker image size 
Docker image size is over 900 MB.  

### 2. Use non-root user for container process 
Container process is using a root user. 

### 3. Fix vulnerabilities 
Container image has some vulnerabilities.
Resolve all of the vulnerabilities. 
> Note: you can ignore some vulnerabilities for which the fix is not yet available. 

### 4. Improve build time 
`Dockerfile` or `README.md` are also copied to the container image. Fix this problem so that they will not be included in the image.  

When you edit the `app.py` file, the docker build will run `pip3 install` again.  
`pip3 install` should be triggered only when `requirements.txt` has been updated.  
Fix Dockerfile to improve the build speed.  