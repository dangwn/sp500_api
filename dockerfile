# Start from the miniconda image
FROM dangawne/ubuntu_miniconda3x

# Copy the source code into the docker container
COPY ./app /app

# Create the conda environment
WORKDIR /app
RUN conda env create --file ./envs/env_flask.yml

# Activate env and run app
ENTRYPOINT ["conda", "run", "-n", "api-env","python","./app.py"]