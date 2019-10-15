from poker import Card
from poker import hand
from poker import Suit
from poker import Rank
import random
import math
import numpy as np
deck = list(Card)
rank_list=list(Rank)
suit_dict={"suit_c":"@","suit_d":'#',"suit_h":"&","suit_s":"$"}
level_dict={'0':'Garbage','1':'Pair','2':'Two Pair','3':'Continue Pair','4':'Three','5':'Collection','6':'Flush','7':'Gourd','8':'Bomb','9':'Flush_Collection'}
    # & $ # *
    #♥ ♠ ♦ ♣
    # h s d c
def make_suit(Hand):
    color_dict={'suit_c':0,'suit_d':0,'suit_h':0,'suit_s':0}
    for i in range(len(Hand)):
        i_suit=Hand[i].suit
        if(i_suit==Suit(suit_dict['suit_h'])):
            color_dict['suit_h']+=1
        if(i_suit==Suit(suit_dict['suit_s'])):
            color_dict['suit_s']+=1
        if(i_suit==Suit(suit_dict['suit_d'])):
            color_dict['suit_d']+=1
        if(i_suit==Suit(suit_dict['suit_c'])):
            color_dict['suit_c']+=1
    return color_dict
def make_rank(Hand):
    rank_dict={'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
    for i in range(len(Hand)):
        i_rank=Hand[i].rank
        i_=str(i_rank)
        rank_dict[i_]+=1
    return rank_dict

class choose_action_option(object):
    def __init__(self,Hand,color_dict,rank_dict):
        self.color_dict=color_dict
        self.rank_dict=rank_dict
        self.Hand=Hand
        self.Collection_tail=self.Collection()
        self.Flush_dict=self.Flush()
        self.Flush_Collection_tail=self.Flush_Collection()
        self.Three_dict=self.Three()
        self.Gourd_dict=self.Gourd()
        self.Bomb_dict=self.Bomb()
        self.Pair_dict=self.Pair()
        self.Action_dict={'Collection_tail':self.Collection_tail,'Flush_dict':self.Flush_dict,'Flush_Collection_tail':self.Flush_Collection_tail,
                'Three_dict':self.Three_dict,'Gourd_dict':self.Gourd_dict,'Bomb_dict':self.Bomb_dict,'Pair_dict':self.Pair_dict}
    def Collection(self):
        Collec_sum=0
        Collection_tail=[]
        def judge_collection(Collec_sum,tar):
            if(self.rank_dict[tar]!=0):
                Collec_sum+=1
            else:
                Collec_sum=0
            if(Collec_sum>=5):
                Collection_tail.append(tar)
            return Collec_sum
        for i in rank_list:
            Collec_sum=judge_collection(Collec_sum,str(i))
        return Collection_tail
    def Flush(self):
        Flush_dict={'suit_c':[],'suit_d':[],'suit_h':[],'suit_s':[]}
        for c in ['c','d','h','s']:
            color_num=self.color_dict['suit_'+c]
            if(color_num>=5):
                for i in range(len(self.Hand)):
                    if(str(self.Hand[i].suit)==suit_dict['suit_'+c]):
                        Flush_dict['suit_'+c].append(self.Hand[i].rank)
        return Flush_dict
    def Flush_Collection(self):
        Flush_dict=self.Flush()
        Flush_Collection_tail={'suit_c':[],'suit_d':[],'suit_h':[],'suit_s':[]}
        for c in ['c','d','h','s']:
            color_num=self.color_dict['suit_'+c]
            if(color_num>=5):
                item_sum=1
                for item in range(1,color_num):
                    if(Rank.difference(Flush_dict['suit_'+c][item],Flush_dict['suit_'+c][item-1]))==1:
                        item_sum+=1
                    else:
                        item_sum=0
                    if(item_sum>=5):
                        Flush_Collection_tail['suit_'+c].append(Flush_dict['suit_'+c][item])
        return Flush_Collection_tail
    def Three(self):
        Three_dict={'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
        for rank in self.rank_dict:
            rank_num=self.rank_dict[rank]
            if(rank_num>=3):
                Three_dict[rank]+=1
        return Three_dict
    def Gourd(self):
        Three_dict=self.Three()
        Gourd_dict={'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'T':[],'J':[],'Q':[],'K':[],'A':[]}
        for rank in Three_dict:
            if(Three_dict[rank]==1):
                for rank_next in self.rank_dict:
                    rank_next_num=self.rank_dict[rank_next]
                    if(rank_next_num>=2 and rank_next!=rank):
                        Gourd_dict[rank].append(rank_next)
        return Gourd_dict
    def Bomb(self):
        Bomb_dict={'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
        for rank in self.rank_dict:
            rank_num=self.rank_dict[rank]
            if(rank_num==4):
                Bomb_dict[rank]+=1
        return Bomb_dict
    def Pair(self):
        Pair_dict={'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
        for rank in self.rank_dict:
            rank_num=self.rank_dict[rank]
            Pair_dict[rank]=math.floor(rank_num/2)
        return Pair_dict
    def choose(self):
        return self.Action_dict

def choose_step_sb(choose_):
    Collection_tail=choose_['Collection_tail']
    Flush_dict=choose_['Flush_dict']
    Flush_Collection_tail=choose_['Flush_Collection_tail']
    Three_dict=choose_['Three_dict']
    Gourd_dict=choose_['Gourd_dict']
    Bomb_dict=choose_['Bomb_dict']
    Pair_dict=choose_['Pair_dict']
    shape_dict={'0':[0,[]],'1':[0,[]],'2':[0,[]],'3':[0,[]],'4':[0,[]],'5':[0,[]],'6':[0,[]],'7':[0,[]],'8':[0,[]],'9':[0,[]]}
    
    for i in Flush_Collection_tail:
        if(Flush_Collection_tail[i]!=[]):
            for j in Flush_Collection_tail[i]:
                shape_dict[str(9)][0]=1
                shape_dict[str(9)][1].append((str(j),str(i)))
    for i in reversed(rank_list):
        if(Bomb_dict[str(i)]!=0):
            shape_dict[str(8)][0]=1
            shape_dict[str(8)][1].append((str(i),''))
    for i in reversed(rank_list):
        if(Gourd_dict[str(i)]!=[]):
            shape_dict[str(7)][0]=1
            shape_dict[str(7)][1].append((str(i),str(Gourd_dict[str(i)][0])))       
    for i in Flush_dict:
        if(Flush_dict[i]!=[]):
            for j in Flush_dict[i]:
                shape_dict[str(6)][0]=1
                shape_dict[str(6)][1].append((str(j),str(i)))
    if(Collection_tail!=[]):
        shape_dict[str(5)][0]=1
        shape_dict[str(5)][1].append((str(Collection_tail[-1]),''))
    for i in reversed(rank_list):
        if(Three_dict[str(i)]!=0):
            shape_dict[str(4)][0]=1
            shape_dict[str(4)][1].append((str(i),''))           
    pair_num=0
    for i in reversed(rank_list):
        if(Pair_dict[str(i)]!=0):
            if(pair_num==0):
                pair_one=str(i)
                pair_num+=1
            elif(pair_num==1 and (rank_list.index(i)-rank_list.index(Rank(pair_one))==-1)):
                pair_two=str(i)
                shape_dict[str(3)][0]=1
                shape_dict[str(3)][1].append((str(pair_one),str(pair_two)))
    pair_num=0
    for i in reversed(rank_list):
        if(Pair_dict[str(i)]!=0):
            if(pair_num==0):
                pair_one=str(i)
                pair_num+=1
                continue
            elif(pair_num==1):
                pair_two=str(i)
                shape_dict[str(2)][0]=1
                shape_dict[str(2)][1].append((str(pair_one),str(pair_two)))
    for i in reversed(rank_list):
        if(Pair_dict[str(i)]!=0):
            shape_dict[str(1)][0]=1
            shape_dict[str(1)][1].append((str(i),''))
    shape_dict[str(0)][0]=1
    shape_dict[str(0)][1].append(('',''))
    return shape_dict
def action_step_sb(Hand,choose_,shape,rank,suit):
    out=[]
    shape = (int)(shape)
    if(shape==9):
        begin = False
        for i in reversed(Hand):
            if(len(out)==5):
                break
            if(str(i.rank)==rank and str(i.suit)==suit_dict[suit]):
                begin = True
            if(begin == True and str(i.suit)==suit_dict[suit]):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==8):
        for i in reversed(Hand):
            if(str(i.rank)==rank):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==7):
        for i in reversed(Hand):
            if(len(out)==5):
                break
            if(str(i.rank)==rank):
                out.append(i)
                Hand.pop(Hand.index(i))
            if(str(i.rank)==suit):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==6):
        for i in reversed(Hand):
            if(str(i.rank)==rank and str(i.suit)==suit_dict[suit]):
                out.append(i)
                Hand.pop(Hand.index(i))
        for i in reversed(Hand):
            if(len(out)==5):
                break
            if(str(i.suit)==suit_dict[suit]):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==5):
        begin = False
        for i in reversed(Hand):
            if(len(out)==5):
                break
            if(begin == False and str(i.rank)==rank):
                begin = rank
                out.append(i)
                Hand.pop(Hand.index(i))
            if(begin != False and str(out[-1].rank)!= str(i.rank)):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==4):
        for i in reversed(Hand):
            if(str(i.rank)==rank):
                out.append(i)
                Hand.pop(Hand.index(i))
        return Hand,out
    if(shape==3 or shape==2 or shape==1):
        for i in reversed(Hand):
            if(str(i.rank)==rank):
                out.append(i)
                Hand.pop(Hand.index(i))
            if(len(out) == 2):
                break
        for i in reversed(Hand):            
            if(str(i.rank)==suit):
                out.append(i)
                Hand.pop(Hand.index(i))
            if(len(out) ==4):
                break
        return Hand,out
    if(shape==0):
        for i in reversed(Hand):
            if(len(out)==5):
                break
            out.append(i)
            Hand.pop(Hand.index(i))
        return Hand,out
