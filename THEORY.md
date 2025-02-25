# Theoretical Questions

## 1️⃣ Deployment on AWS
**Explain how you would deploy the above application on AWS**

I would deploy the API using **AWS ECS (Fargate)** for the backend and **Amazon RDS (PostgreSQL)** for the database.

### Services Used:
- **Docker** – Package the API into a container.
- **AWS ECS (Fargate)** – Run the container without managing servers.
- **AWS RDS (PostgreSQL)** – Store user health data.
- **AWS ALB (Load Balancer)** – Distribute traffic and manage HTTPS.
- **AWS Secrets Manager** – Store database credentials securely.
- **GitHub Actions** – Automate deployment.

### Deployment Steps:
1. Build a Docker image and push it to AWS ECR.
2. Create a PostgreSQL instance in AWS RDS and store credentials in AWS Secrets Manager.
3. Deploy the container to AWS ECS (Fargate) with auto-scaling enabled.
4. Use AWS ALB to distribute traffic and manage SSL/TLS.
5. Set up CloudWatch logs for API requests and error monitoring.
6. Automate deployment via GitHub Actions.

### Conclusion
This setup ensures the API is scalable, secure, and easily maintainable without managing servers manually.

---

## 2️⃣ Scaling & Troubleshooting
**Imagine the health tracker application has become wildly popular, gaining thousands of new users every day. However, users start reporting the following issues:**
- Health scores are inaccurate.
- API responses are delayed.
- The application occasionally crashes under load.

### Questions:
- **How would you approach diagnosing and solving this problem?**
- **How would you design a long-term plan to make the system resilient to future scalability challenges?**

### Diagnosing and solving the problem

1. **Check data accuracy**
   - Identify if health score miscalculations are due to delayed or missing data.
   - Monitor database read and write times to detect slow queries.

2. **Analyze performance bottlenecks**
   - Use AWS RDS Performance Insights to identify slow SQL queries.
   - Check database connection pooling to avoid bottlenecks.
   - Implement Redis caching to reduce the number of queries hitting the database.

3. **Protect the system from overload**
   - Enable ECS auto-scaling to handle traffic spikes.
   - Scale RDS with read replicas to distribute query load.
   - Implement rate limiting in the API to prevent excessive requests from a single user.
   - Monitor key metrics in CloudWatch to detect early signs of performance degradation.

### Long-term scalability plan

1. **Optimize database performance**
   - Use read replicas and connection pooling to reduce primary database load.
   - Periodically archive old data to prevent table size from impacting query performance.

2. **Asynchronous processing for heavy tasks**
   - Move complex health score calculations to a task queue (Celery + Amazon SQS).

3. **Resilient API architecture**
   - If traffic grows beyond ECS limits, migrate to AWS EKS (Kubernetes) for better resource allocation.
   - Implement an API Gateway with built-in caching and rate limiting.

This approach ensures that the system remains stable under high load while keeping performance optimal.

