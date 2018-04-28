import numpy as np
import random
import csv


stocks=np.genfromtxt('54_hfc_20170614_comp.csv', delimiter=',')
stocks = stocks.transpose()
# stocks = stocks.tolist()
#
# for i in range(2000):
#     # stocks[i] = stocks[i].tolist()
#     stocks[i].append(i) #추후에 shuffle시 index구분을 위해
#
# stocks = np.asarray(stocks)
# print (stocks.shape)
# print (stocks[1][-1])

print (stocks.shape)


LR=1/2000.

divided=[]
for i in range(10):
    divided.append([])
argDivided=[]

selected=random.sample(range(2000), 10)
print (selected)

means=[]
for i in selected:
    means.append(stocks[i]) #첫 판에는 평균값 넣을게 없으니 그냥 앞에서 10개 뽑아서 넣기

num_means=[]
for i in range(10):
    num_means.append(0)

tmp_corr=[]
for i in range(10):
    tmp_corr.append(1.)

shuffle=1

for i in range(2000):

    if i%10==0:
        shuffle*=-1
        already=[]
        # print ('--------------------------')

    maxscore=-99999999999999999.
    arg=0
    #각 그룹의 중심점으로부터의 corr을 계산
    for j in range(10):
        tmp_corr[j]=np.corrcoef(stocks[i], means[j])[0][1]

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
        #최대 점수 찾기
        if (setnum not in already) and (maxscore<my_corr-otherAvg/9.):
            maxscore=my_corr-otherAvg/9.
            arg=setnum

    # print (arg)
    #score가 가장 컸던 그룹에 추가
    divided[arg].append(stocks[i])
    argDivided.append([i, arg])

    #10개 그룹 중 하나씩에만 들어가게
    already.append(arg)

    #중심점 평균 업데이트
    num_means[arg]+=1
    means[arg]=(means[arg]+stocks[i])*num_means[arg]/(num_means[arg]+1)

# print (len(divided[0]))
# print (means[0])
print(means)

interGroupCorr=0
interGroupCorrArr = np.corrcoef(means)
for i in range(10):
    for j in range(10):
        interGroupCorr+=interGroupCorrArr[i][j]

print (interGroupCorr)

intraGroupCorr = 0
for i in range(10):
    intraGroupCorrArr=np.corrcoef(divided[i])
    for j in range(200):
        for k in range(200):
            intraGroupCorr+=intraGroupCorrArr[j][k]

print (intraGroupCorr)
print (num_means)
before = intraGroupCorr/interGroupCorr
best=before


iteration=1
stopLoss=0
notEnough=True
while(notEnough):
    argStocks=random.sample(range(2000), 2000)
    print (argStocks)
    myRange=[]
    # for i in range(startPoint, 2000):
    #     myRange.append(i)
    # for i in range(0, startPoint):
    #     myRange.append(i)
    # np.random.shuffle(stocks)   #이렇게 해주지 않으면 stocks의 앞쪽 데이터들에만 민감하게 학습됩니다.
    print (stocks.shape)

    print ('----------------------------------------------------')
    divided = []
    for i in range(10):
        divided.append([])
    argDivided = []

    num_means = []
    for i in range(10):
        num_means.append(0)
    iteration=0
    for i in argStocks:
        if iteration%10==0:
            shuffle*=-1
            already=[]
            # print ('--------------------------')
        iteration+=1

        maxscore=-99999999999999999.
        arg=0
        #각 그룹의 중심점으로부터의 corr을 계산
        for j in range(10):
            tmp_corr[j]=np.corrcoef(stocks[i], means[j])[0][1]

        for j in range(10): #각각의 집합에 들어가기로 선택한 것을 가정하고 어느 집합에 들어가는게 my_corr-otherAvg/9. 가 최대가 되는지 구해서 거기로 들어가는 방식.
            #번갈아가며 앞 혹은 뒤에서부터
            if shuffle==-1:
                setnum=9-j
            else:
                setnum=j
            otherAvg=0. #10개의 평균 집합 중 자기가 선택하지 않은 집합들의 벡터와의 corr의 합
            #점수 구하는데 필요한 값 계산
            for k in range(10):
                if setnum==k:
                    my_corr=tmp_corr[k] #10개의 평균 집합 중 자신이 선택한 집합의 벡터와의 corr
                else:
                    otherAvg+=tmp_corr[k]
            #최대 점수 찾기
            if (setnum not in already) and (maxscore<my_corr-otherAvg/9.):  #200개씩 균등하게 들어가야 하니까, 앞에 벡터가 먼저 들어간 집합에는 들어가지 않는다.
                maxscore=my_corr-otherAvg/9.
                arg=setnum  #지금까지의 score보다 좋았으면 그 argument를 기록

        # print (arg)
        # score가 가장 컸던 그룹에 추가
        divided[arg].append(stocks[i])
        argDivided.append([i, arg])

        # 10개 그룹 중 하나씩에만 들어가게
        already.append(arg)

        # 중심점 평균 업데이트
        num_means[arg] += 1
        means[arg] = (means[arg] + stocks[i]) * num_means[arg] / (num_means[arg] + 1)
        # means[arg] = (means[arg]+LR*stocks[i])/(1+LR)

    #결과들 출력

    # print(means)
    print (argDivided)
    interGroupCorr = 0
    interGroupCorrArr = np.corrcoef(means)
    for i in range(10):
        for j in range(10):
            interGroupCorr += interGroupCorrArr[i][j]

    # print(interGroupCorr)

    intraGroupCorr = 0
    for i in range(10):
        intraGroupCorrArr = np.corrcoef(divided[i])
        for j in range(200):
            for k in range(200):
                intraGroupCorr += intraGroupCorrArr[j][k]

    # print(intraGroupCorr)
    now = intraGroupCorr/interGroupCorr
    print('intra group correlation / inter group correlation = {}'.format(intraGroupCorr/interGroupCorr))    #이게 증가할수록 성공적으로 분류되고 있는 것이다.

    if now<before:  #상황이 안 좋아지고 있으면
        stopLoss+=1
    else:
        if now>=best:
            best=now
            # best_divided=divided
            best_argDIvided=argDivided
        stopLoss=0

    if stopLoss==6: # n번 연속 결과가 악화되면
        # print (best_divided)
        # with open('result.csv', 'w', newline='') as myfile:
        #     wr = csv.writer(myfile)
        #     wr.writerow(best_argDIvided)
        with open('result.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            for i in range(2000):
                wr.writerow(best_argDIvided[i])

        notEnough=False

    before=now