def action_step_add(Hand_three,Hand_two,Hand_rest,shape,rank,suit):
    finish_Hand_three=[]
    finish_Hand_two=[]
    finish_Hand_one=[]

    for i in Hand_three:
        finish_Hand_three.append(i)
    for i in Hand_two:
        finish_Hand_two.append(i)
    if(shape==str(4)):
        for i in reversed(Hand_rest):
            if(str(i.rank)==rank):
                finish_Hand_one.append(i)
                Hand_rest.pop(Hand_rest.index(i))
            if((len(finish_Hand_one))==3):
                break           
                
    if(shape==str(1) or shape==str(2) or shape==str(3)):
        for i in reversed(Hand_rest):
            if(str(i.rank)==rank):
                finish_Hand_one.append(i)
                Hand_rest.pop(Hand_rest.index(i))
            if(len(finish_Hand_one)==2):
                break
        for i in reversed(Hand_rest):
            finish_Hand_one.append(i)
            Hand_rest.pop(Hand_rest.index(i))
            break
    for i in range(5-len(Hand_three)):
        finish_Hand_three.append(Hand_rest[0])
        Hand_rest.pop(0)          
    for i in range(5-len(Hand_two)):
        finish_Hand_two.append(Hand_rest[0])
        Hand_rest.pop(0)
    for i in Hand_rest:
        finish_Hand_one.append(i)
    return finish_Hand_three,finish_Hand_two,finish_Hand_one
