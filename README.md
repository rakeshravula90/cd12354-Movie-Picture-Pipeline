Movie Picture Pipeline

A complete CI/CD implementation for the Movie Picture application using GitHub Actions, Docker, Amazon ECR, Amazon EKS, and Kubernetes.

This project demonstrates automated linting, testing, Docker image creation, image publishing to Amazon ECR, and deployment to Amazon EKS.

Project Overview

The Movie Picture application consists of:

Frontend — React application

Backend — Flask API

Docker — Containerization for frontend and backend

Amazon ECR — Container image registry

Amazon EKS — Kubernetes deployment platform

Kubernetes LoadBalancer Services — Public access to the application

GitHub Actions — Continuous Integration and Continuous Deployment

The final application was successfully deployed and verified on Amazon EKS.

Architecture

                    GitHub Repository
                           |
                           v
                  +------------------+
                  |  GitHub Actions  |
                  +------------------+
                     /            \
                    /              \
             Frontend CI       Backend CI
                  |                 |
                  v                 v
             Tests/Lint        Tests/Lint
                  |                 |
                  v                 v
             Docker Build      Docker Build
                  |                 |
                  v                 v
              Amazon ECR       Amazon ECR
                  |                 |
                  v                 v
             Frontend EKS      Backend EKS
                  |                 |
                  +--------+--------+
                           |
                           v
                  Kubernetes Services
                           |
                           v
                    Movie Application

CI/CD Workflows

Frontend Continuous Integration

The frontend CI pipeline performs:

Checkout source code

Set up Node.js

Install dependencies

Run lint

Run tests

Build the Docker image

Frontend CI Result

All frontend CI jobs completed successfully.



Backend Continuous Integration

The backend CI pipeline performs:

Checkout source code

Set up Python 3.10

Install Pipenv

Install dependencies

Run Flake8

Run Pytest

Build the Docker image

Backend CI Result

All backend CI jobs completed successfully.



Continuous Deployment

Frontend Continuous Deployment

The frontend CD pipeline performs:

Lint Frontend

Test Frontend

Build Docker image

Push Docker image to Amazon ECR

Deploy the image to Amazon EKS

Frontend CD Result

All frontend deployment jobs completed successfully.



Backend Continuous Deployment

The backend CD pipeline performs:

Lint Backend

Test Backend

Build Docker image

Push Docker image to Amazon ECR

Deploy the image to Amazon EKS

Wait for the Kubernetes rollout to complete

Backend CD Result

All backend deployment jobs completed successfully.



Git SHA Image Tagging

The deployment uses Git commit SHAs instead of relying on the latest tag.

This ensures that the exact image produced by a particular Git commit is deployed to the Kubernetes cluster.

Frontend Git SHA

The deployed frontend image was verified as:

527877549745.dkr.ecr.us-east-1.amazonaws.com/movie-frontend:43f2ebc737e3e18cd02e9dffa6a22aeb5ce89ab4



Backend Git SHA

The deployed backend image was verified as:

527877549745.dkr.ecr.us-east-1.amazonaws.com/movie-backend:35001b7f79d0500eb4d843456aba0c39d3f576d5



Kubernetes Deployment

The application was deployed to an Amazon EKS cluster.

Running Pods

The frontend and backend pods were verified to be running successfully.



Kubernetes Services

Both frontend and backend services are exposed using Kubernetes LoadBalancer services.



Kubernetes Resources

The deployed Kubernetes resources were verified using kubectl get all.



Application Verification

Frontend — Movie List

The deployed frontend successfully displays the movie list.



Frontend — Movie Details

The deployed frontend successfully displays movie details.



Backend API

The backend /movies API successfully returns the movie data.



Deployed Application

Frontend

The frontend was successfully exposed through an AWS Elastic Load Balancer.

Frontend endpoint:

http://k8s-default-frontend-918120c914-a2f93d65e24c7386.elb.us-east-1.amazonaws.com

Backend API

The backend API was successfully exposed through an AWS Elastic Load Balancer.

Movies API endpoint:

http://k8s-default-backend-e5c4895f7d-6af84ea1ebdab90b.elb.us-east-1.amazonaws.com/movies

These AWS LoadBalancer endpoints belong to the current deployed environment and may change if the Kubernetes infrastructure is recreated.

Repository Structure

