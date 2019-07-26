
import matplotlib.pyplot as plt

loss = [i for i in range(-4,5)]

val_loss =[j**2 for j in range(-4,5)]

epohs = range(1, len(loss)+1)

plt.plot(epohs, loss, 'bo' , label = 'Training loss')
plt.plot(epohs,val_loss,'b', label = 'Validation loss')
plt.title('training and validation loss')
plt.xlabel('Epohs')
plt.ylabel('Loss')
plt.legend()
plt.show()
