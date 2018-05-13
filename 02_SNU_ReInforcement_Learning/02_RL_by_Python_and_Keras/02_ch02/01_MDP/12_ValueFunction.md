# (state) ValueFunction 의 정의
Time t에서 State s에 대한 DisCountFactor를 반영한 미래 Reward의 총합을 ValueFunction이라고 한다.  
Time t에서 State s에 대한 Return을 ValueFunction이라고 한다.  
action ValueFunction = QFunction과 구분하기 위해서 state ValueFunction으로 사용하기도 한다.  
$` ValueFunction(s) = E[G_t | S_t = s] `$   
$` \kern6em\,\: v(s) = E[G_t | S_t = s] `$  

# ValueFunction을 Recursive하게 정리하기
$` v(S_t) = E[G_t \enspace | \enspace S_t = s] `$  
$` \kern2em\: = E[ \displaystyle\sum_{i=1}^\infty \gamma^{i-1} \cdot R_{t+i} \enspace | \enspace S_t =s ] `$  
$` \kern2em\: = E[ R_{t+1} + \displaystyle\sum_{i=2}^\infty \gamma^{i-1} \cdot R_{t+i} \enspace | \enspace S_t =s ] `$  
$` \kern2em\: = E[ R_{t+1} + \gamma \cdot v(S_{t+1}) \enspace | \enspace S_t = s ] `$  

# Bellman Expectation Equation 유도하기
어떤 Agent가 Policy $` \pi `$를 따른다고 할때   
위의 Recursive하게 정리된 ValueFunction이 Bellman Expectation Equation이다.  

$` v_{\pi}(S_t) = E_{\pi} [ R_{t+1} + \gamma \cdot v_{\pi}(S_{t+1}) \enspace | \enspace S_t = s ]  `$  

위의 ValueFunction은 2가지 단점을 갖고 있다.  
첫째 Time t에서 State $`S_t`$의 ValueFunction을 Time t에서 구할 수 없다.  
둘때 Time t에서 State $`S_t`$를 인식하고 적절한 Action a를 Policy로 부터 얻는다.  
그런데 Policy가 Update될때 ValueFunction만 반영한다면 Action a는 직접 반영되지 않는다.  

첫째 문제를 자세하게 기술하며면 아래와 같다.  

Return $` G_t `$의 정의에 따르면,  
위의 Bellman Expectation Equation을 따르는 Agent는 
$`t+1, t+2, ...`$ 의 각 Reward를 반영해야    
State $`S_t`$ 의 ValueFunction의 참값을 알 수 있다.  

하지만 Return $` G_t `$의 근사식을 이용하면,  
Agent는  
적당한 K번째를 찾아서 $`t+1, t+2, ..., t+k`$ 의 각 Reward를 반영하여  
State $`S_t`$ 의 ValueFunction을 근사값을 알 수 있다.

둘째 문제는 QFunction으로 극복할 수 있다.
