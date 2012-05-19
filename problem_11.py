f = open('20x20.txt', 'rU')
x = []
max_prod = 0

for m in xrange(20):                # Create a list of lists with x
    x.append([])
    for n in xrange(20):
        x[m].append(int(f.read(3)))
                          
f.close()

        # Check horizontally for max_prod...
        
for i in range(len(x)):                 
    for j in range(len(x[i])-3):       
        horiz = (x[i][j])*(x[i][j+1])*(x[i][j+2])*(x[i][j+3])
        if horiz > max_prod:
            max_prod = horiz

        # Check vertically for max_prod...
    
for i in range(len(x[i])-3):        
    for j in range(len(x)):
        vert = (x[i][j])*(x[i+1][j])*(x[i+2][j])*(x[i+3][j])
        if vert > max_prod:
            max_prod = vert

        # Check diagonally right for max_prod...
       
for i in range(len(x[i])-3):        
    for j in range(len(x[i])-3):
        diag_right = (x[i][j])*(x[i+1][j+1])*(x[i+2][j+2])*(x[i+3][j+3])
        if diag_right > max_prod:
            max_prod = diag_right

        # Check diagonally left for max_prod...
            
for i in range(3,len(x)):           
    for j in range(len(x[i])-3):
        diag_left = (x[i][j])*(x[i-1][j+1])*(x[i-2][j+2])*(x[i-3][j+3])
        if diag_left > max_prod:
            max_prod = diag_left

print "Max product = %s" % max_prod
