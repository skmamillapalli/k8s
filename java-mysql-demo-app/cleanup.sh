#!/bin/bash -xe
cd k8s_src

kubectl delete pod db-pod
kubectl delete svc mysql
kubectl delete rc java-mysql-vaullt-demo-rc
kubectl delete svc java-mysql-vaullt-demo-svc

kubectl get pods

kubectl get svc