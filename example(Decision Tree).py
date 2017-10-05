import trees
import treePlotter
fr = open('lenses.txt')
lenses=[line.strip().split('\t') for line in fr.readlines()]
lensesLabels=['age','prescript','agtigmatic','tearRate']
lenseTree = trees.createTree(lenses,lensesLabels)
lenseTree
treePlotter.createPlot(lenseTree)
