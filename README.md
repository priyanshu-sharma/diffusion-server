# diffusion-server
This repository is responsible for maintaining diffusion-related APIs 

## Setup

1. Create conda environment using python=3.11

```
conda create -n "env_diffusion_server" python=3.11
```

2. Install all required python packages using

```
pip install -r src/diffusion_api/requirements.txt
```

3. If you are on Windows install psycopg2 (Only for Windows Users)

```
pip install psycopg2==2.9.6
```

4. Install psycopg on Linux (Only for Linux and Mac Users)

```
pip install psycopg2-binary==2.9.6
```

5. Run the run_entire_flow.ipynb file to see the demo.

## Design Decision

Extented this Diffusion API Server with Django Framework for better modularity. Run the following command to see the API server.

```
python src/diffusion_api/manage.py runserver
```

(Note) - In case of CUDA Out-of-Memory Error (OOMKilled). Comment out the following code in "src/diffusion_api/manage.py"

```
from services import *
```

After starting up the server, use this http://127.0.0.1:8000/docs link to see all the APIs along with Documentation (This is powered by Swagger API)

Designs Aspects -

1. Right now, this server is only responsible for serving the backend Diffusion-related API, we can further extend the same repo for various other projects related to diffusion Example - UI for Diffusion Server, Monitoring Service for Diffusion Server, just by initializing the project in src/ folder.

2. In order to see the entire code in flow. Just open "src/diffusion_api/run_entire_flow.ipynb" file and run the command according to usecase to get the desired results.

3. Further in "src/diffusion_api/" folder, we have "dataset_domain" for everything related to data. In order to add new images just add the images inside the "src/diffusion_api/dataset_domain/images/" folder and add the same in "src/diffusion_api/tasks/random_diffusion.py" in preprocess() function. Add the images with "dataset_domain/images/" prefix in the self.images list.

```
self.images = [....]
```

4. Complete end-to-end flow is implemented in "src/diffusion_api/tasks/random_diffusion.py" file. It takes a list of prompt as a input and randomly choose a prompt and model from the given input list for generating a new image.

5. All the diffusion models are defined in "src/diffusion_api/services/" and I have created a Singleton Class for all the models ("src/diffusion_api/services/__init__.py"), which can be initialize only once during the entire lifetime. (Reason - Preboot the model, fasten up the process.)

6. In order to add new models and initialize them, we just need to define them first and then add them in ("src/diffusion_api/services/__init__.py") and rotate the Kubernetes Pods to get the new ineffect. 

7. Extend an API for Random Diffusion process on this endpoint - ("api/image_model_domain/v1/random_diffusion/1/initialize_diffusion/"). One can access the API after running the server using "runserver" command

Here is the curl for the API.

```
curl --location 'http://127.0.0.1:8000/api/image_model_domain/v1/random_diffusion/1/initialize_diffusion/' \
--header 'accept: application/json' \
--header 'X-CSRFToken: CqxzMEg1qWowaBbEtv4ElCjQhkCaTSXs82ybXVNsvBODkTELX4lAJuZhksQlHs5E' \
--header 'Content-Type: application/json' \
--data '{
    "prompt_list": ["cat dancing in rain"]
}'
```

8. We can further enchance the performance by caching the frequently used images and can add django-redis in order to efficiently solve this. - (https://github.com/jazzband/django-redis)

9. For the given usecase, we can have as many new images as possible. In order to accomodate and manage these images properly, I created a model for the Image ("src/diffusion_api/image_model_domain/models/images.py") and similarly for models also (in-case we need to managed very large number of models), we have Dlmodels ("src/diffusion_api/image_model_domain/models/dlmodels.py").

10. In order to populate these table use the fixtures defined in "src/diffusion_api/fixtures" folder. You can use the following command to populate the data.

```
python src/diffusion_api/manage.py loaddata src/diffusion_api/fixtures/*.json
```

## Results

For 17 images, with 4 different random choosen diffusion model, I am able to generate new images for all 17 images within 

Total Time Taken - 44.27491855621338 seconds

Memory Usage is around - 7627.07421875 MB

Average Time/Image - 2.60 seconds

You can also get the results for your images by running the run_entire_flow.ipynb file.

** (Note) - I have didn't process all the images for single models in one go as I was getting the cuda memory error. But it is can be easily done with server. (I have commented out the code for parallel processing of image in "src/diffusion_api/tasks/random_diffusion.py" under perform_diffusion() function)

