# Define your stack name and Docker Compose file
$STACK_NAME = "nexfitra_swarm"
$VOLUME_NAME = "nexfitra_swarm_postgres_data"
$IMAGE_NAME = "sdeery14/nexfitra_flask_app:latest"

# Remove the stack
Write-Output "Removing stack..."
docker stack rm $STACK_NAME

# Wait for the stack to be removed
Write-Output "Waiting for the stack to be removed..."
Start-Sleep -Seconds 10

# Remove the volumes
Write-Output "Removing volumes..."
docker volume rm $VOLUME_NAME

# Build the Docker image
Write-Output "Building Docker image..."
docker build -t $IMAGE_NAME ./app

# Push the Docker image (assuming you have a Docker registry configured)
Write-Output "Pushing Docker image..."
docker push $IMAGE_NAME

# Deploy the stack
Write-Output "Deploying stack..."
docker stack deploy -c docker-compose.yml $STACK_NAME

Write-Output "Deployment complete."
