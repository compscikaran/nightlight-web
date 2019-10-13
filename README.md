# Nightlight Web App

Steps to run

1. Clone this repo 
2. Install Anaconda and Install additional dependencies by running 
>conda install tensorflow

>python -m pip install django pillow rawpy imagio exifread
3. Download model files from below link and place them in transform/model/ folder
>https://drive.google.com/file/d/1B017V0Ydpu9AEiCyCStyPcjgglS8OVTB/view?usp=sharing
4. Download static assets and place them in static/assets/ folder
5. Setup database using 
>python manage.py migrate
6. Run app using
>python manage.py runserver 
7. Goto 127.0.0.1:8000 in browser