def judge_right(res_one,res_two,res_three,shape_1,shape_2,shape_3):
    if (shape_1==str(2) or shape_1==str(3)):
        return False
    if (shape_3==str(0)):
        for i in range(5):
            for j in range(5):
                if(i!=j and res_three[i].rank == res_three[j].rank):
                    return False
    if (shape_2==str(0)):
        for i in range(5):
            for j in range(5):
                if(i!=j and res_two[i].rank == res_two[j].rank):
                    return False
    if (shape_1==str(0)):
        for i in range(3):
            for j in range(3):
                if(i!=j and res_one[i].rank == res_one[j].rank):
                    return False
    if (shape_3==str(1)):
        pair_num = 0
        for i in res_three:
            for j in res_three:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 2):
            return False
    if (shape_2==str(1)):
        pair_num = 0
        for i in res_two:
            for j in res_two:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 2):
            return False
    if (shape_1==str(1)):
        pair_num = 0
        for i in res_one:
            for j in res_one:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 2):
            return False 
    if (shape_3==str(2) or shape_3==str(3)):
        pair_num = 0
        for i in res_three:
            for j in res_three:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 4):
            return False
        pair_one = ''
        pair_two = ''
        for i in res_three:
            for j in res_three:
                if(pair_one == '' and i!=j and i.rank == j.rank):
                    pair_one = i.rank
                elif(pair_one!='' and i!=j and i.rank == j.rank and i.rank!=pair_one):
                    pair_two = i.rank

        if(shape_3 == str(2) and Rank.difference(pair_one,pair_two) == 1):
            return False
    if (shape_2==str(2) or shape_2==str(3)):
        pair_num = 0
        for i in res_two:
            for j in res_two:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 4):
            return False
        pair_one = ''
        pair_two = ''
        for i in res_two:
            for j in res_two:
                if(pair_one == '' and i!=j and i.rank == j.rank):
                    pair_one = i.rank
                elif(pair_one!='' and i!=j and i.rank == j.rank and i.rank!=pair_one):
                    pair_two = i.rank
        if(shape_2 == str(2) and Rank.difference(pair_one,pair_two)==1):
            return False
        
    if (shape_3==str(4)):
        pair_num = 0
        for i in res_three:
            for j in res_three:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 6):
            return False
    if (shape_2==str(4)):
        pair_num = 0
        for i in res_two:
            for j in res_two:
                if(i!=j and i.rank == j.rank):
                    pair_num +=1
        if(pair_num != 6):
            return False
    if (shape_1==str(4)):
        if(res_one[0].rank != res_one[1].rank or res_one[1].rank !=res_one[2].rank or res_one[1].rank!=res_one[0].rank):
            return False 
    flag_reward = Compare_up(3,res_three,res_two,shape_3,shape_2)
    if(flag_reward<0):
        return False
    flag_reward = Compare_gap(res_two,res_one,shape_2,shape_1)
    if(flag_reward<0):
        return False
    return True
