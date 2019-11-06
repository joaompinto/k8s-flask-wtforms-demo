Flask + WTForms + Kubernetes Deployment
=======================================

# Test locally (using Python3)
```bash
pip3 install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app --config=config.py
# Browse to http://127.0.0.1:5000/
```

# Test locally (using Docker)

```bash
docker build -t kubernetes-flask-wtforms:latest .
docker run -p 5000:5000 kubernetes-flask-wtforms:latest
# Browse to http://127.0.0.1:5000/
```

# JMeter Test plan
A [test plan](SimpleTestPlan.jmx) for JMeter is provided.

# Demo Screenshot

![Flask Web Demo](images/FlaskWebForm_demo.png "ok")

