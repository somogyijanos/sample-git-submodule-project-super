# Sample Superproject using `git submodule`
This is a sample superproject which is using the repository [`sample-git-submodule-project-mymodule`](https://github.com/somogyijanos/sample-git-submodule-project-mymodule) as a sample module (git submodule).

## Features
- repository with docker compose environment
- just a silly tool to:
    1. print hello world,
    2. count files and folders in an input path using Python 3.12

## Usage

### Run from command line
Startup the environments:
```bash
cd sample-git-submodule-project-super
docker compose up -d
```
Then run the scripts, each of them will run in the corresponding environment:
```bash
docker compose exec core python scripts/run-core.py
docker compose exec mymodule python scripts/run-mymodule.py <path-in-container>
```

Or for convenience, there is an example in [run.sh](./scripts/run.sh) you can run directly:
```bash
bash scripts/run.sh
```

### Develop from VS Code
Open VS Code, select `Dev Containers: Open Folder in Container...`
then select the `sample-git-submodule-project-super` repository you cloned before. After that you'll be asked to select the development environment (devcontainer). For this repository, there are two:
- `core`  
    This is a devcontainer for developing and running code specific for this repository.
- `mymodule`  
    This is a devcontainer for developing and running code where code from the `sample-git-submodule-project-mymodule` repo is used.

Select one, then open a new window of VS Code and open the repository again, now with the other devcontainer. Now you'll have two VS Code windows, both of them are devcontainers, both have the repository open but they have two different environments.

From the scripts run above you can test each of them in their corresponfing environment. In the corresponding window/devcontainer open a terminal at the reposiytiry root (`/sample-git-submodule-project-super`) and run:
- core  
    ```bash
    python scripts/run-core.py
    ```
- mymodule  
    ```bash
    python scripts/run-mymodule.py
    ```
The good thing is, you can not only work/commit/push regarding the `sample-git-submodule-project-super` repository but you can also simoultaneously work on the module repository `sample-git-submodule-project-mymodule`. You can push the changes there and in another superproject you cann pull those changes and update you submodule to the latest version.