def begin_game(myhand_need,Weight,Times,beta,is_Train,Auto,b,real):
    can_weight = np.zeros((5,10,10))
    can_choose = []
    myhand = myhand_need.copy()
    color_dict=make_suit(myhand) #花色
    rank_dict=make_rank(myhand) #数量
    step=choose_action_option(myhand,color_dict,rank_dict)
    choose=step.choose()
    shape_dict_3=choose_step_sb(choose)
    for i in reversed(range(10)):
        if(shape_dict_3[str(i)][0]!=0):
            for j in range(len(shape_dict_3[str(i)][1])):
                
                myhand = myhand_need.copy()
                shape_3,rank,suit= str(i),shape_dict_3[str(i)][1][j][0],shape_dict_3[str(i)][1][j][1]
                myhand_two_need,out_3_need=action_step_sb(myhand,choose,shape_3,rank,suit)
                myhand_two = myhand_two_need.copy()
                color_dict_2=make_suit(myhand_two) #花色
                rank_dict_2=make_rank(myhand_two)
                step=choose_action_option(myhand_two,color_dict_2,rank_dict_2)
                choose_=step.choose()
                shape_dict_2=choose_step_sb(choose_)
                for q in reversed(range(10)):
                    if(shape_dict_2[str(q)][0]!=0):
                        for w in range(len(shape_dict_2[str(q)][1])):
                            myhand_two = myhand_two_need.copy()
                            shape_2,rank,suit= str(q),shape_dict_2[str(q)][1][w][0],shape_dict_2[str(q)][1][w][1]
                            if (shape_2 > shape_3):
                                break
                            myhand_three_need,out_2_need=action_step_sb(myhand_two,choose_,shape_2,rank,suit)
                            myhand_three = myhand_three_need.copy()
                            out_2_need.sort()
                            out_3_need.sort()
                            color_dict_3=make_suit(myhand_three) #花色
                            rank_dict_3=make_rank(myhand_three) #数量
                            step=choose_action_option(myhand_three,color_dict_3,rank_dict_3)
                            choose_2=step.choose()
                            shape_dict_1=choose_step_sb(choose_2)
                            for e in reversed(range(5)):
                                if(shape_dict_1[str(e)][0]!=0):
                                    for r in range(len(shape_dict_1[str(e)][1])):
                                        myhand_three = myhand_three_need.copy()
                                        out_3 = out_3_need.copy()
                                        out_2 = out_2_need.copy()
                                        shape_1,rank,suit= str(e),shape_dict_1[str(e)][1][r][0],shape_dict_1[str(e)][1][r][1]
                                        if (shape_1>shape_2):
                                            break
                                        res_three,res_two,res_one=action_step_add(out_3,out_2,myhand_three,shape_1,rank,suit)
                                        res_three.sort()
                                        res_two.sort()
                                        res_one.sort()
                                        #if (can_weight[int(shape_1)][int(shape_2)][int(shape_3)] == 0 and )
                                        if(judge_right(res_one,res_two,res_three,shape_1,shape_2,shape_3)==True):
                                            can_weight[int(shape_1)][int(shape_2)][int(shape_3)] = 1
                                            can_choose.append(([int(shape_1),int(shape_2),int(shape_3)],res_one,res_two,res_three))
                                            if(real == False):
                                                if(Auto == True):
                                                    if(is_Train == False):
                                                        finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                                                        return finish_hand
                                                    if(is_Train == True):
                                                        finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                                                        reward = 0
                                                        reward += Compare_Combo(finish_hand,b[0])
                                                        reward += Compare_Combo(finish_hand,b[1])
                                                        reward += Compare_Combo(finish_hand,b[2])
                                                        reward = reward * ((beta)/math.sqrt(Times[int(shape_1)][int(shape_2)][int(shape_3)]))
                                                        Times[int(shape_1)][int(shape_2)][int(shape_3)]+=1
                                                        Weight[int(shape_1)][int(shape_2)][int(shape_3)]+=(int(reward)/1000)
                                                if(Auto == False):
                                                    print("第三墩：",shape_3)
                                                    print(res_three)
                                                    print("第二墩：",shape_2)
                                                    print(res_two)
                                                    print("第一墩：",shape_1)
                                                    print(res_one)
                                                    print("-------------------------------")
                                                    if(is_Train == False):
                                                        finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                                                        return finish_hand
                                                    if(is_Train == True):
                                                        finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                                                        reward = input()
                                                        print("-------------------------------")
                                                        if(reward == 'shabi'):
                                                            continue
                                                        if(reward == 'gundan'):
                                                            return Weight
                                                        Weight[int(shape_1)][int(shape_2)][int(shape_3)]+=(int(reward)/10000)
                                            else:
                                                continue
    if(real == True):
        mymax = -100000
        my_one = ''
        my_two = ''
        my_three = ''
        for i in range(5):
            for j in range(10):
                for m in range(10):
                    if(can_weight[i][j][m]==1 and Weight[i][j][m]>mymax):
                        mymax = Weight[i][j][m]
                        if(Auto==False):
                            print(Weight[i][j][m],i,j,m)
                        my_one = i
                        my_two = j
                        my_three = m
        my = [my_one,my_two,my_three]
        res_one=''
        res_two=''
        res_three=''
        for item in can_choose:
            tar_reward=0
            flagres_one=''
            flagres_two=''
            flagres_three=''
            if(item[0]==my):
                if(res_one==''):
                    res_one = item[1]
                    res_two = item[2]
                    res_three = item[3]
                    shape_1 = my_one
                    shape_2 = my_two
                    shape_3 = my_three
                elif(res_one!=''):
                    if(item[1]!=res_one):
                        flagres_one = item[1]
                    if(item[2]!=res_two):
                        flagres_two = item[2]
                    if(item[3]!=res_three):
                        flagres_three = item[3]
                    if(flagres_three != ''):
                        tar_reward+=Compare_up(3,flagres_three,res_three,shape_3,shape_3)
                    if(flagres_two != ''):
                        tar_reward+=Compare_up(2,flagres_two,res_two,shape_2,shape_2)
                    if(flagres_one != ''):
                        tar_reward+=Compare_down(flagres_one,res_one,shape_1,shape_2)
                    if(tar_reward>0):
                        if(flagres_one != ''):
                            res_one = flagres_one
                        if(flagres_two != ''):
                            res_two = flagres_two
                        if(flagres_three != ''):
                            res_three = flagres_three
        if(Auto== True):
            
            if(is_Train == False):
                finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                return finish_hand
            if(is_Train == True):
                finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
                reward = 0
                reward += Compare_Combo(finish_hand,b[0])
                reward += Compare_Combo(finish_hand,b[1])
                reward += Compare_Combo(finish_hand,b[2])
                reward = reward * ((beta)/math.sqrt(Times[int(shape_1)][int(shape_2)][int(shape_3)]))
                Times[int(shape_1)][int(shape_2)][int(shape_3)]+=1
                Weight[int(shape_1)][int(shape_2)][int(shape_3)]+=(int(reward)/10)
                print("第三墩：",shape_3)
                print(res_three)
                print("第二墩：",shape_2)
                print(res_two)
                print("第一墩：",shape_1)
                print(res_one)
                print("-------------------------------")
        else:
            print("第三墩：",shape_3)
            print(res_three)
            print("第二墩：",shape_2)
            print(res_two)
            print("第一墩：",shape_1)
            print(res_one)
            print("-------------------------------")
            finish_hand={"level_1":(res_one,shape_1),"level_2":(res_two,shape_2),"level_3":(res_three,shape_3)}
            return finish_hand
    return Weight,Times

