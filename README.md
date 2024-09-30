# news-search
New commit.
Please create a results folder in the root directory of the project.


# How to get it
```
docker pull kalel1130/news-search:latest
```

Create a results folder in the root directory of the project.

# How to run it
```
docker run -it --rm -v "$(pwd)/results:/app/results" -v "$(pwd)/data:/app/data" kalel1130/news-search:latest
```
