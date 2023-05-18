docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -aq) # закоментить, если не нужно удаление всех образов

# выбрать образы которые нужно пересобрать 
#docker rmi postgres:15.2-alpine
#docker rmi dpage/pgadmin4:7.1
#docker rmi fastapi_simple_app_app:latest
#docker rmi nginx:alpine

echo "---------------------------------------------------------------------"
echo ""
docker ps -a

echo "---------------------------------------------------------------------"
echo ""
docker images

echo "---------------------------------------------------------------------"
echo ""
#docker-compose up
