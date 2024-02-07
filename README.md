# Build Fast and Efficient Python Applications Using Threads

Source code for the O'Reilly live online training with Lee Gaines.

We will use a Python3 Docker image to run the code. Assuming you have [installed Docker](https://docs.docker.com/get-docker/), navigate to the `src/threads` directory of this repo, then build the image with the following command:

```
docker build -t py3-threads .
```

To access the shell, run a container using this command:

```
docker run -it py3-threads bash
```

All of the source code will be located in the `/src` directory in the container. To sync this directory with your working directory when you run the container, use this command:

```
docker run -it --mount type=bind,source=$$(pwd),target=/src py3-threads bash
```

If you have `make` you can use the following command to automate the build and run commands:

```
make run
```

## Tips and Notes

* To view the threads as a program is running with `htop`: `htop` -> `F2` -> `Show custom thread names` (tree view is nice, too)
* To view the threads as a program is running `ps`: `ps -elF`
* Show information about the current thread: `threading.current_thread()`
* *Green threads* are scheduled by the Python process, as opposed to a system-level thread scheduled by the OS.
