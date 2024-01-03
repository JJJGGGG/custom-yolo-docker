FROM python:3.9.18

WORKDIR /code

# Download YOLOv8 custom Model (saved in drive)

RUN mkdir /code/sam_images
RUN pip install gdown

RUN gdown 1pB_7eVrncxwXc84uA8YyEVQjijrFsho8 -O /code/sam_images/custom_yolo_model.pt

# Install the requirements and libraries

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt update -y
RUN apt install libgl1-mesa-glx -y

# Copy the app code

COPY ./app /code/app

# Startup command

CMD ["uvicorn", "app.main:app", "--host", "::", "--port", "80"]
