import matplotlib.pyplot as plt

loss = [i for i in range(-4, 5)]

val_loss = [j ** 2 for j in range(-4, 5)]

epohs = range(1, len(loss) + 1)

def show(epohs, y, z, title = "", label1 = '', label2 = '', x = '' , f = ''):

    plt.plot(epohs, y , 'bo', label = label1)
    plt.plot(epohs, z, 'r', label = label2)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(f)
    plt.legend()
    plt.show()

show(epohs, loss, val_loss, )
