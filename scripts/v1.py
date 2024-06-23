import seaborn as sns 
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
iris.head(2)

sns.pairplot(iris, hue='species', palette='Dark2')
plt.show()

# Just the Grid
sns.PairGrid(iris)

g = sns.PairGrid(iris)
g.map(plt.scatter)