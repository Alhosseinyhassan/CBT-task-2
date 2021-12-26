#################################              isotops                   #######################    


hydrogn_isoDist = {"mass": [], "abundance": []}
heliem_isoDist = {"mass": [], "abundance": []}
hydrogen = DataBase.getElement("H")
isotopes = hydrogen.getIsotopeDistribution()
for iso in isotopes.getContainer():
    print("hydrogen isotope:", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
    hydrogn_isoDist["mass"].append(iso.getMZ())
    hydrogn_isoDist["abundance"].append((iso.getIntensity() * 100))
heleim = DataBase.getElement("He")
isotopes = heleim.getIsotopeDistribution()
for iso in isotopes.getContainer():
    print("heleim isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
    heliem_isoDist["mass"].append(iso.getMZ())
    heliem_isoDist["abundance"].append((iso.getIntensity() * 100))
def adjustText(x1, y1, x2, y2):
    if y1 > y2:
        plt.annotate('%0.3f' % (y2), xy=(x2, y2), xytext=(x2 + 0.5, y2 + 9),
                     textcoords='data',
                     arrowprops=dict(arrowstyle="->", color='r', lw=0.5),
                     horizontalalignment='right', verticalalignment='top')
    else:
        plt.annotate('%0.3f' % (y1), xy=(x1, y1), xytext=(x1 + 0.5, y1 + 9),
                     textcoords='data',
                     arrowprops=dict(arrowstyle="->", color='r', lw=0.5),
                     horizontalalignment='right', verticalalignment='top')
                     
                     
#########################       plotDistribution        ###############################

def plotDistribution(distribution):
    n = len(distribution["mass"])
    for i in range(0, n):
        plt.vlines(x=distribution["mass"][i], ymin=0, ymax=distribution["abundance"][i])
        if int(distribution["mass"][i - 1]) == int(distribution["mass"][i]) \
                and i != 0:
            adjustText(distribution["mass"][i - 1], distribution["abundance"][i - 1],
                       distribution["mass"][i], distribution["abundance"][i])
        else:
            plt.text(x=distribution["mass"][i],
                     y=(distribution["abundance"][i] + 2),
                     s='%0.3f' % (distribution["abundance"][i]), va='center',
                     ha='center')
    plt.ylim([0, 110])
    plt.xticks(range(math.ceil(distribution["mass"][0]) - 2,
                     math.ceil(distribution["mass"][-1]) + 2))
                     
                     
########################################################

from urllib.request import urlretrieve
import pyopenms
from pyopenms import ElementDB, EmpiricalFormula, CoarseIsotopePatternGenerator, FineIsotopePatternGenerator, ResidueDB, \
    ModificationsDB, RibonucleotideDB, AASequence, Residue, FASTAEntry, FASTAFile
import math
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 7))
plt.subplot(1, 2, 1)
plt.title("Isotopic distribution of Hydrogen")
plotDistribution(hydrogn_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")


########################################################

plt.subplot(1, 2, 2)
plt.title("Isotopic distribution of Heleim")
plotDistribution(heliem_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")
plt.show()
