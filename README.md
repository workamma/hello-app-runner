# Hello App Runner

![](/static/banner_sample.png)

This is a example web service for [AWS App Runner](https://aws.amazon.com/apprunner/).
You can use this repo to automatically build and deploy or use pre-built images at [ECR Public](https://gallery.ecr.aws/aws-containers/hello-app-runner).

You can read about AWS App Runner in the [launch blog](https://aws.amazon.com/blogs/containers/introducing-aws-app-runner/)

## Deploy to App Runner

If you want to deploy this container make sure you have the latest release of the [`awscli`](https://github.com/aws/aws-cli) and run

```bash
SERVICE_NAME=hello-app-runner

cat > hello-app-runner.json <<EOF
{
    "ImageRepository": {
        "ImageIdentifier": "public.ecr.aws/aws-containers/hello-app-runner:latest",
        "ImageConfiguration": {
            "Port": "8000"
        },
        "ImageRepositoryType": "ECR_PUBLIC"
    },
    "AutoDeploymentsEnabled": false
}
EOF

aws apprunner create-service --service-name ${SERVICE_NAME} \
    --source-configuration file://hello-app-runner.json
```

If you want to deploy and manage this container using AWS CloudFormation just run

```bash
SERVICE_NAME=hello-app-runner

aws cloudformation create-stack --template-body file://cf.yaml --stack-name ${SERVICE_NAME} --parameters "ParameterKey=ServiceName,ParameterValue=${SERVICE_NAME}"
```

## Features

The service exposes a basic splash page with links to relevant App Runner content.
It has several unique features which benefit from running it in App Runner.

Upon first request it generates a unique avatar for each service which is saved in `./static/social.png`.
This image is used for social preview images when shared online and will be the same across different all of your container instances.
It is an example of using a local disk for small assets in an application.

The service also provides a `/metrics` endpoint so you can see some of the long running metrics of requests coming into the service.
This is an example of global state stored on a per container basis.
It can be used for state management, in memory cache, or other application needs.

### HTTP Proxy Functionality

The service includes a `/proxy` endpoint that demonstrates accessing an external site (https://checkip.amazonaws.com/) through an HTTP proxy. The proxy settings are configured using environment variables:

- `HTTP_PROXY` or `http_proxy`: Proxy server for HTTP requests
- `HTTPS_PROXY` or `https_proxy`: Proxy server for HTTPS requests
- `NO_PROXY` or `no_proxy`: Comma-separated list of hosts that should bypass the proxy

For detailed instructions on using this feature, see [PROXY_USAGE.md](PROXY_USAGE.md).

There also might be an easter egg or two if you read the code. ;)

## Development

To run this application locally you can use `pipenv`

```
pipenv install
pipenv run python app.py
```

To run the application locally in a container you can use `docker`

```
docker build -t hello-app-runner .
docker run -it -p 8000:8000 hello-app-runner
```

To run with HTTP proxy settings:

```
docker build -t hello-app-runner .
docker run -it -p 8000:8000 \
  -e HTTP_PROXY=http://proxy.example.com:8080 \
  -e HTTPS_PROXY=http://proxy.example.com:8080 \
  -e NO_PROXY=localhost,127.0.0.1 \
  hello-app-runner
```
