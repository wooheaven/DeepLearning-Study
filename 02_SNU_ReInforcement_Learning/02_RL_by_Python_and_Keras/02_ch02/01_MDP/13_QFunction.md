# QFunction 의 정의
(state) ValueFunction의 단점을 보완하기 위하여  
Bellman Expectation Equation에 Action a를 추가한 Equation이다.  
(action) ValueFunction 또는 QFunction이라고 한다.  

# QFunction에 대한 Bellman Expectation Equation
$` q_{\pi}(s,a) = E_{\pi}[R_{t+1} + \gamma \cdot q_{\pi}(S_{t+1},A_{t+1}) \enspace | \enspace S_t = s, A_t = a] `$   

# ValueFunction과 QFunction과의 관계
$` v_{\pi}(s) = \displaystyle\sum_{a \in A_t} \pi(a|s)q_{\pi}(s,a) \enspace where \: S_t = s`$  
$` \kern2em\: = \pi(a_1|s)q_{\pi}(s,a_1) + \pi(a_2|s)q_{\pi}(s,a_2) \enspace where \: A_t = \{a_1, a_2\}`$  

# Calculatable Bellman Expectation Equation
$` v_{\pi}(S_t) = E_{\pi} [ R_{t+1} + \gamma \cdot v_{\pi}(S_{t+1}) \enspace | \enspace S_t = s ]  `$  
$` \kern2em\:\:\: = \displaystyle\sum_{a \in A_t} \pi(a|s) \cdot \lgroup R_{t+1} + \gamma \cdot \displaystyle\sum_{s' \in S_{t+1}}P_{ss'}^a \cdot v_{\pi}(s') \rgroup `$  

# True Expectation Value and Approximate Expectation Value
위의 Calculatable Bellman Expectation Equation을 이용하여 ValueFunction을 Update 해보자.  
만일 무한번의 Time t, t+1, t+2, ... $` = \lim\limits_{k=1}^{\infty}(t+k)`$ 에서 모든 State에 대한 Reward를 각각 계산해서 Return을 구할 수 있다면  
어떤 Policy $`\pi`$를 따르는 Agent가 얻게 되는 ValueFunction에 대한 True Expectation Value를 구할 수 있다.  
(이상적인 경우)  

한편 ValueFunction의 값이 원하는 오차범위 안에서 수렴한다면  
무한번이 아닌 유한번의 Time t, t+1, t+2, ..., t+K 를 적절히 찾아서  
어떤 Policy $`\pi`$를 따르는 Agent가 얻게 되는 ValueFunction에 대한 Approximate Expectation Value를 구할 수 있다.  
(현실적인 경우)  

더 나아가 여러 Policy에 대한 ValueFunction의 근사값을 각각 구할 수 있으면  
그중 값이 가장 큰 Policy를 Optimal Policy라고 한다.
