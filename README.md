# Book Genre Classifier: Precision in Varied Approaches

Embark on the fascinating journey of the Book Genre Classifier, a project immersing you in the intricate world of categorizing books. This adventure goes beyond conventional methods to ensure precise predictions of book genres through various approaches.

**Fine-Tuning with Huggingface Transformer LLM:**
In the first phase of our adventure, experience the unveiling of the nuanced art of predicting book genres. We fine-tune a Huggingface Transformer Language Model (LLM), incorporating cutting-edge technology for enhanced accuracy.

**PEFT/LoRA Technique Unveiled:**
Delve into an additional fine-tuning technique—the PEFT/LoRA method. Discover its potential in genre classification, adding sophistication to our model and broadening the scope of precision.

**Scikit-Learn Classification Odyssey:**
Join us on an engaging exploration of scikit-learn's classification saga. Immerse yourself in the world of Support Vector Classifier (SVC), Naive Bayes (NB), and Random Forest (RF) classifiers. Highlighting the distinct strengths of each model, this journey showcases the blend of classical and modern approaches.

**Flask App for Seamless Interaction:**
Beyond technical complexities, experience the user-friendly side of the Book Genre Classifier. Our Flask app provides a smooth interface for users to interact with the classification system, making the exploration of genres an enjoyable and intuitive process.

**Docker Deployment for Efficiency:**
Witness the efficiency of our deployment through Docker. We encapsulate the Book Genre Classifier into a Docker container, ensuring portability and easy replication across different environments.

**Docker Image on the Horizon:**
Explore the encapsulated magic with our Docker image, capturing the essence of precision in book genre classification. This image represents the culmination of our efforts, ready to be shared, tested, and deployed.

**Scaling Up with AWS EC2:**
For those aiming for a broader horizon, we guide you through deploying the Book Genre Classifier on AWS EC2. Scale up the reach of your classifier, making it accessible to a wider audience.

## Table of Contents

