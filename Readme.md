# Uncommon Hacks 2019 Submission

![Logo](./Images/LOGO.png)


## Inspiration
The first round of interview is mostly coding where we are provided problems on HackerRank or some other platform. Now the trick that many people use it, they ask some of their friends to do it on their behalf and move easily to the next round.
The whole process of hiring is very tiring and involves many useful resources and money. So if cheat can be detected at an early stage, it will have multiple benefits. Major of these are:
1. Cutting down possiblities of Cheating
2. Only good candidates are passed through
3. Saves time and resources of interviewers

## What it does

We are using several events to check if the candidate is doing cheating such as:
  - Screensharing thorugh Chrome Desktop share, Teamviewer and Skype
  - If multiple people are present for the challenges
  - Using Print screen

## How we built it

We have noticed some trend over screensharing, such as when usng Google Chrome it shows text at the top such as 
"Your desktop is currently shared with jayrodge15@gmail.com. Stop Button(Button)".
![chrome](./Images/Google Remote\ Desktop\ -\ 1.png)
With Teamviewer, it shows:
![teamviewer](./Images/TeamViewer-1.png)


## Challenges we ran into
Using Google Cloud Vision API, at first we though it would be easy, but it turned out to be quite difficult because input type that it was expecting and input type of our screenshots was different that it was 


## Accomplishments that we're proud of

We are sucessfull in detecting whether the candidates is using screen share when coding challenge is active and whether there are more than one people.


## What we learned

Calling APIs isn't easy, figuring out whats APIs expect and using it for the application takes time.


## What's next for Online Coding Challenges Cheat Detection

Using Computer Vision and Deep Learning to detect various screen sharing tools such as Skype or any other third party applications.
