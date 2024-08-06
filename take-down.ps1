# Define your stack name and Docker Compose file
$STACK_NAME = "nexfitra_swarm"
$VOLUME_NAME = "nexfitra_swarm_postgres_data"

# Remove the stack
Write-Output "Removing stack..."
docker stack rm $STACK_NAME

# Wait for the stack to be removed
Write-Output "Waiting for the stack to be removed..."
Start-Sleep -Seconds 10

# Remove the volumes
Write-Output "Removing volumes..."
docker volume rm $VOLUME_NAME