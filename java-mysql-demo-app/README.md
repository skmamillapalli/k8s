<h2>Java Demo app for secret management with hashicorp vault</h2>

<h3>Steps to run</h3>

1) Build the app locally or from CI with mvn. Run `./mvnw clean install` (For class not found errors, monitor JAVA_HOME and jdk version).  
2) Build docker image locally or from CI. Push the image to an image repository for consumption by k8s pods. ex;`docker build -t java-demo-app`.  
3) Run ./install.sh to setup pods/rcs/svc.
4) Configure authorization for pods to vault looking at instructions. https://learn.hashicorp.com/tutorials/vault/kubernetes-sidecar.
5) Test the app, which is basically a set/get service.
6) Run cleanup.sh to remove pods and service.

<h3>Tests</h3>

* To add an entry to database via Java App,  
  ```curl {NODEIP:NODEPORT}/secrets-demo/add-user -d name=First -d email=someemail@email.com```.  
Entry Saved!

* To retrieve all users in database.  
  ```curl {NODEIP:NODEPORT}/secrets-demo/get-all-users```.  
[{"id":1,"name":"First","email":"someemail@email.com"}]
