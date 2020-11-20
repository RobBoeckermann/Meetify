# Meetify - Milestones

### Stack Setup -- 10/04/2020  
Create the basic environment for the code to live in. This includes:  
* Setting up MySQL database server  
* Setting up Python server that interacts with Spotify  
* Setting up Django server  
* Setting up React frontend  

### Song Intersection -- 10/04/2020  
This is a feature that takes the Liked Songs from two Spotify users and produces a list of songs that they have in common. This list will be then compiled into a playlist for the two users to share.  

### Setup Server -- 10/09/2020  
Upload the necessary files to the server and set up DNS configuration.  

### Design Database -- 10/23/2020  
Lay out the schema for the database tables.  

### Save Intersection as Playlist -- 10/23/2020  
Using the Spotify API, take the list of songs from the song intersection and turn it into a playlist that both users can access.  

### Authentication and Login -- 10/28/2020  
Authenticating Spotify users using the OAuth system. This feature includes:  
* Saving authorization token so a user does not have to authenticate every time they access the app  
* Adding a proper redirect URL to avoid the copy/paste of the URL  

### Implement Database Design -- 10/30/2020  
Use MySQL to implement design. Add dummy data to test design.  

### Search for Other Users -- 11/12/2020  
Add search functionality to find other users. Need to discuss what all should be included in search results.  

### User Location -- 11/13/2020  
Fetch user location. This will be used in the user matching algorithm to match users that are closer together.  

### Matching Users -- 11/20/2020  
This feature matches users based on Spotify listening history. It will also match users based on location.  

### Messaging Service -- 12/18/2020  
Users can communicate with each other via messaging service in-app after matching. Need to determine if this service is going to be done using a third-party service or if we will be creating it ourselves.  

### Final Product -- 02/28/2021  
Full Meetify application is deployed.  


