# HTTP Proxy Functionality

This application includes functionality to access an external site (https://checkip.amazonaws.com/) through an HTTP proxy and display the results.

## Accessing the Proxy Endpoint

To use this functionality, navigate to the `/proxy` endpoint in your browser:

```
http://localhost:8000/proxy
```

or when deployed:

```
https://your-app-runner-url.awsapprunner.com/proxy
```

## Configuring the Proxy

The proxy settings are configured using standard environment variables:

- `HTTP_PROXY` or `http_proxy`: Proxy server for HTTP requests
- `HTTPS_PROXY` or `https_proxy`: Proxy server for HTTPS requests
- `NO_PROXY` or `no_proxy`: Comma-separated list of hosts that should bypass the proxy

### Example Environment Variable Settings

```bash
# For Linux/macOS
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1

# For Windows Command Prompt
set HTTP_PROXY=http://proxy.example.com:8080
set HTTPS_PROXY=http://proxy.example.com:8080
set NO_PROXY=localhost,127.0.0.1

# For Windows PowerShell
$env:HTTP_PROXY = "http://proxy.example.com:8080"
$env:HTTPS_PROXY = "http://proxy.example.com:8080"
$env:NO_PROXY = "localhost,127.0.0.1"
```

## Running with Docker

If you're using Docker, you can pass the environment variables when running the container:

```bash
docker run -p 8000:8000 \
  -e HTTP_PROXY=http://proxy.example.com:8080 \
  -e HTTPS_PROXY=http://proxy.example.com:8080 \
  -e NO_PROXY=localhost,127.0.0.1 \
  your-image-name
```

## AWS App Runner Configuration

When deploying to AWS App Runner, you can set these environment variables in the App Runner console or in your apprunner.yaml file:

```yaml
env:
  - name: HTTP_PROXY
    value: http://proxy.example.com:8080
  - name: HTTPS_PROXY
    value: http://proxy.example.com:8080
  - name: NO_PROXY
    value: localhost,127.0.0.1
```

## Response Format

The response will show:

1. Your IP address as seen by checkip.amazonaws.com
2. The proxy configuration that was used
3. The status of the request

If there's an error, the response will include error details to help with troubleshooting.