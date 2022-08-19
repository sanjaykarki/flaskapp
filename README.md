### Flask app to view the price of Bitcoin(BTC) in both EUR and CZK

#### Prerequisites
- Docker
- Minikube
- Kubectl

#### Building docker images directly inside minikube
`eval $(minikube docker-env)`

#### Start minikube
`minikube start`

#### build docker images
`docker compose build`

#### Apply deployment and create pods
`kubectl apply -f kubernates/deployment.yml`

#### Apply services
`kubectl apply -f kubernates/service.yml`

#### Get the IP address of Kubernetes service
`minikube service flaskapp-service`