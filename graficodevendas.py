import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [100, 30, 80, 300, 500]

plt.bar(meses, vendas, color='blue')

plt.xlabel('Mês')
plt.ylabel('Vendas(em unidades)')

plt.title('Vendas mensais')

plt.show()