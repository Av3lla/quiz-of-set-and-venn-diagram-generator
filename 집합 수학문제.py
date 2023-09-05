import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted


class Sets():
    def question(self, mode):
        self.mode = mode    #0-합집합 문제 1-치집합 문제 3-교집합 문제
        a_range = np.random.randint(10)
        b_range = np.random.randint(10)

        self.a = []
        self.b = []
        for i in np.arange(a_range):
            temp = np.random.randint(10)
            if temp not in self.a:
                self.a.append(temp)

        for i in np.arange(b_range):
            temp = np.random.randint(10)
            if temp not in self.b:
                self.b.append(temp)
        
        print("\n------------------------------------------------------------")
        print(f"『집합 A = {self.a} 이고, 집합 B = {self.b} 일때, ")

        if self.mode == 0:
            print("두 집합의 합집합을 구하시오.』")
            print("------------------------------------------------------------")
        elif self.mode == 1:
            print("두 집합의 차집합을 구하시오.』")
            print("------------------------------------------------------------")
        elif self.mode == 2:
            print("두 집합의 교집합을 구하시오.』")
            print("------------------------------------------------------------")

    def union(self):    #합집합
        result = self.a
        for i in self.b:
            if i not in self.a:
                result.append(i)
        result.sort()
        return result

    def complement(self):   #차집합
        result = self.a
        for i in self.b:
            if i in self.a:
                result.remove(i)
        result.sort()
        return result

    def intersection(self): #교집합
        result = []
        for i in self.a:
            if i in self.b:
                result.append(i)
        result.sort()
        return result

    def answer(self):
        if self.mode == 0:
            result = self.union()
            result.sort()
        elif self.mode == 1:
            result = self.complement()
            result.sort()
        elif self.mode == 2:
            result = self.intersection()
            result.sort()
        return result


q1 = Sets()
mode = int(input("합집합 문제는 0, 차집합 문제는 1, 교집합 문제는 2를 입력해주세요. : "))
q1.question(mode)
user_answer = input("Answer: ")
answer = q1.answer()

if user_answer == str(answer):
    print(f"정답은 {answer} 입니다. 정답입니다!")
elif user_answer != str(answer):
    print(f"정답은 {answer} 입니다. 정답이 아닙니다!")


set1 = set(q1.a)
set2 = set(q1.b)
print(set1, set2)

venn = venn2_unweighted(subsets=[set1, set2], set_labels=('A', 'B'), alpha=0.3)
venn.get_label_by_id('10').set_text(''.join(str(sorted(set1-set2))))
venn.get_label_by_id('11').set_text(''.join(str(sorted(set1&set2))))
venn.get_label_by_id('01').set_text(''.join(str(sorted(set2-set1))))
plt.show()