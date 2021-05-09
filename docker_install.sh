sudo apt-get update
sudo apt install docker.io
sudo docker --version
sudo systemctl status docker
sudo docker run hello-world
sudo docker images
sudo docker run docker/whalesay cowsay moby dick
sudo docker run -d -p 8080:5000 jcdemo/flaskapp
