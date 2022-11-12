@REM Nginx ingress controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml

@REM NAA APP
kubectl apply -f namespace-app.yaml
kubectl apply -f auth-secret.yaml
kubectl apply -f main-secret.yaml
kubectl apply -f auth.yaml
kubectl apply -f main.yaml
kubectl apply -f ingress.yaml
kubectl get all -n=naa-app