cd12354-Movie-Picture-Pipeline/
│
├── .github/
│   └── workflows/
│       ├── frontend-ci.yaml
│       ├── frontend-cd.yaml
│       ├── backend-ci.yaml
│       └── backend-cd.yaml
│
├── setup/
│
├── starter/
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── package-lock.json
│   │   └── k8s/
│   │       ├── deployment.yaml
│   │       └── service.yaml
│   │
│   └── backend/
│       ├── Dockerfile
│       ├── Pipfile
│       ├── Pipfile.lock
│       ├── app.py
│       └── k8s/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── kustomization.yaml
│── screenshots/
│       ├── frontend-ci-workflow.png
│       ├── backend-ci-workflow.png
│       ├── frontend-cd-workflow.png
│       ├── backend-cd-workflow.png
│       ├── frontend-sha-deployment.png
│       ├── backend-sha-deployment.png
│       ├── frontend-output.png
│       ├── frontend-moviedetails-output.png
│       ├── backend-api-working-output.png
│       ├── kubectl-get-pods-output.png
│       ├── kubectl-get-services-output.png
│       └── kubectl-get-all-output.png
│
└── README.md

Technologies Used

Technology

Purpose

GitHub

Source code repository

GitHub Actions

CI/CD automation

React

Frontend application

Flask

Backend API

Python

Backend runtime

Node.js

Frontend runtime/build

Docker

Application containerization

Amazon ECR

Docker image registry

Amazon EKS

Kubernetes cluster

Kubernetes

Application orchestration

AWS LoadBalancer

Public application access

CI/CD Flow

Frontend

Git Push
   |
   v
Frontend CI
   |
   +--> Lint
   |
   +--> Test
   |
   +--> Docker Build
   |
   v
Frontend CD
   |
   +--> Docker Build
   |
   +--> Push to ECR
   |
   +--> Tag with Git SHA
   |
   +--> Deploy to EKS
   |
   v
Frontend LoadBalancer

Backend

Git Push
   |
   v
Backend CI
   |
   +--> Lint
   |
   +--> Test
   |
   +--> Docker Build
   |
   v
Backend CD
   |
   +--> Docker Build
   |
   +--> Push to ECR
   |
   +--> Tag with Git SHA
   |
   +--> Deploy to EKS
   |
   v
Backend LoadBalancer

Deployment Verification

The final deployment was verified using Kubernetes commands including:

kubectl get pods

kubectl get services

kubectl get all

The deployed container images were also verified directly from the Kubernetes deployments:

kubectl get deployment frontend   -o jsonpath='{.spec.template.spec.containers[0].image}'

kubectl get deployment backend   -o jsonpath='{.spec.template.spec.containers[0].image}'

The results confirmed that both applications were running SHA-tagged images.

Project Evidence

The docs/screenshots/ directory contains supporting screenshots for:

Frontend CI

Backend CI

Frontend CD

Backend CD

Frontend SHA deployment

Backend SHA deployment

Kubernetes pods

Kubernetes services

Kubernetes resources

Frontend application

Movie details

Backend API

Repository structure

GitHub Actions

The complete CI/CD workflow history is available in the repository's GitHub Actions section.

The successful workflows demonstrate:

Automated code validation

Automated testing

Docker image builds

Amazon ECR publishing

Amazon EKS deployment

Git SHA based deployments

Final Status

Component

Status

Frontend CI

✅ Successful

Backend CI

✅ Successful

Frontend CD

✅ Successful

Backend CD

✅ Successful

Frontend Docker Image

✅ Built & Pushed

Backend Docker Image

✅ Built & Pushed

Frontend SHA Deployment

✅ Verified

Backend SHA Deployment

✅ Verified

Frontend EKS Pod

✅ Running

Backend EKS Pod

✅ Running

Frontend LoadBalancer

✅ Working

Backend LoadBalancer

✅ Working

Movie List

✅ Working

Movie Details

✅ Working

Backend /movies API

✅ Working

Conclusion

The Movie Picture Pipeline project successfully implements an end-to-end CI/CD workflow.

Both the frontend and backend are automatically linted, tested, containerized, pushed to Amazon ECR, and deployed to Amazon EKS.

The final Kubernetes deployments were verified using Git SHA-tagged Docker images, and the deployed application was successfully tested through its frontend and backend endpoints.

Submission Repository

This project is hosted in the GitHub repository for submission and review.

Repository:

https://github.com/rakeshravula90/cd12354-Movie-Picture-Pipeline



