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

# Optimal Policy, Optimal ValueFunction, Optimal Function  
모든 Policy에 대해서 가장 큰 ValueFunction/QFunction 값을 반환하는 Policy 를 Optimal Policy라고 하고  
$` \pi_{*}(s) = a \enspace where \enspace a = ^{argmax}_{a \in A} q_{*}(s, a) `$  

Optimal ValueFunction과 Optimal QFunction은 다음과 같다.  
$` v_{*}(s) = \max\limits_{\pi}[ v_{\pi}(s) ] `$  
$` q_{*}(s,a) = \max\limits_{\pi}[ q_{\pi}(s,a) ] `$  

# Bellman Expectation Equation
(ValueFunction/QFunction)에 대한 Bellman Expectation Equation에 Optimal Policy를 적용한 것이  
Bellman Optimal Equation이다.  
$` v_{\pi_{*}}(s) = E_{\pi_{*}} [ R_{t+1} + \gamma \cdot v_{\pi_{*}}(S_{t+1}) \: | \: S_{t} = s ] `$  
$` \kern2em\:\: = \max\limits_{\pi} E [ R_{t+1} + \gamma \cdot v_{*}(S_{t+1}) \: | \: S_{t} = s ] `$  
$` \kern2em\:\: = v_{*}(s) `$  
$` q_{\pi_{*}}(s,a) = E_{\pi_{*}} [ R_{t+1} + \gamma \cdot q_{\pi_{*}}(S_{t+1}, A_{t+1}) \: | \: S_{t} = s, A_{t} = a ] `$  
$` \kern2em\:\: = \max\limits_{\pi} E [ R_{t+1} + \gamma \cdot q_{*}(S_{t+1}, A_{t+1}) \: | \: S_{t} = s, A_{t} = a ] `$  
$` \kern2em\:\: = q_{*}(s,a) `$  

# How to Solve MDP is How to find Optimal Policy
가능한 많은 Policy $` \pi `$ 와  특정 시점 예를들면 시작 State $` S_{t=1} `$ 에 대한  
$` ValueFunction(S_{t=1}) \: or \: QFunction(S_{t=1}) `$ 를 모두 구한다.  
많은 Iteration으로 수렴하는 근사값을 찾고 그 값중에서 가장 큰 값을 반환하는 Policy를 Update하면서 
궁극적으로는 Optimal Policy를 찾는다.
