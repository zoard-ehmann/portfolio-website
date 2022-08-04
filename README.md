# Portfolio Website

## Assignment
A website to show off your skills and the things you've built.

## Summary
I decided to use Python and Flask on the backend and mainly Bootstrap on the frontend. As I had a website already built with WordPress custom theme (CSS and JavaScript), I thought I will try to replicate it but with Flask and Bootstrap instead.  
This project set some challenges to me as I wanted to build a fully functional CMS to easily add, edit and remove projects in the portfolio section. To handle this, I had to implement a simple login system as well to ensure only the authenticated and authorized members can manage the portfolio section. This approach required a database in the backend, so I chose SQLite to handle the user and content management. The website contains a contact form as well to ensure that visitors can reach out to me. For this, I implemented an SMTP mailer system in the backend and used Flask Forms on the frontend. Some form elements had to be re-designed to match with the Bootstrap style.  
I tried to build this project with modularity in mind so I used classes wherever I could. I also added docstring to most of the functions and classes where it made sense.