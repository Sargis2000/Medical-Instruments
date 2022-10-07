### Step1:  
Install Git by running  on Debian-based distributions like Ubuntu
```bash
sudo apt install git
```
 or
 ```bash
sudo dnf install git
```
### Step2:
[Create githob account](https://www.github.com)
### Step3:
Add configs 
``` bash
git config --global user.name "YOUR NAME"
```
``` bash
git config --global user.email "YOUR EMAIL"
```
### Step4:
[Creat personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
### Step5:
Clone repositoy
``` bash
git clone https://github.com/sargis2000/Medical-Instruments.git
```
insted of password use your personal access token.
### Step6: 
Install python.\
Run the following commands as root or user with sudo access to update the packages list and install the prerequisites:
``` bash
sudo apt update
sudo apt install software-properties-common
```
Add the deadsnakes PPA to your system’s sources list:
``` bash
sudo add-apt-repository ppa:deadsnakes/ppa
```
When prompted press ```ENTER``` to continue:\
Once the repository is enabled, install Python 3.7 with:
``` bash
sudo apt install python3.7
```
Verify that the installation was successful by typing:
``` bash
python3 --version
```
### Step7:
Isntall pip
``` bash
sudo apt-get install python3-pip 
```

### Step8:
Install dependencies
``` bash
pip install -r requirements.txt
```

### Step9:
Apply migranions
``` bash
python manage.py makemigrations && python manage.py migrate
```
### Step10:
Then create Superuser to access admin panel
``` bash
python manage.py createsuperuser
```
### Step11:
Run the server 
``` bash
python manage.py runserver
```

### Step12:
Facebook authentication:\
[Got o the Facebook for Developers login and add new app](https://developers.facebook.com/apps)\
Then Click the button ```Tune``` under Login with Facebook\
![img1](./media/README_screanshots/Screenshot_normname_1.png)\
After that  Select WEB.\
Enter your  host url here\
![img2](./media/README_screanshots/img.png)\
then click save and continue.\
Turn on work-mode for production server\
![img3](./media/README_screanshots/Screenshotno.png)\
this will take more additional steps.
Click  Basic setting  and fill  ```privacy policy URL``` field.
#### Step12.2:
Then go to the admin panel ```host:/admin``` and login with superuser login and password\
navigate to ```SOCIAL ACCOUNTS```>```Social applications```  click add and 
fill fields. Example picture above. Your app id and secret key you can find inside your basic-setting\
then click save.\
![img4](./media/README_screanshots/img_1.png)
### Step13:
LinkedIn authentication:
[go to Linkdin Developer](https://developer.linkedin.com/) login and click ```My Apps``` creat a new app.\
Then navigate to > ```Auth```.There you need to fill ```Authorized redirect URLs for your app``` like this
```your-host/linkedin_oauth2/login/callback/``` then  register LinkedIn app  on your admin panel like ```Step 12.2```.


> **WARNING**: For serving static files in production [check documentation](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/) 

