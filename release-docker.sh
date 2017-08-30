set -ex

# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=vivaconagua
# image name
IMAGE=sluice


# bump version
docker run --rm -v "$PWD":/app vivaconagua/sluice patch
version=`cat VERSION`
echo "version: $version"

# run build
./build-docker.sh

docker tag $USERNAME/$IMAGE:latest $USERNAME/$IMAGE:$version
# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$version
