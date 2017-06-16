# REU AMI 2017: ASL Project
# Week 1:
* ~~Get an x value for a specific body part~~
* ~~Get the average x value for a specific body part over a single xml file~~
* ~~Get the average x value for a specific body part over all xml files and store the output~~
* Sort the signs by their x value averages over that body part
* ~~Find the average time per sign spent~~

## Friday afternoon / Monday objectives:
##### Provide more information for prior work - Hypothesis: ASL = 2x time of spoken language, and 2x the information
* ~~range of motion for signs~~

#Week 2
##Monday - Wednesday
* ~~Create an animation for a given xml file's body part~~
* ~~Make that animation work for all body parts~~
* ~~Have a way to create a video out of that animation for computer vision purposes if needed~~
* Read over more papers in the subject
* Find out what work has been done in the field

##Thursday
* ~~create a regex to fix up the filenames~~
* ~~Start implementing NLTK~~
    * Decided to use TextBlob instead of NLTK
    * (for identifying which signs are nouns, adjectives, verbs, etc by looking at the filenames)
* ~~Create a database within python so that it can be manipulated (python script)~~
* ~~Create a data frame so that more features can be extracted~~
* ~~C# translate the XML data from CameraSpace to DepthSpace so the data can better represent the absolute x, y, and z values~~
* https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html is cool

##Friday
* ~~Make the data frame work properly~~
* ~~Split the data frame into multiple objects, figure out more things to add to the df~~
* ~~In C# have the "converted" XML data become skeletal animations (and be able to save said animations)~~

#Week 3:
##Monday
* ~~Split up the data frame into different objects and changed to useful stats~~
* ~~set up the printer~~
* Talk and find out what to do next

##Tuesday
* ~~find interesting details on the datasets that were split up~~
* Create a list of signs that are unique and can be used to train
    * signs should be distinguishable commands to Google assistant
* Finish up presentation for tomorrow
* ~~Some work on the ASR for deaf people using mturk~~

##Wednesday/Thursday
* ~~Use the average of x,y,z to find the min and max, and subtract those 2 for the range~~
* ~~Get a skeleton for the figure~~
* ~~Animate the skeleton~~
* ~~Get Rodeo to work~~

##Friday
* Actually read papers about ASL recognition and discuss what has been done
    * Perhaps write summary of papers for better organization and easier look-up
* Get voice samples for subjects for the deaf speech side project
* Discuss how we will record ourselves with the Kinect
    * (need XML and human video)
    * Finish up list of words to sign


##Monday
* Add features of each sign into the database
