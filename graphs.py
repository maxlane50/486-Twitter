import sys
import matplotlib.pyplot as plt


def main(argv):
    #k value accuracy graph
    k = [1,2,3,5,10,20]
    vals = [0.57069,0.51928,0.56298,0.53985,0.52442,0.53728]

    #k = 3, n-grams
    n_grams = [1,2,3]
    vals2 = [0.56298,0.53728,0.53985]

    # k = 1, n-grams
    n_grams3 = [1, 2, 3]
    vals3 = [0.57069, 0.48843, 0.48586]

    plt.xticks(n_grams3,n_grams3)
    plt.plot(n_grams3,vals3)
    plt.title("Accuracy with n-grams k = 1")

    plt.xlabel("# of n-grams")
    plt.ylabel("Accuracy")
    plt.ylim(0.44,0.60)
    plt.savefig("k3ngrams.png")

    # plt.title("Nearest Neighbors Accuracy Values")
    # plt.xlabel("Nearest Neighbor k value")
    # plt.ylabel("Accuracy")
    # plt.ylim(0.4,0.65)
    # plt.savefig("KNN_graph.png")


if __name__ == '__main__':
    main(sys.argv)