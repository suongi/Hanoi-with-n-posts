# breadth first search & depth first search
The codes bfs.py and dfs.py is solution for the Tower of Hanoi with n posts.  
### Note
* Python 3.X is used  
* index of disks is 1, 2, ..., disk  
* index of posts is 0, 1, ..., post-1 for the computer; 1, 2, ..., post to show  
* status is an integer  
$~~~~~~$the post_index of the smallest disk preserved on bit: 0\~bits-1  
$~~~~~~$the post_index of the      disk-2      preserved on bit: bits\~2\*bits-1  
$~~~~~~$the post_index of the  largest disk  preserved on bit: (disk-1)\*bits\~disk\*bits-1  
* Function rightset incorporate every equal status into an only one  
* for example, execute the code bfs.py  
Please input the number of disks: 10  
Please input the number of posts: 5  
at begining: \[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  \[]  \[]  \[]  \[]  
$~~$1from1to5: [10, 9, 8, 7, 6, 5, 4, 3, 2]  []  []  []  [1]    
$~~$2from1to2: [10, 9, 8, 7, 6, 5, 4, 3]  [2]  []  []  [1]      
$~~$3from1to4: [10, 9, 8, 7, 6, 5, 4]  [2]  []  [3]  [1]        
$~~$4from1to3: [10, 9, 8, 7, 6, 5]  [2]  [4]  [3]  [1]          
$~~$3from4to3: [10, 9, 8, 7, 6, 5]  [2]  [4, 3]  []  [1]        
$~~$2from2to3: [10, 9, 8, 7, 6, 5]  []  [4, 3, 2]  []  [1]      
$~~$1from5to3: [10, 9, 8, 7, 6, 5]  []  [4, 3, 2, 1]  []  []    
$~~$5from1to4: [10, 9, 8, 7, 6]  []  [4, 3, 2, 1]  [5]  []      
$~~$6from1to5: [10, 9, 8, 7]  []  [4, 3, 2, 1]  [5]  [6]        
$~~$7from1to2: [10, 9, 8]  [7]  [4, 3, 2, 1]  [5]  [6]          
$~~$6from5to2: [10, 9, 8]  [7, 6]  [4, 3, 2, 1]  [5]  []        
$~~$5from4to2: [10, 9, 8]  [7, 6, 5]  [4, 3, 2, 1]  []  []      
$~~$8from1to5: [10, 9]  [7, 6, 5]  [4, 3, 2, 1]  []  [8]        
$~~$9from1to4: [10]  [7, 6, 5]  [4, 3, 2, 1]  [9]  [8]          
$~~$8from5to4: [10]  [7, 6, 5]  [4, 3, 2, 1]  [9, 8]  []        
$~$10from1to5: []  [7, 6, 5]  [4, 3, 2, 1]  [9, 8]  [10]        
$~~$8from4to1: [8]  [7, 6, 5]  [4, 3, 2, 1]  [9]  [10]          
$~~$9from4to5: [8]  [7, 6, 5]  [4, 3, 2, 1]  []  [10, 9]        
$~~$5from2to4: [8]  [7, 6]  [4, 3, 2, 1]  [5]  [10, 9]          
$~~$8from1to5: []  [7, 6]  [4, 3, 2, 1]  [5]  [10, 9, 8]        
$~~$6from2to1: [6]  [7]  [4, 3, 2, 1]  [5]  [10, 9, 8]          
$~~$7from2to5: [6]  []  [4, 3, 2, 1]  [5]  [10, 9, 8, 7]        
$~~$1from3to2: [6]  [1]  [4, 3, 2]  [5]  [10, 9, 8, 7]          
$~~$6from1to5: []  [1]  [4, 3, 2]  [5]  [10, 9, 8, 7, 6]        
$~~$2from3to1: [2]  [1]  [4, 3]  [5]  [10, 9, 8, 7, 6]          
$~~$5from4to5: [2]  [1]  [4, 3]  []  [10, 9, 8, 7, 6, 5]        
$~~$3from3to4: [2]  [1]  [4]  [3]  [10, 9, 8, 7, 6, 5]          
$~~$4from3to5: [2]  [1]  []  [3]  [10, 9, 8, 7, 6, 5, 4]        
$~~$3from4to5: [2]  [1]  []  []  [10, 9, 8, 7, 6, 5, 4, 3]      
$~~$2from1to5: []  [1]  []  []  [10, 9, 8, 7, 6, 5, 4, 3, 2]    
$~~$1from2to5: []  []  []  []  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  
step= 31  
usetime: 18.879 seconds
