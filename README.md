## Inspiration

Is your camera roll filled with tens of screenshots of your friends’ schedules? Do you have to constantly scroll through the chat with your friend to find their schedule, just to realize that they are in class? Thanks to Friendule, you will always be able to know which of your friends are available to hang out with you in between your classes.

## What it does

Friendule is a website where McGill students can create an account and upload a screenshot of their friends' schedules in order to see at the current time if their friends would be able to hang out with them. 

## How we built it

We used the textract OCR API to convert the screenshot of the schedule to a .csv file. We then manipulated the data in the file to extract the friend's name, the course names, the day each class is, and the start and end times of the classes, which is done using a python script. The information is then stored in an SQLite3 database to save each user's friend list and the schedule information attached to them. 
## Challenges we ran into
 We were going to use the open-source OCR tesseract, which had serious accuracy issues until we discovered Textract, Amazon's machine learning service. Also, working with Django was challenging, as none of us had worked with it before McHacks. We had to learn this completely new framework, read documentation, and fix bugs. Most importantly, after having made all the individual components of the website, such as the user interface, scripts, and database, connecting every piece together was proven to be very difficult. 

## Accomplishments that we're proud of

Getting the OCR to work perfectly was a fulfilling accomplishment, as our multiple attempts with alternative OCRs to textract were inaccurate and yielded inconsistent results. We were also very unsure about whether the data extraction would work at all, which our whole project was based on, but thankfully it did work. 

## What we learned

This hackathon was a complete learning experience as we learned how to make a website from scratch, which none of us had done before.  We had to learn how to use Django, SQLite3, and Amazon's textract, among other packages/tools.


## What's next for Friendule

Friendule only works with screenshots of Mcgill schedules from Minerva, McGill's central information system. A user from another university can, therefore, not use Friendule unless their university's schedule is formatted precisely like McGill's. A drop-down menu that includes choices of different university schedule formats could be added to offer more compatibility. Also, although the website could be opened on a mobile phone, making a dedicated app would be more convenient for the user. 
