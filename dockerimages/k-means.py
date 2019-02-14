import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.cm as cm

from sklearn.datasets.samples_generator import make_blobs
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50)

# make blobs is used to generate synthetic dataset
# make blobs returns a dataset with independent and target variables

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
y_kmeans = kmeans.fit_predict(X)

#prediction means is every value in dataset will be assigned to its own cluster.
#while fitting kmeans will learn which cluster, so no need to transform

np.bincount(y_kmeans)

kmeans.cluster_centers_

def plot_clusters(data, clusters, y):
    plt.scatter(data[:,0], data[:, 1],c=y, s=50, cmap='viridis')
    centers = clusters.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5 )
    
plot_clusters(X, kmeans, y_kmeans)

from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

#distance based algorithms are basically very sensitive to data,
# so we apply standard scaling to our data so we have data near to 0.


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(cancer_data.data)
X_cancer = scaler.transform(cancer_data.data)

kmeans = KMeans(n_clusters=2)
cancer_kmeans = kmeans.fit_predict(X_cancer)
kmeans.cluster_centers_

plot_clusters(X_cancer, kmeans, cancer_kmeans)


labels = np.zeros_like(cancer_kmeans)

# homogeneity score
'''
A clustering result satisifies homogeneity if all of its clusters contain only data points which are members of a single class
'''

# Completeness score.

'''
A clustering result satisifies completeness if all the data points that are members of a given class are 
elements of a same cluster

'''


from scipy.stats import mode
from sklearn.metrics import accuracy_score


accuracy_score(cancer_data.target, cancer_kmeans)

