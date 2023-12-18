import matplotlib.pyplot as plt
import numpy as np 


# Graph 01 : Detection Rate vs Percentage of Sybil Nodes
# ========
x_axis_01 = ["5%", "10%", "15%", "20%"] # % of sybil nodes

# M. Ayida et al. [23] 
ayida_01 = [80.65, 90.39, 95.48, 97.49]
# M. S. Kabbur et al. [10] 
kabbur_01 = [85.23, 92.46, 94.93, 95.78]
# J. Pougajendy et al. [17] 
pouga_01 = [88.43, 94.23,96.25,97.85]
# Proposed DDDS 
ddds_01 = [90.98, 96.48, 98.45, 99.07]


# plt.xlabel('Percentage of Sybil Nodes', fontsize=16)
# plt.ylabel('Detection Rate', fontsize=16)
# plt.title('Detection Rate vs Percentage of Sybil Nodes', fontsize=22)

# X_axis = np.arange(len(x_axis_01))
# width = 0.25
# plt.xticks(X_axis + 2 * width, x_axis_01, fontsize=14)
# plt.yticks(fontsize=14)

# plt.bar(X_axis + 0.2, ayida_01, 0.2, label = "M. Ayida et al. [23]")
# plt.bar(X_axis + 0.4, kabbur_01, 0.2, label = "M. S. Kabbur et al. [10] ")
# plt.bar(X_axis + 0.6, pouga_01, 0.2, label = "J. Pougajendy et al. [17] ")
# plt.bar(X_axis + 0.8, ddds_01, 0.2, label = "Proposed DDDS")


# plt.legend()
# plt.show()


# Graph 02 : False Negative Rate vs Percentage of Sybil Nodes
# ========
x_axis_01 = ["5%", "10%", "15%", "20%"] # % of sybil nodes

# M. Ayida et al. [23] 
ayida_02 = [19.5, 9.61, 4.52, 2.2]
# M. S. Kabbur et al. [10] 
kabbur_02 = [14.77, 7.54, 5.07, 4.22]
# J. Pougajendy et al. [17] 
pouga_02 = [11.57, 5.77, 3.75, 2.15]
# Proposed DDDS 
ddds_02 = [9.02, 3.52, 1.55, 0.93]

# plt.xlabel('Percentage of Sybil Nodes', fontsize=16)
# plt.ylabel('False Negative Rate', fontsize=16)
# plt.title('False Negative Rate vs Percentage of Sybil Nodes', fontsize=22)

# X_axis = np.arange(len(x_axis_01))
# width = 0.25
# plt.xticks(X_axis + 2 * width, x_axis_01, fontsize=14)
# plt.yticks(fontsize=14)

# plt.bar(X_axis + 0.2, ayida_02, 0.2, label = "M. Ayida et al. [23]")
# plt.bar(X_axis + 0.4, kabbur_02, 0.2, label = "M. S. Kabbur et al. [10] ")
# plt.bar(X_axis + 0.6, pouga_02, 0.2, label = "J. Pougajendy et al. [17] ")
# plt.bar(X_axis + 0.8, ddds_02, 0.2, label = "Proposed DDDS")


# plt.legend()
# plt.show()



# Graph 03 - Attact Detection Time vs No: of nodes
# ========
x_axis_03 = [100, 200, 300, 400, 500] # No: of Sybil nodes

# M. S. Kabbur et al. [10] 
kabbur_03 = [2, 4, 4.5, 5, 6]
# y. Hao et al. [24] 
hao_03 = [4, 8, 13, 15, 16]
# Proposed DDDS 
ddds_03 = [2, 2.5, 3, 3.5, 4]

# plt.xlabel('Number of Sybil Nodes', fontsize=16)
# plt.ylabel('Attack Detection Time', fontsize=16)
# plt.title('Attack Detection Time vs Number of Sybil Nodes', fontsize=22)

# X_axis = np.arange(len(x_axis_03))
# width = 0.25
# plt.xticks(X_axis + 0.385, x_axis_03, fontsize=14)
# plt.yticks(fontsize=14)

# plt.bar(X_axis + 0.2, kabbur_03, 0.2, label = "M. S. Kabbur et al. [10] ")
# plt.bar(X_axis + 0.4, hao_03, 0.2, label = "y. Hao et al. [24]  ")
# plt.bar(X_axis + 0.6, ddds_03, 0.2, label = "Proposed DDDS")


# plt.legend()
# plt.show()

# Graph 04 - False Positive Rate vs No: of nodes
x_axis_04 = [40, 60, 80, 100, 120] # No: of Sybil nodes

# R.K.P et al. [25] 
rkp_04 = [0.49,0.33,0.24,0.2,0.13]
# J. Pougajendy et al. [17] 
pouga_04 = [0.59,0.4,0.3,0.25, 0.19]
# Proposed DDDS 
ddds_04 = [0.49, 0.33, 0.24, 0.2, 0.13]

plt.xlabel('Number of Sybil Nodes', fontsize=16)
plt.ylabel('False Positive Rate', fontsize=16)
plt.title('False Positive Rate vs Number of Sybil Nodes', fontsize=22)

X_axis = np.arange(len(x_axis_04))
width = 0.25
plt.xticks(X_axis + 0.385, x_axis_04, fontsize=14)
plt.yticks(fontsize=14)

plt.bar(X_axis + 0.2, rkp_04, 0.2, label = "R.K.P et al. [25] ")
plt.bar(X_axis + 0.4, pouga_04, 0.2, label = "J. Pougajendy et al. [17] ")
plt.bar(X_axis + 0.6, ddds_04, 0.2, label = "Proposed DDDS")


plt.legend()
plt.show()
