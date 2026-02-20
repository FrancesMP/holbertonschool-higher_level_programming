# RESTful API

## HTTP vs HTTPS

- **HTTP** (Hypertext Transfer Protocol) is the base protocol to send data over the web. It is non-secure, which means that the data is sent in plain text.
- **HTTPS** (HTTP Secure) is a secure version of HTTP that uses TLS/SSL to encrypt the data transferred.
- The main difference between HTTP and HTTPS is that HTTPS is secure and HTTP is not. HTTPS results in slightly slower transfer speeds due to encryption.

## HTTP Request Structure

An HTTP request is made of several parts:

1. **Request Line**
   - Includes the method (GET, POST, etc.), the URL, and the protocol version

2. **Headers**
   - Contains metadata like content type, content length, cookies, etc.

3. **Body** (optional)
   - Contains the data sent with the request
   - Example: For a POST request, it contains the data to create a new resource

## HTTP Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| GET    | Retrieves data | Fetching a web page or data from an API |
| POST   | Creates a new resource | Submitting a form or creating a new resource |
| PUT    | Updates an existing resource | Updating a user profile or a product |
| DELETE | Deletes a resource | Deleting a user profile or a product |

## Common HTTP Status Codes

| Status Code | Description | Scenario |
|-------------|-------------|-----------|
| 200 | OK | When a request is successful |
| 201 | Created | When a new resource is created |
| 301 | Moved Permanently | When a resource has been moved to a new URL |
| 404 | Not Found | When a requested page or resource isn't available on the server |
| 500 | Internal Server Error | When a server error occurs |


  


