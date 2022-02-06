# nginx-docker-loadbalancer

##### Load balancer is a service/technique that work with multiple application instances for optimizing resource utilization, maximizing throughput, reducing latency, and ensuring fault-tolerance.
##### nginx is a very popular and efficient HTTP load balancer for distributing traffic to several application servers to improve performance, scalability and reliability.

### What we want to achive?
We will run 3 python application container in three different port (5001, 50002, and 5003). We will also run a nginx container in port 8000 that will take care of the load balancing among 3 application containers.

##### nginx loadbalancer configuration file (nginx.conf):
```
upstream loadbalancer {
server 172.17.0.1:5001;
server 172.17.0.1:5002;
server 172.17.0.1:5003;
}
server {
location / {
proxy_pass http://loadbalancer;
}}
```

![nginx-lb-in-docker](https://user-images.githubusercontent.com/73134659/152667851-4992c524-7dfc-4fd0-bd35-ee537b9c438e.JPG)

### Wayout 
##### Clone the repo where you will find app and nginx folder with required configuration and Dokcrefile. Stay in the base and run ``` docker-compose up ``` command
![image](https://user-images.githubusercontent.com/73134659/152667943-14d1da89-2bfc-48c1-91d9-af8c358d463a.png)

### Final Output:
Put Host IP and 8080 port in the brower and hit enter. Our request will be redirected to the applications via nginx loadbalancer and we will see different response with every page refresh.

![nginx-lb-output](https://user-images.githubusercontent.com/73134659/152669022-e8864b8d-7c49-48a4-9f89-bd3d470fcf28.JPG)



