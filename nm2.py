import pymysql
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
from matplotlib import pyplot as plt
#arr = [[17.52582648550422, 10.438711773969066, 13.271180467464076, 10.46329252673364, 19.038131473440362, 28.30941724055796, 19.934134092054265],[33.984554824581714, 26.109782278391375, 33.1794166031442, 26.328045391274305, 18.181451499399063, 32.882685514188175, 52.921305512288725],[19.2942151110119, 19.247243003869404, 21.85886950988086, 24.76564852270178, 17.53262518135833, 22.37802554404656, 33.19470655466019],[27.779961159080116, 36.793861301853056, 29.46535254328379, 13.746380159882095, 18.089901229691666, 13.974012415909764, 17.879058280569478]]
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql="select re from trace where re is not null"
cursor.execute(sql)
arr=[]
for re_list in cursor.fetchall():
    re=re_list[0].split()
    re = list(map(eval, re))
    arr.append(re)
    #print(re)
# X = [[1,2],[3,2],[4,4],[1,2],[1,3]]
Z = linkage(arr, 'ward')
f = fcluster(Z,4,'distance')
#fig = plt.figure(figsize=(5, 3))
dn = dendrogram(Z)
#plt.show()
mergings = linkage(arr)
print(mergings)
