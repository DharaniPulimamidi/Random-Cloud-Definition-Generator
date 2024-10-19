# Random Cloud Definition Generator

![EC2 Tag Notification (1)](https://github.com/user-attachments/assets/e5ded822-7a26-457f-bf6d-f1cbdcb8d6f4)

### Project Description:
Description: In this video, I’ll show you how to create a beautiful web application that fetches random cloud definitions using AWS API Gateway and DynamoDB. This project demonstrates how to leverage cloud technologies to serve dynamic content in a user-friendly way. You’ll learn how to:

* Set up an API with AWS API Gateway to retrieve cloud definitions from DynamoDB.
* Build a simple yet elegant front-end using HTML, CSS, and JavaScript.
* Enhance the user experience with smooth transitions and interactivity.
* Deploy the application and see it in action!

### Architecture Diagram: 
![Untitled (Youtube Banner)](https://github.com/user-attachments/assets/35ad8dfa-0097-4a01-ac21-ff78f65911a2)

### Steps Explained
* Client Interaction: The user opens the web application and clicks a button to get a random cloud definition.
* API Gateway: The browser sends an HTTP GET request to the API Gateway.
* Lambda Function: The API Gateway triggers a Lambda function to handle the request.
* DynamoDB Query: The Lambda function queries the DynamoDB table for a random cloud definition.
* Response: The Lambda function returns the definition to the API Gateway, which then sends it back to the client browser for display.

### Implementation:
* DynamoDB Table Name: ```CloudDefinitions```
* LambdaFunction Name: ```GetRandomQuote```
* API Gateway Name: ```QuoteGenerator```
* Resource Name: ```quote```

Whether you're a beginner or an experienced developer, this project will help you understand the basics of cloud computing and web development. Don't forget to like, share, and subscribe for more cloud-related tutorials!

Note: You can host the Frontend on S3 or EC2 Instance
