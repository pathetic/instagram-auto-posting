# Instagram Auto Posting

Simple python script that logs in into your account using [InstaBot](https://pypi.org/project/instabot/) and posts a random photo each x hours using [schedule](https://github.com/dbader/schedule). 

## Installation

```bash
pip install -r requirements.txt
```

## Usage
Update your config.py with your details.  
Change the amount of x hours you want a photo to be posted in main.py file at line 49. 
```python
schedule.every(4).hours.do(run_threaded, upload_pictures)
```
And run the script.
```bash
python main.py
```
## Recommendations
If you want to use the script on a VPS, use a VPN from your country in order to avoid any issues with the authentication.  
If the script does not work, try to change your account type to business.  
Make sure the photos are in .jpg format.
## License
[MIT](https://choosealicense.com/licenses/mit/)