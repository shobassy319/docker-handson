# docker-handson 
Sample Dockerfiles and quizzes for learning docker best practices. 

This repository provides some sample (compromised) dockerfile for a simple HTTP server application.  
You can learn some best practices by inspecting and fixing the `Dockerfile`. 

## Tasks 

You can choose your preferred programming language: Go or Python.  

The quizzes require a little language-specific knowledge or experience.  
But you only have to fix `Dockerfile`.  

## Pre-requisities 
- Docker 
- Any container scanning tool (e.g. [Trivy](https://github.com/aquasecurity/trivy) or [`docker scan`](https://docs.docker.com/engine/scan/) )

## Getting started 
1. Clone this repo 
```
git clone https://github.com/AvintonCode/docker-handson.git
```

2. Go to the `go-sample` or `python-sample` directory and find the compromised `Dockerfile`.  

## Hints 

### Read some articles about docker best practices 
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) by Docker
- [Image-building best practices](https://docs.docker.com/get-started/09_image_best/) by Docker
- [Docker development best practices](https://docs.docker.com/develop/dev-best-practices/) by Docker
- [Best practices for building containers](https://cloud.google.com/architecture/best-practices-for-building-containers) by Google
- [Best practices writing a Dockerfile](https://docs.bitnami.com/tutorials/best-practices-writing-a-dockerfile) by Bitnami

### Use trivy to scan vulnerabilities 
[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability scanner for container images, file systems, config files, etc. 

You can add `--ignore-unfixed` to hide unfixed vulnerabilities from the result.  
```
trivy image --ignore-unfixed go-simple:latest
```