1. [Project Highlights](#project-highlights)

2. [Why Book Genre Classifier?](#why-book-genre-classifier)

3. [Get Started](#get-started)

4. [Docker Deployment](#docker-deployment)

5. [Test Using Docker Hub Image](#test-using-docker-hub-image)

6. [Deploying on AWS EC2](#deploying-on-aws-ec2)


## Project Highlights

- **Transformer LLM Fine-Tuning:** Delve into the sophistication as we fine-tune a Huggingface Transformer Language Model (LLM) to unveil the nuanced art of book genre prediction. Find detailed insights in the notebook file [Book_Genre_Prediction.ipynb](https://github.com/adinmg/book_genre_classifier.git/Book_Genre_Prediction.ipynb).

- **PEFT/LoRA Technique:** Explore an additional fine-tuning technique, the PEFT/LoRA method, shedding light on its potential in genre classification. Refer to [Book_Genre_Prediction.ipynb](https://github.com/adinmg/book_genre_classifier.git/Book_Genre_Prediction.ipynb) for a comprehensive understanding.

- **Scikit-Learn Classification Odyssey:** Immerse yourself in a captivating exploration as we leverage scikit-learn's Support Vector Classifier (SVC), Naive Bayes (NB), and Random Forest (RF) classifiers, highlighting the unique strengths of each model. Find detailed insights in the notebook file [Book_Genre_Prediction.ipynb](https://github.com/adinmg/book_genre_classifier.git/Book_Genre_Prediction.ipynb).


## Why Book Genre Classifier?

It's challenging to determine a book's genre based on its title and summary, but it's essential for several reasons:

- **Enhanced Recommendations:** Elevate book recommendations with a classifier that comprehends genres at a nuanced level, offering users personalized and accurate suggestions.

- **Insights into Literary Trends:** Uncover hidden patterns in literary success by exploring the relationship between book genres and their portrayal in summaries.

- **Recommendation Systems:** A robust genre classifier assists recommendation systems in providing readers with more personalized book recommendations, leading to increased reader engagement on digital platforms.

- **Literary Success:** Understand the correlation between genres and their portrayal in summaries to gain insights into what makes books commercially successful or where improvements can be made.

- **Book Themes and Trends:** Study book genres to better understand the prevailing themes and trends in the publishing industry, providing valuable insights for cultural and societal studies.

## Get Started

Clone the Book Genre Classifier repository and explore the precision of diverse approaches to revolutionize book genre classification.

```bash
git clone https://github.com/adinmg/book_genre_classifier.git
```

### Requirements

Ensure a seamless setup by installing the required packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Flask Integration

1. Navigate to the project directory:

   ```bash
   cd book_genre_classifier
   ```

2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Access the Book Genre Classifier at `http://127.0.0.1:5000/` in your web browser to interact with the classification system.

## Docker Deployment

1. Ensure Docker is installed on your machine.

2. Build the Docker image:

   ```bash
   docker build -t book_classifier-app .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 5000:5000 book_classifier-app
   ```

4. Access the Book Genre Classifier at `http://127.0.0.1:5000/` in your web browser to experience the precision of diverse approaches in book genre classification.

## Test Using Docker Hub Image

1. To test the Book Genre Classifier using the image from Docker Hub, execute the following command:


    ```bash
    docker pull adinmg/book_classifier-app:v1
    ```

2. Run the Docker Container:

    ```bash
    docker run -p 5000:5000 adinmg/book_classifier-app:v1
    ```

This command assumes that the application inside the container exposes port 5000 and maps it to the same port on your host machine.

3. Accessing the Classifier:

After the container is running, you might access the Book Genre Classifier by opening your web browser and navigating to `http://127.0.0.1:5000/`.

## Deploying on AWS EC2

1. **Create an AWS EC2 Instance:**
   - Log in to your AWS Management Console.
   - Navigate to EC2 and launch a new instance.
   - Choose an appropriate Amazon Machine Image (AMI) and configure instance details.

2. **Configure Security Groups:**
   - Set up security groups to allow inbound traffic on the necessary ports (e.g., 5000 for Flask).

3. **SSH into the EC2 Instance:**
   - Use the provided key pair to SSH into your EC2 instance.

4. **Clone the Repository:**
   - Clone the Book Genre Classifier repository into your EC2 instance:

   ```bash
   git clone https://github.com/adinmg/book_genre_classifier.git
   ```

5. **Install Dependencies:**
   - Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
   Unicorn is already in the requirements.

6. **Test the App in Gunicorn:**
   - Run the app using Gunicorn:

   ```bash
   gunicorn -b 0.0.0.0:8000 app:app
   ```

   (Make sure you are in the app folder)

7. **Configure Gunicorn Service:**
   - Create a Gunicorn service configuration file:

   ```bash
   sudo nano /etc/systemd/system/myapp.service
   ```

   **"myapp".service:**

   ```ini
   [Unit]
   Description=gunicorn instance for a simple flask app
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/book_genre_classifier
   ExecStart=/home/ubuntu/myenv/bin/gunicorn -b localhost:8000 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

8. **Restart Daemon:**
   - Reload the systemd daemon to apply the changes:

   ```bash
   sudo systemctl daemon-reload
   ```

9. **Start the Gunicorn Service:**
    - Start the Gunicorn service:

    ```bash
    sudo systemctl start myapp
    ```

10. **Enable the Gunicorn Service:**
    - Enable the Gunicorn service to start on boot:

    ```bash
    sudo systemctl enable myapp
    ```

11. **Install Nginx:**
    - Install the Nginx web server:

    ```bash
    sudo apt install nginx
    ```

12. **Start Nginx:**
    - Start the Nginx service:

    ```bash
    sudo systemctl start nginx
    ```

13. **Enable Nginx:**
    - Enable Nginx to start on boot:

    ```bash
    sudo systemctl enable nginx
    ```

14. **Edit Nginx Default File:**
    - Open the default Nginx configuration file for editing:

    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

15. **Modify Default File:**
    - Add the following upstream block and modify the location block:

    ```nginx
    # Default server configuration (add)
    upstream myapp {
        server 127.0.0.1:8000;
    }

    # modify location
    location / {
        ...
        proxy_pass http://myapp;
    }
    ```

16. **Restart Nginx:**
    - Restart the Nginx service to apply the changes:

    ```bash
    sudo systemctl restart nginx
    ```

17. **Debug NGINX if necessary:**
    - Check the Nginx error log for debugging:

    ```bash
    sudo tail /var/log/nginx/error.log
    ```

Now, your Book Genre Classifier is deployed on AWS EC2 with Gunicorn and Nginx for efficient and reliable web service.
