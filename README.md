# Portfolio Website

## Task
A website to show off your skills and the things you've built.  

## Assignment
Using what you have learnt about web development, build your own portfolio website.  

This can be designed any way you want. It's the place to show off your skills and the things you've built.  

Take inspiration from other developers but try not to copy their designs. Because this is about showing off what you can do!  

Use what you've learnt from Day 65 and plan out your website. Think about design, UI, UX, colour schemes, fonts. Don't build the website for other people, build it to make yourself proud.  

If you want, deploy and host the website to share with other students so we can admire your hard work!  

## Summary
I decided to use Python and Flask on the backend and mainly Bootstrap on the frontend. As I had a website already built with WordPress custom theme (CSS and JavaScript), I thought I will try to replicate it but with Flask and Bootstrap instead.  

This project set some challenges to me as I wanted to build a fully functional CMS to easily add, edit and remove projects in the portfolio section. To handle this, I had to implement a simple login system as well to ensure only the authenticated and authorized members can manage the portfolio section. This approach required a database in the backend, so I chose SQLite to handle the user and content management. The website contains a contact form as well to ensure that visitors can reach out to me. For this, I implemented an SMTP mailer system in the backend and used Flask Forms on the frontend. Some form elements had to be re-designed to match with the Bootstrap style.  

I tried to build this project with modularity in mind so I used classes wherever I could. I also added docstring to most of the functions and classes where it made sense.  