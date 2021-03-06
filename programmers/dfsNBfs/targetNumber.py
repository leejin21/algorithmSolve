'''
PROBLEM
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

입출력 예
numbers	
[1, 1, 1, 1, 1]	
target	
3
return
5
'''

'''
SOLUTION
높이=n인 이진트리에서 전위 순회하면서 메모제이션으로 기억해 두기(거기까지의 tot 합)
마지막 리프 노드에서 타겟 넘버이면 ways 에 1 추가
'''

def solution(numbers, target):
    stack = []; ways = 0
    stack.append([0, 0])
    while(len(stack)!=0):
        curTot, dep = stack.pop()
        if dep == len(numbers)-1:
            if target in [curTot+numbers[dep],curTot-numbers[dep]]:
                ways += 1
        elif dep < len(numbers) - 1:
            stack.append([curTot+numbers[dep], dep+1])
            stack.append([curTot-numbers[dep], dep+1])

    return ways


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))