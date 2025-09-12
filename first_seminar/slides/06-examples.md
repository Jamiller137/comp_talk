## Installation:

```shell
pip install umap-learn
```

- Python >= 3.6 
- NumPy
- SciPy
- Numba
- PyNNDescent


## Import 

```language-python
import umap
reducer = umap.UMAP()
# Fit data and return output
embedding = reducer.fit_transform(data)
```


## ```umap.UMAP()```

- ```n_neighbors``` (15): Local neighborhood size.
- ``` n_components```  (2): Output dimension
- ``` metric ```  ('euclidean'): Distance metric
- ``` min_dist ``` (0.1) Min dist between output
- ``` spread ``` (1.0) Scale of embedded points


## 3D Example:
```python
# 3D embedding
reducer = umap.UMAP(
    n_components=3,
    n_neighbors=50
)
embed_3d = reducer.fit_transform(data)
```


## Cosine Distance Example:
```python
# cosine distance
reducer = umap.UMAP(
    metric='cosine'
)
```
Custom metrics must be a Numba jit'd function which takes two 1D arrays and returns a float
- aka, decorated with ```@numba.jit()```


## Supervised Embedding:
```Python
reducer.fit_transform(data, y=labels)
```


## Inverse Example:
```Python
# transform back to original space
X = reducer.inverse_transform(x)

```
