# 좋은 Policy 를 선택하기
```
(DisCountFactor를 고려하기 전에) 특정 state에서만 Reward가 큰 Action a를 제안하는 Policy보다는
모든 state에서 크지는 않아도 Reward가 꾸준히 상승하는 Action a를 제안하는 Policy가 좋다.
예를 들어, 토끼와 거북이의 경우 거북이 같은 Policy가 좋다.
```

# Turtle and Rabbit Policy Example
```{bash}
$ python 11_turtle_rabbit_equation_plot.py
```

# Cumulative Sum + DisCountFactor = Return
좋은 Policy를 선택하기 위해서  
Return이라는 개념을 아래와 같이 정의한다.  
  
Agent가 어떤 Policy p를 따른다고 할때,  
Time t이후 받게되는 모든 Reward에 DisCountFactor $`\gamma`$를 적용한 CumulativeSum을 Return 이라고 한다.  
  
$` Return \space G_t = R_{t+1} + \gamma \cdot R_{t+2} + \gamma^2 \cdot R_{t+3} + ... + \gamma^{k-1} \cdot R_{t+k} + \mathellipsis `$  
$` \kern4em\:\:\, = \lim \limits_{k \rightarrow \infty} \displaystyle\sum_{i=1}^k \gamma^{i-1} \cdot R_{t+i} `$  
$` \kern4em\:\:\, = \displaystyle\sum_{i=1}^\infty \gamma^{i-1} \cdot R_{t+i} `$  
$` \kern4em\:\:\, \approx \displaystyle\sum_{i=1}^{K-t} \gamma^{i-1} \cdot R_{t+i} \space ( if \space \exists K \in \mathbb{N} = Episode \space consists \space of \space K \space times \space ) `$
