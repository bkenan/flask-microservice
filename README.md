# Portfolio demo website using AWS Elastic Beanstalk


### How to run it in AWS:


1. Clone this repo and cd into it

2. Create a Python virtualent: `python3 -m venv ~/.eb`

3. Source virtual envirnment: `source ~/.eb/bin/activate`

4. Install all dependencies: `make all`

5. Initialize new eb app by: `eb init -p python-3.7 <your app name> --region us-east-1`

6. Create remote eb instance: `eb create <your app name>-env`
