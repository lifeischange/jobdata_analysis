# encoding:utf-8

import matplotlib.pyplot as plt

def city_mean(data):
    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    data.boxplot(column="Citys",by="Salary")
    plt.show()
