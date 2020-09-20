docker-compose build \
--build-arg PASSWORD=$GIT_PASSWORD \
--build-arg ROUTE53_URL=$ROUTE53_URL \
--build-arg ROUTE53_PASSWORD=$ROUTE53_PASSWORD \
--build-arg ACCESS_KEY=$ACCESS_KEY \
--build-arg SECRET_KEY=$SECRET_KEY \
--build-arg BUCKETS_NAME=$BUCKETS_NAME

docker-compose up -d
