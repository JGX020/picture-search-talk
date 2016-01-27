from PIL import Image
 
def sketch(img, threshold):
    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100
     
    width, height = img.size
    img = img.convert('L') # convert to grayscale mode
    pix = img.load() # get pixel matrix
 
    for w in xrange(width):
        for h in xrange(height):
            if w == width-1 or h == height-1:
                continue
             
            src = pix[w, h]
            dst = pix[w+1, h+1]
 
            diff = abs(src - dst)
 
            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255
 
    return img
if __name__ == "__main__":
    import sys, os
 
    path = os.path.dirname(__file__) + os.sep.join(['', 'uploads', '4.jpg'])
    threshold = 15
     
    if len(sys.argv) == 2:
        try:
            threshold = int(sys.argv[1])
        except ValueError:
            path  = sys.argv[1]
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        threshold = int(sys.argv[2])
 
    img = Image.open(path)
    img = sketch(img, threshold)
    img.save(os.path.splitext(path)[0]+'.sketch.jpg', 'JPEG')