def Compare_gap(res_1,res_2,shape_1,shape_2):
    res_1.sort()
    res_2.sort()
    shape_1 = (int)(shape_1)
    shape_2 = (int)(shape_2)
    if(shape_1>shape_2):
        return 1
    elif (shape_1<shape_2):
        return -1
    else:
        if(shape_1 == 0):
            for i in reversed(range(3)):
                if(res_1[i+2].rank>res_2[i].rank):
                    return 1
                elif(res_1[i+2].rank<res_2[i].rank):
                    return -1
                else:
                    continue
            for i in reversed(range(3)):
                if(res_1[i+2]>res_2[i]):
                    return 1
                elif(res_1[i+2]<res_2[i]):
                    return -1
            return 0
        if(shape_1 == 1 or shape_1 == 2 or shape_1 == 3):
            pair_one =''
            rest_one = ''
            pair_another_one = ''
            pair_two =''
            rest_two = ''
            pair_another_two = ''
            for i in range(4):
                if (res_1[i].rank == res_1[i+1].rank):
                    pair_one = res_1[i].rank
                    break
            for i in range(4):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank!=pair_one):
                    pair_another_one = res_1[i].rank
                    break
            for i in reversed(range(5)):
                if(res_1[i].rank!=pair_one and res_1[i].rank!=pair_another_one):
                    rest_one = res_1[i]
                    break
            for i in range(2):
                if (res_2[i].rank == res_2[i+1].rank):
                    pair_two = res_2[i].rank
            for i in range(3):
                if(res_2[i].rank!=pair_two):
                    rest_two = res_2[i]
            if(pair_another_one == ''):
                if(pair_one>pair_two):
                    return 1
                elif(pair_one<pair_two):
                    return -1
                else:
                    if(rest_one>rest_two):
                        return 1
                    elif(rest_one<rest_two):
                        return -1
                    else:
                        return 0
            else:
                return 1
            return 0
        if(shape_1==4):
            three_one = ''
            rest_one = ''
            three_two = ''
            rest_two = ''
            for i in range(3):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank == res_1[i+2].rank):
                    three_one = res_1[i].rank
                    break
            three_two = res_2[0].rank
            for i in range(5):
                if (res_1[i].rank == three_one):
                    rest_one = res_1[i].rank
                    break
            if(three_one>three_two):
                    return 1
            elif(three_one<three_two):
                    return -1
            return 0
