import matplotlib.pyplot as plt

meses = ['Julho', 'Agosto', 'Setembro', 'Novembro']
quantidade_de_produtos = [300, 250, 100, 40]

plt.bar(meses, quantidade_de_produtos, color='black')

plt.xlabel('Mês')
plt.ylabel('Quantitativo do estoque')

plt.title('Acompanhamento do estoque')

plt.show()