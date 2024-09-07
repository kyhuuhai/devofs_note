## Login ECR
  `aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 456869240414.dkr.ecr.ap-southeast-1.amazonaws.com`

## Build image
  `docker build -t ecs-user .`

## After the build completes, tag your image so you can push the image to this repository:
  `docker tag ecs-user:latest 456869240414.dkr.ecr.ap-southeast-1.amazonaws.com/ecs-user:latest`

## Run the following command to push this image to your newly created AWS repository:
  `docker push 456869240414.dkr.ecr.ap-southeast-1.amazonaws.com/ecs-user:latest`
