## k8s应用设定文件
- kubectl apply -f k8s/service.yaml

## 启动服务通道
- minikube service sum-service

## rollout部署配置
- kubectl rollout restart deployment sum-service

## 服务端口映射
- kubectl port-forward service/sum-service 8081:80

## 获取部署信息
- kubectl get deployment

## 获取服务信息
- kubectl get svc

## 获取POD信息
- kubectl get pods

## 创建命名空间
- kubectl create namespace argocd

## 获取命名空间
- kubectl get namespaces

## 获取日志文件
- kubectl logs sum-service-658b656d6c-zz9x2

## 添加argo至kubectl
- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## argo同步
- argocd app sync my-app

## argo生成app
- argocd app create my-app  --repo https://github.com/sonsai/src-app-learn-docker-k8s.git  --path k8s  --dest-server https://kubernetes.default.svc  --dest-namespace default

##
