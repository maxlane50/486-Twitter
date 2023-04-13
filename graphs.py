import sys
import matplotlib.pyplot as plt
import numpy as np


def main(argv):
    #k value accuracy graph - euclidean
    k = np.array([1,2,3,5,10,20])
    vals = np.array([0.57069,0.51928,0.56298,0.53985,0.52442,0.53728])
    maxvals = np.array([0.59719,0.57025,0.58066,0.5854,0.55893,0.52587])

    #k = 3, n-grams - euclidean
    n_grams = np.array([1,2,3])
    vals2 = np.array([0.56298,0.53728,0.53985])

    # k = 1, n-grams - euclidean
    n_grams3 = np.array([1, 2, 3])
    vals3 = np.array([0.57069, 0.48843, 0.48586])

    # k = 1 n-grams - jaccard
    n_grams = np.array([1, 2, 3])
    jvals = np.array([0.71134, 0.68181, 0.63223])
    #k values accuracy - jaccard
    k = np.array([1, 2, 3, 5, 10, 20])
    jacvals =  np.array([0.71134,0.67835,0.73340,0.69485,0.68041,0.65979])

    # a, b = np.polyfit(n_grams3, vals3, 1)

    plt.xticks(n_grams,n_grams)
    line1 =plt.plot(n_grams,vals3,label="Euclidean")
    line2 = plt.plot(n_grams,jvals,label="Jaccard")
    leg = plt.legend(loc='upper center')
    # plt.plot(n_grams3,a*n_grams3+b)
    plt.title("Nearest Neighbor Accuracy Comparison of Metrics with changing n-grams")

    plt.xlabel("# of n-grams")
    plt.ylabel("Accuracy")
    plt.ylim(0.46,0.75)
    plt.savefig("ngramcompKNN.png")

    # plt.title("Nearest Neighbors Accuracy Values")
    # plt.xlabel("Nearest Neighbor k value")
    # plt.ylabel("Accuracy")
    # plt.ylim(0.4,0.65)
    # plt.savefig("KNN_graph.png")

    #data visuals
    #1. Euclidean Accuracy table
    #2. Jaccard Accuracy Table
    #3. Comparison Table of two metrics
    #4. Comparison of datasets accuracy
    #5. effect of ngrams


if __name__ == '__main__':
    main(sys.argv)