#!/bin/bash -xe
cd k8s_src

# setup nodes and services for k8s
kubectl create -f db-pod.yaml
kubectl create -f db-svc.yaml
kubectl create -f java-app-rc.yaml
kubectl create -f java-app-svc.yml
