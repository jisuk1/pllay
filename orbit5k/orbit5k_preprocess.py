# -*- coding: utf-8 -*-
"""orbit5k_preprocess

Automatically generated by Colaboratory.
"""

import numpy as np

from pllay import *

"""#Preprocessing"""

def grid_from_points(X, by = 0.025):
    X_grid = np.zeros((X.shape[0], int(1./by), int(1./by)))
    for iOrbit in range(len(X)):
        orbit_int = np.floor(X[iOrbit] / by).astype(int) - (X[iOrbit] == (1./by)).astype(int)
        for iPt in range(len(orbit_int)):
            X_grid[iOrbit][orbit_int[iPt][0], orbit_int[iPt][1]] += 1
    # X_grid /= 1000
    X_grid = np.array(2 * tf.math.sigmoid(X_grid) - 1)  
    return (X_grid)


def orbit5k_preprocess(m0, lims, by, r, tseq, KK, dimensions, maxscale,
      nmax_diag, X_original_file_list, X_processed_file_list,
      X_grid_processed_file_list, batch_size=16):

    np.random.seed(0)

    for iNoise in range(nNoise):
          
        X = np.load(X_original_file_list[iNoise])

        X_grid = grid_from_points(X=X, by=0.025)

        X_landscape = compute_landscape_dtm(X=X,  m0=m0, lims=lims, by=by, r=r,
              tseq=tseq, KK=KK, dimensions=dimensions, batch_size=batch_size)
        X_diag = compute_diagram_dtm(X=X,  m0=m0, lims=lims, by=by, r=r,
              tseq=tseq, KK=KK, dimensions=dimensions, maxscale=maxscale,
              nmax_diag=nmax_diag, batch_size=batch_size)

        X_processed = np.hstack((
              X.reshape(5 * num_orbit_per_param, 2 * num_pts_per_orbit),
              X_landscape.reshape(5 * num_orbit_per_param, 102),
              X_diag.reshape(5 * num_orbit_per_param, 4 * nmax_diag)))
        X_grid_processed = np.hstack((
              X_grid.reshape(5 * num_orbit_per_param, 1600),
              X_landscape.reshape(5 * num_orbit_per_param, 102),
              X_diag.reshape(5 * num_orbit_per_param, 4 * nmax_diag)))

        np.save(X_processed_file_list[iNoise], X_processed)
        np.save(X_grid_processed_file_list[iNoise], X_grid_processed)

# noise_prob_list = [0.1]
noise_prob_list = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
nNoise = len(noise_prob_list)
file_noise_list = [None] * nNoise
for iNoise in range(nNoise):
    file_noise_list[iNoise] = str(int(noise_prob_list[iNoise] * 100)).zfill(2)

X_original_file_list = [None] * nNoise
for iNoise in range(nNoise):
    X_original_file_list[iNoise] = (
          'orbit5k_X_original_' + file_noise_list[iNoise] + '.npy')

X_processed_file_list = [None] * nNoise
for iNoise in range(nNoise):
    X_processed_file_list[iNoise] = (
          'orbit5k_X_processed_' + file_noise_list[iNoise] + '.npy')
X_grid_processed_file_list = [None] * nNoise
for iNoise in range(nNoise):
    X_grid_processed_file_list[iNoise] = (
          'orbit5k_X_grid_processed_' + file_noise_list[iNoise] + '.npy')

# num_orbit_per_param = 100
# num_pts_per_orbit = 100
num_orbit_per_param = 1000
num_pts_per_orbit = 1000

m0 = 0.02
lims = [[0.0125, 0.9875], [0.0125, 0.9875]]
by = 0.025
r = 2.
tseq = np.linspace(0.03, 0.1, 17)
KK = np.array([0, 1, 2])
dimensions = [0, 1]

batch_size = 16

nmax_diag = 69
maxscale = 1.

orbit5k_preprocess(m0=m0, lims=lims, by=by, r=r, tseq=tseq, KK=KK,
      dimensions=dimensions, maxscale=maxscale, nmax_diag=nmax_diag,
      X_original_file_list=X_original_file_list,
      X_processed_file_list=X_processed_file_list,
      X_grid_processed_file_list=X_grid_processed_file_list,
      batch_size=batch_size)