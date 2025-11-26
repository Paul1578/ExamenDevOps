build: 
	docker build -t ghcr.io/paul1578/arce:1.0.5 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml paul

rm: 
	docker stack rm paul