def Compare_down(res_1,res_2,shape_1,shape_2):
    res_1.sort()
    res_2.sort()
    shape_1 = (int)(shape_1)
    shape_2 = (int)(shape_2)
    if(shape_1>shape_2):
        return 1
    elif (shape_1<shape_2):
        return -1
    else:
        if(shape_1 == 0):
            for i in reversed(range(3)):
                if(res_1[i].rank>res_2[i].rank):
                    return 1
                elif(res_1[i].rank<res_2[i].rank):
                    return -1
            for i in reversed(range(3)):
                if(res_1[i]>res_2[i]):
                    return 1
                elif(res_1[i]<res_2[i]):
                    return -1
            return 0
        if(shape_1 == 1 or shape_1 == 2 or shape_1 == 3):
            pair_one =''
            rest_one = ''
            pair_two =''
            rest_two = ''
            for i in range(2):
                if (res_1[i].rank == res_1[i+1].rank):
                    pair_one = res_1[i].rank
            for i in range(3):
                if(res_1[i].rank!=pair_one):
                    rest_one = res_1[i]
            for i in range(2):
                if (res_2[i].rank == res_2[i+1].rank):
                    pair_two = res_2[i].rank
            for i in range(3):
                if(res_2[i].rank!=pair_two):
                    rest_two = res_2[i]
            if(pair_one>pair_two):
                return 1
            elif(pair_one<pair_two):
                return -1
            else:
                if(rest_one>rest_two):
                    return 1
                elif(rest_one<rest_two):
                    return -1
            return 0
        if(shape_1==4):
            if(res_1[0]>res_2[0]):
                return 1
            else:
                return -1
            return 0
