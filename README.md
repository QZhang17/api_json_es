# api_json_es

### API for querying harvard_dataverse.json datasets with elasticsearch

### Prerequisites:

Create conda environment with python and activate
```
conda create -n env_name python=3.8 anaconda
conda activate env_name
```

Install elasticsearch and flask:

```
pip install elasticsearch
```
```
pip install flask
```
Set up Jupyter Notebook for coding and testing:
```
pip install notebook
```

Run notebook:
```
jupyter notebook
```
### Run

Run elastic search:
```
elasticsearch
```

Load data into elastic search
```
python3 index_json_file.py
```

Spin up Flask API:
```
python3 api_json.py
```

### Example Queries

#### Get data by the '@id' field in the data
```
localhost:5000/query_id?id=https://doi.org/10.11588/data/0HJAJS
```

#### Query by a field in the JSON data
```
localhost:5000/query?keywords=Earth and Environmental Sciences
```
```
localhost:5000/query?funder.name=United States Agency
```
```
localhost:5000/query?author.name=Herfort, Benjamin
```
