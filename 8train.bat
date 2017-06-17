rem opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 132 -numNeg 260 -numStages 10 -w 30 -h 30 -precalcIdxBufSize 4096 -precalcValBufSize 4096

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1500 -numNeg 800 -numStages 20 -w 20 -h 32 -precalcIdxBufSize 4096 -precalcValBufSize 4096