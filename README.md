# Virtual_Assistant
### I am interested in making some stuff work for me, and then enhance those to make that work for others

I used Ubuntu 16.04 and python3.7 for this project. I recommend to create a virtual environment for every project to
keep the requirements of each project separate.

After defining a virtual environment, you need to install all the requirements using requirement.txt.
Therefore, cd to the main directory, then run the following command
#### pip install -r requirement.txt

#### Generate API_Key in [wolframalpha](https://developer.wolframalpha.com/portal/myapps/index.html "wolframalpha")
1. First sign up for free
2. Generate AppID
3. I recommend not to use this ID directly inside code, but store it as an environment variable or in configuration file.
    (I have used the second option for this code, so if you are running my code, then please create a config.json file
    within the same folder, and copy your AppID under key as "api_key")


With these settings in hand, you are good to run [pyda.py](https://github.com/chandms/Virtual_Assistant/blob/master/pyda.py)

### User will have to type query in the search box, if searchable, then user will be able to see result popup
### and voice note of the same.
1. For searching, I have used wolframalpha, and wikidepia libraries
2. For voice note, I have used espeak
