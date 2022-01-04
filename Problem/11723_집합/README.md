### 문제
<div class="problem-text" id="problem_description">
<p>비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.</p>
<ul>
<li><code>add x</code>: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.</li>
<li><code>remove x</code>: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.</li>
<li><code>check x</code>: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)</li>
<li><code>toggle x</code>: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)</li>
<li><code>all</code>: S를 {1, 2, ..., 20} 으로 바꾼다.</li>
<li><code>empty</code>: S를 공집합으로 바꾼다. </li>
</ul>
</div>
<hr/>

### 입력
<p>첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.</p>
<p>둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.</p>
<hr/>

### 출력
<p><code>check</code> 연산이 주어질때마다, 결과를 출력한다.</p>
<hr/>

### 입력 예시 1
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

### 출력 예시 1
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0

<hr/>

