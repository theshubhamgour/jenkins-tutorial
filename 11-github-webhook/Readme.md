# 🧩 Jenkins Tutorial – Flask CI/CD Project [Webhook Explained]

## 🔗 What is a Webhook?

A **webhook** is a way for one system to send real-time data to another system as soon as an event occurs.  
It’s like an automatic “notification” that carries data about an event.

In simple terms:
- **GitHub** is the source system — it detects an event like a code push.
- **Jenkins** is the destination system — it listens for that event.

When you push code to GitHub, the webhook sends an **HTTP POST request** to Jenkins with details about the event (like branch, commit, etc.).  
Jenkins receives that payload and automatically triggers a build or deployment.

<img width="2878" height="1622" alt="image" src="https://github.com/user-attachments/assets/6b6a76b4-2f9d-4402-9877-4bb13e112c8d" />


<img width="2878" height="1628" alt="image" src="https://github.com/user-attachments/assets/16df22a9-c0f4-4d4b-9000-ae2cfd3ba393" />


**Example:**
When you push a commit to your Flask project’s GitHub repo, Jenkins (through the webhook URL) detects it and automatically starts the pipeline — building a Docker image, running tests, or deploying your app.

This enables **Continuous Integration (CI)** and **Continuous Deployment (CD)** without manual intervention.

---

<img width="2880" height="1624" alt="image" src="https://github.com/user-attachments/assets/ef5dd2a2-364d-475c-992a-8678c1c0eda8" />

**Webhook URL format:**

```
<JENKINS_URL>/github-webhook/
```


<img width="2880" height="1162" alt="image" src="https://github.com/user-attachments/assets/9838bb58-62b5-4f2d-a5ea-47b2e1af1c7e" />

- The Jenkins server must be accessible from the internet (public IP or ngrok).  
- GitHub sends POST requests to this URL whenever configured events (like push or PR) occur.


<img width="2876" height="798" alt="image" src="https://github.com/user-attachments/assets/ab5a6b45-c609-4f35-b039-dda1325aaa4d" />

---

**In summary:**  
Webhooks make Jenkins *react automatically* to GitHub changes — enabling seamless automation in DevOps pipelines.