def Compare_up(level,res_1,res_2,shape_1,shape_2):
    res_1.sort()
    res_2.sort()
    shape_1 = (int)(shape_1)
    shape_2 = (int)(shape_2)
    if(shape_1>shape_2):
        if(level == 2):
            if(shape_1 == 7):
                return 2
            if(shape_1 == 8):
                return 8
            if(shape_1 == 9):
                return 10
            else:
                return 1
        else:
            if(shape_1 == 8):
                return 4
            if(shape_1 == 9):
                return 5
            else:
                return 1
    elif (shape_1<shape_2):
        if(level == 2):
            if(shape_2 == 7):
                return -2
            if(shape_2 == 8):
                return -8
            if(shape_2 == 9):
                return -10
            else:
                return -1
        else:
            if(shape_2 == 8):
                return -4
            if(shape_2 == 9):
                return -5
            else:
                return -1
    else:
        if(shape_1 == 0):
            for i in reversed(range(5)):
                if(res_1[i].rank>res_2[i].rank):
                    return 1
                elif(res_1[i].rank<res_2[i].rank):
                    return -1
                else:
                    continue
            for i in reversed(range(5)):
                if(res_1[i]>res_2[i]):
                    return 1
                elif(res_1[i]<res_2[i]):
                    return -1
            return 0
        if(shape_1 == 1 or shape_1 == 2 or shape_1 == 3):
            pair_one =''
            rest_one = ''
            pair_another_one = ''
            pair_two =''
            rest_two = ''
            pair_another_two = ''
            for i in range(4):
                if (res_1[i].rank == res_1[i+1].rank):
                    pair_one = res_1[i].rank
                    break
            for i in range(4):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank!=pair_one):
                    pair_another_one = res_1[i].rank
                    break
            for i in reversed(range(5)):
                if(res_1[i].rank!=pair_one and res_1[i].rank!=pair_another_one):
                    rest_one = res_1[i]
                    break
            for i in range(4):
                if (res_2[i].rank == res_2[i+1].rank):
                    pair_two = res_2[i].rank
                    break
            for i in range(4):
                if (res_2[i].rank == res_2[i+1].rank and res_2[i].rank!=pair_two):
                    pair_another_two = res_2[i].rank
                    break
            for i in reversed(range(5)):
                if(res_2[i].rank!=pair_two and res_2[i].rank!=pair_another_two):
                    rest_two = res_2[i]
                    break
            if(pair_another_one == '' and pair_another_two == ''):
                if(pair_one>pair_two):
                    return 1
                elif(pair_one<pair_two):
                    return -1
                else:
                    if(rest_one>rest_two):
                        return 1
                    elif(rest_one<rest_two):
                        return -1
                    else:
                        return 0
            elif(pair_another_one != '' and pair_another_two==''):
                return 1
            else:
                if(pair_another_one>pair_another_two):
                    return 1
                elif(pair_another_one<pair_another_two):
                    return -1
                else:
                    if(pair_one>pair_two):
                        return 1
                    elif(pair_one<pair_two):
                        return -1
                    else:
                        if(rest_one>rest_two):
                            return 1
                        elif(rest_one<rest_two):
                            return -1
            return 0
        if(shape_1==4):
            three_one = ''
            rest_one = ''
            three_two = ''
            rest_two = ''
            for i in range(3):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank == res_1[i+2].rank):
                    three_one = res_1[i].rank
                    break
            for i in range(3):
                if (res_2[i].rank == res_2[i+1].rank and res_2[i].rank == res_2[i+2].rank):
                    three_two = res_2[i].rank
                    break
            for i in range(5):
                if (res_1[i].rank == three_one):
                    rest_one = res_1[i].rank
                    break
            for i in range(5):
                if (res_2[i].rank == three_two):
                    rest_two = res_2[i].rank
                    break
            if(three_one>three_two):
                    return 1
            elif(three_one<three_two):
                    return -1
            else:
                if(rest_one>rest_two):
                    return 1
                elif(rest_one<rest_two):
                    return -1
                else:
                    return 0
            return 0
        if(shape_1==5):
            if(res_1[-1]>res_2[-1]):
                return 1
            elif(res_1[-1]<res_2[-1]):
                return -1
            return 0
        if(shape_1==6):
            for i in reversed(range(5)):
                if(res_1[i].rank>res_2[i].rank):
                    return 1
                elif(res_1[i].rank<res_2[i].rank):
                    return -1
            if(res_1[-1]>res_2[-1]):
                return 1
            elif(res_1[-1]<res_2[-1]):
                return -1
            return 0
        if(shape_1==7):
            three_one = ''
            three_two = ''
            for i in range(3):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank == res_1[i+2].rank):
                    three_one = res_1[i].rank
                    break
            for i in range(3):
                if (res_2[i].rank == res_2[i+1].rank and res_2[i].rank == res_2[i+2].rank):
                    three_two = res_2[i].rank
                    break
            if(three_one>three_two):
                return 1
            elif(three_one<three_two):
                return -1
            return 0
        if(shape_1==8):
            three_one = ''
            rest_one = ''
            three_two = ''
            rest_two = ''
            for i in range(3):
                if (res_1[i].rank == res_1[i+1].rank and res_1[i].rank == res_1[i+2].rank):
                    three_one = res_1[i].rank
                    break
            for i in range(3):
                if (res_2[i].rank == res_2[i+1].rank and res_2[i].rank == res_2[i+2].rank):
                    three_two = res_2[i].rank
                    break
            for i in range(5):
                if (res_1[i].rank == three_one):
                    rest_one = res_1[i].rank
                    break
            for i in range(5):
                if (res_2[i].rank == three_two):
                    rest_two = res_2[i].rank
                    break
            if(three_one>three_two):
                if(level==2):
                    return 8
                else:
                    return 4
            elif(three_one<three_two):
                if(level==2):
                    return -8
                else:
                    return -4
            else:
                if(rest_one>rest_two):
                    return 1
                elif(rest_one<rest_two):
                    return -1
            return 0
        if(shape_1==9):
            if(res_1[4]>res_2[4]):
                if(level==2):
                      return 10
                else:
                    return 5
            elif(res_1[4]<res_2[4]):
                if(level==2):
                    return -10
                else:
                    return -5
            return 0
def Compare_Combo(finish_hand_1,finish_hand_2):
    
    myreward = 0
    res_one_1,shape_one_1 = finish_hand_1['level_1'][0],finish_hand_1['level_1'][1]
    res_two_1,shape_two_1 = finish_hand_1['level_2'][0],finish_hand_1['level_2'][1]
    res_three_1,shape_three_1 = finish_hand_1['level_3'][0],finish_hand_1['level_3'][1]
    
    res_one_2,shape_one_2 = finish_hand_2['level_1'][0],finish_hand_2['level_1'][1]
    res_two_2,shape_two_2 = finish_hand_2['level_2'][0],finish_hand_2['level_2'][1]
    res_three_2,shape_three_2 = finish_hand_2['level_3'][0],finish_hand_2['level_3'][1]
    myreward += Compare_down(res_one_1,res_one_2,shape_one_1,shape_one_2)
    myreward += Compare_up(2,res_two_1,res_two_2,shape_two_1,shape_two_2)
    myreward += Compare_up(3,res_three_1,res_three_2,shape_three_1,shape_three_2)
    return myreward