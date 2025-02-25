# Theoretical Questions

## 1️⃣ Deployment on AWS
**Explain how you would deploy the above application on AWS**

I would deploy the API using **AWS ECS (Fargate)** for the backend and **Amazon RDS (PostgreSQL)** for the database.

### **1️⃣ Services Used:**
- **Docker** → Package the API into a container.
- **AWS ECS (Fargate)** → Run the container without managing servers.
- **AWS RDS (PostgreSQL)** → Store user health data.
- **AWS ALB (Load Balancer)** → Distribute traffic.
- **AWS CloudWatch** → Monitor logs and performance.
- **GitHub Actions** → Automate deployment.

### **2️⃣ Deployment Steps:**
1. **Build a Docker image and push it to AWS ECR.**  
2. **Create a PostgreSQL instance in AWS RDS** and connect the API to it.  
3. **Set up AWS ECS (Fargate)** to run the container.  
4. **Attach an AWS Load Balancer** to handle traffic.  
5. **Enable CloudWatch** for logs and monitoring.  
6. **Use GitHub Actions for CI/CD**, so every push to `main` automatically deploys the latest version.  

### **📌 Conclusion**
This deployment approach **removes the need to manage servers**, scales easily, and ensures **reliability and security**. 🚀

---

## 2️⃣ Scaling & Troubleshooting
**Imagine the health tracker application has become wildly popular, gaining thousands of new users every day. However, users start reporting the following issues:**
- Health scores are inaccurate.
- API responses are delayed.
- The application occasionally crashes under load.

### **Questions:**
- **How would you approach diagnosing and solving this problem?**
- **How would you design a long-term plan to make the system resilient to future scalability challenges?**

