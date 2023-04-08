# Nightlight Web App

Bachelors of Technology Major project. In this project we have implemented a CNN based on the paper Learning to see in the dark.
The CNN uses a U-Net architecture and takes as input dark images and brightens them up so all the details are visible

Steps to run

1. Clone this repo 
2. Install Anaconda and Install additional dependencies by running 
>conda install tensorflow

>python -m pip install django pillow rawpy imagio exifread
3. Download model files from below link and place them in transform/model/ folder
4. Download static assets and place them in static/assets/ folder
5. Setup database using 
>python manage.py migrate
6. Run app using
>python manage.py runserver 
7. Goto 127.0.0.1:8000 in browser

Based on paper Learning to See in the Dark - https://arxiv.org/abs/1805.01934
