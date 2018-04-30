```{text}
ref : http://keydifferences.com/difference-between-compounding-and-discounting.html

100만원이 있고, 복리로 연이자가 11%일때 1년 뒤 얼마를 갚아야 하는가?
PresentValue = 100만원
CompoundInterestRate = 0.08
Formula : FV = PV * (1+r)^n 
FV = 100만원 * ( 1 + 0.11 )
   = 100만원 * ( 111 / 100 )
   = 111만원

FV = PV * CompoundFactor

같은 복리로 1년 뒤 100만원이 되려면 얼마를 저축해야 하는가?
PresentValue = 100만원
DiscountRate = 0.08
Formula : PV = FV / (1+r)^n
PV = 100만원 / ( 1 + 0.11 )
   = 100만원 / ( 111 / 100 )
   = 100만원 * ( 100 / 111 )
   = (대략) 90만 1천원

PV = FV * DiscountFactor

실생활 관전에서
은행에서 돈을 빌렸다고 했을때
복리로 연이자 11%라고 하자. 시간이 지남에 따라 돈은 급력히 불려진다.
복리로 연이자 1 %라고 하자. 시간이 지남에 따라 돈은 상대적으로 덜 불려진다.

DeepLearning Modeling관점에서 
DiscountFactor = 0.9  를 쓰는데 Compound interest rate = 0.11 의 역수이다. 즉 시간이 지남에 따라 보상이 급격히 불려진다.
DiscountFactor = 0.99 를 쓰는데 Compound interest rate = 0.1  의 역수이다. 즉 시간이 지남에 따라 보상이 덜 불려진다.

Programing 구현관점에서
PV <-> FV
PV --> FV : f1(PV, CF) = FV
PV <-- FV : f2(FV, DF) = PV
```
