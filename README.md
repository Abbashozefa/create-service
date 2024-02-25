# Create Service Images

To create docker images of the services that print their own name



## Run 

Clone the project

```bash
  git clone https://github.com/Abbashozefa/create-service
```

Go to the project directory

```bash
  cd create-service
```

Go to app.py and change

```bash
  return jsonify({'name':'<servicename>'})
```
Login to dockerhub account

```bash
  docker login
```
Build image with service name

```bash
  docker build -t dsanokia/<servicenamewithoutunderscore>:latest .
```


push image dockerhub repo

```bash
  docker push dsanokia/<servicenamewithoutunderscore>
```

#Creating Helm Charts 

Start a local Kubernetes cluster
```bash
minikube start
```

Create a new Helm Chart
```bash
helm create <chart_name>
```

Change in created directory
```bash
Go to values.yaml and change the following:
1.image: repository : dsa/nokia
2.tag:"latest"
3.service: port:5000
```

Install new package
```bash
helm install <some_user_name> <chart_name>
```

Install Helm package
```bash
helm package <chart_name>
```

To see the status of the Kubernetes pods deployed 
```bash
kubectl get pods
```

Forward network traffic from a local port on your computer to a port on a Kubernetes Pod
```bash
kubectl port-forward <copied_NAME_from_previous_step> 8080:5000
```

Push the chart to Docker Hub
```bash
->helm push <name_of_tarball.tgz> oci://registry-1.docker.io/dsanokia
```


