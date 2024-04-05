class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        dict_ = {}
        answer = []

        # strs의 단어를 일단 가져오기...
        # word를 가져왔으면 또 한 문자씩 가져오기
        # a부터 z까지 카운트를 해줄 count 생성 word마다 초기화를 해야한다.

        # abc -> [1,1,1,0,0,...0]
        # bca -> [1,1,1,0,0,...0]

        for word in strs:
            
            count = [0] * 26 # a ... z index [0,0,0,0,...0]

            for c in word:
                # ascii를 이용해서 count index에 알파벳에 맞게 1씩 추가
                
                count[ord(c) - ord('a')] += 1

                

            #dict에 저장하기 위한 key 변환작업
            index = ','.join(map(str,count))
            
            #key가 있으면 그대로 추가 없으면 새로 생성

            if index in dict_:
                dict_[index]+=word+','
            else: dict_[index]=word+','
            
        
        for words in list(dict_.values()):
            s = words.split(',')
            
            answer.append(s[:-1])
        
        return answer

        #Wrong answer
        #["bdddddddddd","bbbbbbbbbbc"] input
        #[["bdddddddddd","bbbbbbbbbbc"]] output
        #[["bbbbbbbbbbc"],["bdddddddddd"]] 내 코드 답 sorted 문제같다
        




