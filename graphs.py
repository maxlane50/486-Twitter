import sys
import matplotlib.pyplot as plt
import numpy as np


def main(argv):
    #k value accuracy graph
    k = np.array([1,2,3,5,10,20])
    vals = np.array([0.57069,0.51928,0.56298,0.53985,0.52442,0.53728])
    maxvals = np.array([0.59719,0.57025,0.58066,0.5854,0.55893,0.52587])

    #k = 3, n-grams
    n_grams = np.array([1,2,3])
    vals2 = np.array([0.56298,0.53728,0.53985])

    # k = 1, n-grams
    n_grams3 = np.array([1, 2, 3])
    vals3 = np.array([0.57069, 0.48843, 0.48586])

    # a, b = np.polyfit(n_grams3, vals3, 1)

    plt.xticks(k,k)
    plt.plot(k,vals)
    plt.plot(k,maxvals)
    # plt.plot(n_grams3,a*n_grams3+b)
    plt.title("Nearest Neighbor Accuracy Comparison of both datasets")

    plt.xlabel("# of nearest neighbors")
    plt.ylabel("Accuracy")
    plt.ylim(0.44,0.60)
    plt.savefig("datasetcomparisonKNN.png")

    # plt.title("Nearest Neighbors Accuracy Values")
    # plt.xlabel("Nearest Neighbor k value")
    # plt.ylabel("Accuracy")
    # plt.ylim(0.4,0.65)
    # plt.savefig("KNN_graph.png")


if __name__ == '__main__':
    main(sys.argv)