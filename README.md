
# Create Service Images

To create docker images of the services that print their own name



## Run 

Clone the project

```bash
  git clone https://Abbashozefa/create-service
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