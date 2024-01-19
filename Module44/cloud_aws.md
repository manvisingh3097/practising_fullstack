# AWS and EC2 Deployment Guide for Romeo's E-commerce Application

## Assignment 1: Getting Started with AWS

### Creating an AWS Account

1. Visit the [AWS official website](https://aws.amazon.com/).
2. Click on "Create an AWS Account" and follow the on-screen instructions.
3. Provide accurate billing information and choose the AWS Support Plan that suits your needs.
4. Set up multi-factor authentication (MFA) for added security.
5. Review the AWS Customer Agreement and click on "Create Account and Continue."

### Security Measures for AWS Account

1. **Enable MFA:** Enable Multi-Factor Authentication to add an extra layer of security to your AWS account.
2. **IAM Users:** Create IAM (Identity and Access Management) users with the principle of least privilege, granting only necessary permissions.
3. **Security Groups and Network ACLs:** Use Security Groups and Network ACLs to control inbound and outbound traffic.
4. **AWS Key Management Service (KMS):** Use AWS KMS for encryption of sensitive data.

### Popular AWS Services for App Deployment

1. **Amazon S3 (Simple Storage Service):** S3 provides scalable object storage for storing and retrieving any amount of data. It's suitable for storing static assets, media files, and backups.

2. **Amazon EC2 (Elastic Compute Cloud):** EC2 offers resizable compute capacity in the cloud. It's widely used for deploying applications and hosting websites.

3. **AWS Elastic Beanstalk:** Beanstalk is a fully managed service that makes it easy to deploy and run applications in multiple languages.

## Assignment 2: Launching an EC2 Instance

### What is an EC2 Instance?

Amazon EC2 (Elastic Compute Cloud) is a web service that provides resizable compute capacity in the cloud. It allows users to run virtual servers, known as instances, to host applications and services.

### Launching an EC2 Instance

1. **Login to AWS Console:** Go to the AWS Management Console.
2. **Navigate to EC2:** Under "Services," select EC2.
3. **Launch Instance:**
   - Click on "Launch Instance."
   - Choose an Amazon Machine Image (AMI), e.g., Amazon Linux.
   - Select an instance type based on your application requirements.
   - Configure instance details, add storage, add tags, configure security groups.
   - Create or select an existing key pair for SSH access.

### Connecting to EC2 Instance via SSH


*  **SSH Connection:** Connect to your EC2 instance using the following command:

   ```
   ssh -i path/to/your-key.pem ec2-user@your-instance-ip
    ```

## Assignment 3: Python and MongoDB on EC2

### Installing Python and Dependencies

1. **Update Packages:**
   ```
    sudo yum update -y
    ```

2. **Install Python:**
    ```
    sudo yum install python3 -y
    ```

3. **Install Dependencies:**

* Install any additional dependencies required for your Django application.
MongoDB Setup on EC2
* Install MongoDB:

    ```
    sudo yum install -y mongodb-server
    ```

* Start MongoDB:
    ```
    sudo service mongod start
    ```

4. **Create Database and Collections:**

* Access the MongoDB shell:
    ```
    mongosh
    ```

* Inside the MongoDB shell, create the database and collections:
    ```
    mongodb
    use ecommerce_db
    db.createCollection("products")
    db.createCollection("orders")
    ```


## Assignment 4: Deploying and Managing the Application on EC2

## Deploying Django Application

**Copy Application Code:**

* Use scp or other methods to copy your Django application code to the EC2 instance.

**Install Requirements:**

    ```
    pip3 install -r requirements.txt
    ```

**Run Migrations:**

```
python3 manage.py migrate
```

**Start Django Application:**

```
python3 manage.py runserver 0.0.0.0:8000
```

**Settings.py Configuration**

*Update Allowed Hosts:*

* In settings.py, add your EC2 instance's public IP to the ALLOWED_HOSTS list:

```
ALLOWED_HOSTS = ['your-ec2-public-ip']
```

Ensure that the EC2 instance's security group allows incoming traffic on port 8000.
Access Django APIs:

In Postman, make requests to your EC2 instance's public IP on port 8000.


