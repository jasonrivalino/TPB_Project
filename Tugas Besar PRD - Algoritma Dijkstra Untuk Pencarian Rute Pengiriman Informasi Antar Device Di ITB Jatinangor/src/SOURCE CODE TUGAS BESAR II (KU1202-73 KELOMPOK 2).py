class Graph(): 
    #Fungsi untuk menginisialisasi nilai pertama dari graph
    def __init__(self, nodes):
        #inisialisasi array jarak
        self.distArray = [0 for i in range(nodes)]
        #inisialsasi nodes yang dikunjungi
        self.vistSet = [0 for i in range(nodes)]
        #inisialisasi jumlah dari nodes
        self.V = nodes
        #inisialisasi nilai tak hingga
        self.INF = 1000000
        #inisialisasi graph untuk matriks
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)]

   
    def dijkstra(self, srcNode, Node_tujuan):
        for i in range(self.V):
          #inisialisasi jarak menuju tak hingga terlebih dahulu
          self.distArray[i] = self.INF
          #set node yang dikunjungi dianggap boolean yang bernilai False terlebih dahulu
          self.vistSet[i] = False
        #insialisasi jarak pertama adalah 0
        self.distArray[srcNode] = 0
        for i in range(self.V): 
  
            #Menentukan nilai jarak minimum dari nodes yang belum diproses
		        #u selalu sama dengan Node yang diiterasi pertama kali 
            u = self.minDistance(self.distArray, self.vistSet) 
  
            #Set nilai minimum pada node yang dikunjungi
            self.vistSet[u] = True
  
            #Mengupdate dist[v] jika tidak dalam vistSet, 
		        #ada edge dari u ke v dan total beban dari src ke v melewati u
		        #lebih kecil dari nilai dist[v] yang sekarang
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.vistSet[v] == False and self.distArray[v] > self.distArray[u] + self.graph[u][v]: 
                        self.distArray[v] = self.distArray[u] + self.graph[u][v] 
  
        self.printSolution(self.distArray, srcNode, Node_tujuan)

    #Fungsi untuk menemukan node dengan nilai jarak minimum, 
    #dari himpunan node yang belum termasuk dalam jalur graph 
    def minDistance(self, distArray, vistSet): 
  
        #Inisialisasi nilai minimum untuk node berikutnya
        min = self.INF
  
        #Melakukan pencarian dari node yang belum dikunjungi
        for v in range(self.V): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                min_index = v 
  
        return min_index

    def printSolution(self, distArray, Node_sumber, Node_tujuan): 
        print (Node_sumber, " --> ", Node_tujuan)
        print ("Cost minimum: ", distArray[Node_tujuan])

          
#Menampilkan tabel Dijkstra berdasarkan kondisi pemetaan
ourGraph = Graph(8) 
ourGraph.graph = [[0, 2, 3, 9, 1, 1, 0, 0], 
        [2, 0, 0, 0, 0, 0, 0, 2], 
        [2, 0, 0, 4, 0, 0, 4, 0], 
        [9, 0, 4, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 3, 0], 
        [1, 0, 0, 0, 0, 0, 0, 4], 
        [0, 0, 2, 0, 3, 0, 0, 0],
        [0, 2, 0, 0, 0, 4, 0, 0]
        ]; 


srcNode = int(input("Masukkan node sumber: "))
Node_tujuan = int(input("Masukkan node tujuan: "))
ourGraph.dijkstra(srcNode,Node_tujuan)