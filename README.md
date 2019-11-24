# intro
This is our effort to join in Apkathon competition 2019 ref. https://aptechvietnam.com.vn/apkathon2019

# wire up selenium hub & a chrome node
```bash
: you@localhost:/path/to/cloned/code
./docker/stop.sh; ./docker/compose-up.sh               
```

# run test
```bash
pipenv sync
pipenv run pytest
```

#run login_fb.py
pipenv run python -m  src.scenario.login_fb.py 



