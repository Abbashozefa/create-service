
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

```bash
->minikube start
```

->helm create <chart_name> 
Go to values.yaml and change the following:
1.image: repository : dsa/nokia
2.tag:"latest"
3.service: port:5000

->helm install <some_user_name> <chart_name>

->helm package <chart_name>

->kubectl get pods
Copy the NAME

->kubectl port-forward <copied_NAME_from_previous_step> 8080:5000

->helm push <name_of_tarball.tgz> oci://registry-1.docker.io/dsanokia


