# Borinne

## What's going on here?

Borinne is a project that aims to prevent Bob (my chunky cat) to eat the food of Corinne(my other cat) as it is one of the issues we have when we are not home and can't be checking hi is not stealig her sister's food.

## Creating a server with Flask

I've created a rudimentary server that receives the image type file and sends it to my google drive with date and hour, so for now it's a good way to keep track of the cats, however I've created my first image recognizer with tensorflow and I'll be deploying it in the next few days on this server

The model will tell if it's Bob, Corinne or "nothing" in front of the camera and then decide if the image should or should not be send to the google drive.

## Must dos

The camera is an ESP32 cam module that when detecting any movement will make the http request to the Flask server with the capture of the image. I HAVE TO FINISH THIS, will probably be on another repo...

Also it would be cool to create certain type of mechanism to prevent Bob eating Corinne's food, could be some sound or a barrier of some sort...
