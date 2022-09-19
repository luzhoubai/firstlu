
import matplotlib.pyplot as plt
import writedoc.wr as wr




def printhello():
    print("hello")


def read1txt():
    with open('1.txt', encoding='utf-8') as file1:
    # contents = file1.read()
    # print(contents)
    # for line in file1:
    #     print('line:',line)
        contents = file1.readlines()

    print('1:',contents)

    newList=[]

    for content in contents:
        newContent = content.replace('\n','')
        money = newContent.split('：')[-1]    # get last element
        newList.append(int(money))

    print('2:',newList)

    x=[1,2,3,4,5,6]
    y = newList
    plot1 = plt.plot(x,y,'r')
    plt.xlabel('month')
    plt.ylabel('money')
    plt.savefig('销售额.png')
    #plt.legend()
    #plt.show()

    sum0 =0
    for money in newList:
        sum0 += money
    average = sum0/len(newList)
    print('average1:',average)

    average2 = sum(newList) / len(newList)
    print("average2:",average2)


printhello()
read1txt()
wr.w()