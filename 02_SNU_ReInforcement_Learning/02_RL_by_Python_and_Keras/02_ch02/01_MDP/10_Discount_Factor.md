# DiscoutFactor 
DiscountFactor $`\gamma \in [0, 1]`$ 는 미래의 Reward $`R_k`$ 를 Time k를 고려하여 현재의 Reward 로 감가하는 비율이다.  
DiscountFactor를 사용하면,  
1. Reward 같은 크기일 때 Time이 더 가까운 Reward 를 구별할 수 있다.
2. PresentValue가 작아도 FuctureValue가 큰 State와 연결될 수 있다면, Reward는 커질 수 있다.  

# Discounting and Compounding Reference
```
http://keydifferences.com/difference-between-compounding-and-discounting.html
```

# Discounting and Compounding
Discounting is a way to compute the PresentValue from FuctureValue and DiscoutRate  
FV ---Discounting--> $`PV = function(FV, DF)`$  

Compounding is a way to compute the FuctureValue from PresentValue and CompoundInterestRate
PV ---Compounding--> $`FV = function(PV, CF)`$  

# Discounting and Compounding Example
```{text}
100만원이 있고, 복리로 연이자가 11%일때 1년 뒤 얼마를 갚아야 하는가?
PresentValue = 100만원
CompoundInterestRate = 0.08
Formula : FV = PV * (1+r)^n 
FV = 100만원 * ( 1 + 0.11 )
   = 100만원 * ( 111 / 100 )
   = 111만원
FV = PV * CompoundFactor

같은 복리로 1년 뒤 100만원이 되려면 얼마를 저축해야 하는가?
FuctureValue = 100만원
DiscountRate = 0.08
Formula : PV = FV / (1+r)^n
PV = 100만원 / ( 1 + 0.11 )
   = 100만원 / ( 111 / 100 )
   = 100만원 * ( 100 / 111 )
   = (대략) 90만 1천원
PV = FV * DiscountFactor
```
