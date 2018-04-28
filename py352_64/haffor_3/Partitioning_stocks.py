import numpy as np

stocks=np.genfromtxt('54_hfc_20170614_comp.csv', delimiter=',')
stocks = stocks.transpose()
print (stocks.shape)

# print (np.correlate(stocks[0], stocks[1]))
# print (np.corrcoef(stocks[0], stocks[1]))


divided=[]
for i in range(10):
    divided.append([stocks[i]])

# centers=[]
# for i in range(10):
#     centers.append(stocks[i])

means=[]
for i in range(10):
    means.append(stocks[i])

tmp_corr=[]
for i in range(10):
    tmp_corr.append(1.)

shuffle=1

for x in range(1990):
    i=x+10


    if i%10==0:
        shuffle*=-1
        already=[]
        print ('--------------------------')

    maxscore=-99999999999999999.
    arg=0
    #각 그룹의 중심점으로부터의 corr을 계산
    for j in range(10):
        tmp_corr[j]=np.correlate(stocks[i], means[j])

    for j in range(10):
        if shuffle==-1:
            setnum=9-j
        else:
            setnum=j
        otherAvg=0.
        #점수 구하는데 필요한 값 계산
        for k in range(10):
            if setnum==k:
                my_corr=tmp_corr[k]
            else:
                otherAvg+=tmp_corr[k]
        # print ('otherAvg shape: {}'.format(otherAvg))
        # print ('otherAvg: {}'.format(otherAvg))
        # print ('my_corr: {}'.format(my_corr))
        # print ('result: {}'.format(my_corr+otherAvg/9.))
        # print ('score: {}'.format(score))
        # print ('boolean: {}'.format(np.any(score<my_corr+otherAvg/9.)))
        #최대 점수 찾기
        if (setnum not in already) and (maxscore<my_corr-otherAvg/9.):
            maxscore=my_corr-otherAvg/9.
            arg=setnum

    print (arg)
    #score가 가장 컸던 그룹에 추가
    divided[arg].append(stocks[i])
    #10개 그룹 중 하나씩에만 들어가게
    already.append(arg)
    #중심점 업데이트
    means[arg]=(means[arg]+stocks[arg])*len(means)/(len(means)+1)

print (len(divided[0]))
print (means[0])

interGroupCorr = 0
for i in range(10):
    for j in range(10):
        interGroupCorr+=np.correlate(means[i],means[j])

print (interGroupCorr)

intraGroupCorr = 0
for i in range(10):
    for j in range(200):
        for k in range(200):
            intraGroupCorr+=np.correlate(divided[i][j], divided[i][k])

print (intraGroupCorr)


# print (np.corrcoef([[1,2,3],[4,1,6]]))