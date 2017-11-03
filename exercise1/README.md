# How does a program read the cvMat object, in particular, what is the order of the pixel structure?
    There are 2 ways to read cvMat object:
    1. Using macro:CV_MAT_ELSEM(mat,type,row, colume) to read cvMat is easy but takes more time.
    2. Using pointer:
        functions like: cvPtr*D and cvGet*D (cvPtr1D, cvPtr2D, cvPtr3D,cvPtrND)
        build your own pointer(BEST WAY)
