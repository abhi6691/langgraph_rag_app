# Use the AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.9

# Install additional dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the CMD to your Lambda handler
CMD ["src/app.lambda_handler"]
