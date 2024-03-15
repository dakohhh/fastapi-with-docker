sudo docker build -t <project_name> . 

sudo docker run -d -p 8000:8000 <project_name>

sudo docker-compose up -d  <!-- Run container in detached mode -->

sudo docker-compose up --build  <!-- Run container in terminal/interactive mode -->

sudo docker-compose down  <!-- stop and remove all containers running -->

sudo docker exec -it <container_name> sh <!-- Starts an interactive shell to view containers files -->




sudo docker image ls   <!-- List all the images created on Docker -->


sudo docker stop container_id_or_name

