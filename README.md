# news-search
New commit.
Please create a results folder in the root directory of the project.


# How to get it
```
docker pull kalel1130/news-search:latest
```
Create a data folder in the root directory of the project to put the useful and useless lists csvs.

Create a results folder in the root directory of the project.

# How to run it
```
docker run -it --rm -v "$(pwd)/results:/app/results" -v "$(pwd)/data:/app/data" kalel1130/news-search:latest
```
