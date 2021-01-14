<h2>Java Demo app for secret management with hashicorp vault</h2>

<h3>Steps to run</h3>

1) Run ./install.sh to setup pods/rcs/svc.
2) Configure authorization for pods to vault looking at instructions. https://learn.hashicorp.com/tutorials/vault/kubernetes-sidecar.
3) Test the app, which is basically a set/get service.
4) Run cleanup.sh to remove pods and service.

* To add an entry to database via Java App,  
  ```curl {NODEIP:NODEPORT}/secrets-demo/add-user -d name=First -d email=someemail@email.com```.  
Entry Saved!

* To retrieve all users in database.  
  ```curl {NODEIP:NODEPORT}/secrets-demo/get-all-users```.  
[{"id":1,"name":"First","email":"someemail@email.com"}]
