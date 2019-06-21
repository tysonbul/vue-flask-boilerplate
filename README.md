# Vue+Flask Boilerplate

A boilerplate project for anyone seeking to use Vue with a Python Flask backend.

The Vue project is setup through the Vue-CLI, with options to include the router and a Vuex Store, along with ESLint+Prettier formatting.

The Flask part is a custom setup I use personally, with a versionable API layer, and some custom exception handling to build on.

It also includes a with a Dockerfile for production and staging builds.

## System requirements
* Python 3.6+
* Node + NPM
* (Optionally) Docker



## Project setup

This assumes you have installed Python3.6+ and NPM.

### Clone the project

```
git clone https://github.com/tysonbul/vue-flask-boilerplate.git
cd vue-flask-boilerplate
```

### VueJS Setup
Use NPM to install the VueJS dependencies
```
npm install
```

### Python Flask setup
Install venv and initialize virtual environment 

```
python3 -m pip install venv # install venv if not already installed
venv venv
source venv/bin/activate # activates the virtual environment
```

Install Python dependencies
```
pip3 install -r requirements.txt
```



## Running the project

### Run both Flask Server and Vue webpack server, both with compiles and hot-reloads

**Recommended for** general development or rapidly developing features. 

*Only tested on Unix OS's

```
npm run dev
```

This will run the both the vue-cli-service and Flask server and run by default on [localhost:8080](http://localhost:8080). This works because there is a setting in the vue.config.js that proxies api/ requests from the server running on 8080 to the Flask server running on 5000.

### For compiles and hot-reloads Vue files for development

**Recommended for** only developing frontend components with no requirement of server endpoints. 

```
npm run serve
```

**NOTE**: This will run the vue-cli-service and run by default on [localhost:8080](http://localhost:8080), serving only the Vue content. NOT the Python Flask server. If you want to run both check out the above command `npm run dev` 

### For compiles and hot-reloads Flask for development

**Recommended for** when only working with Backend code and will be hitting the API with something like Postman, or will be using a debugger on the backend Python code.

```
npm run flask
```

**NOTE**: This will run ONLY the Flask server on [localhost:5000](http://localhost:5000). If you want to run both check out the above command `npm run dev`. ALSO before you run this you must run `npm run build` to compile the Vue pages for the server to serve at least once. 

### For compiles and minifies Vue files for production

```
npm run build
```

### Run your Vue tests
```
npm run test
```

### Lints and fixes Vue files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



## Using the Docker image

I've supplied a simple Docker image for building the project useful if the project will be deployed in a cluster, such as with AWS ECS. You may even choose to develop on it with some extra steps.

### Build docker image

First, ensure docker is installed and running on your local system.

Then, build the docker image specifying the environment [development|staging|production]. Defaults to 'staging'.

```
docker build --build-arg ENV='staging' -t my-vue-flask-app:latest . # run in project root
```

### Run docker image

```
docker run -it --rm --name my-vue-flask-app -p 5000:5000 my-vue-flask-app:latest
```

Check [localhost:5000](http://localhost:5000) and you should see the Hello World Vue app.