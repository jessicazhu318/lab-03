# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jessica Zhu
- No second team member

## Lab Question Answers

### Introduction
 Answer to Question 1: 
   RESTful APIs are scalable since the REST architecture means that the APIs
   are stateless, so no client request information needs to be retained by
   the server, which reduces the load on the server and makes it possible for
   the server to simultaneously handle a big number of clients. Also, with
   the REST architecture, caching is supported, which reduces some of the
   interactions needed between the client and server as well as improves the
   response time of the server.
   
### Creating a Client/Server
 Answer to Question 2:
   The resources the mail server is providing to the client include email 
   contents composed of the recipient of the mail, the sender of the mail, 
   the subject of the mail, the body of the mail, as well as a generated
   unique id number for the mail.
 
 Answer to Question 3:
   A common REST method not used in this mail server is the PUT method. The 
   mail server could be extended to use this method if the ability to create
   a draft email was implemented. Thus, an email could be drafted and saved
   as a draft on the server, but with each change and new save, the PUT 
   method would be used to update the already existing draft email on the
   server. This way the same draft email is not created multiple times.
   
### Using a 'Real' API
 Answer to Question 4:
   API keys are used for many RESTful APIs because they allow a way for the 
   application making the call to the API to be identified. The purpose of 
   these keys is to make sure that the application making the call is
   authorized to do so. Thus, with API keys, you can control the number of
   calls being made to your API as well as see patterns of your API's usage
   in terms of traffic.
   
   Source for Q4:
   https://www.cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:
   text=API%20keys%20provide%20project%20authorization,-To%20decide%20which
   &text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20
   the%20API
   
   
 
