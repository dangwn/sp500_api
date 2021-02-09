# Start from the miniconda image
FROM dangawne/ubuntu_miniconda3x

# Copy the source code into the docker container
COPY ./model_api /model_api

# Create the conda environment
WORKDIR /model_api
RUN conda env create --file ./env_flask.yml
