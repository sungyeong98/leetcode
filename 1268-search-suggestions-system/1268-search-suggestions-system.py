class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result=[]

        for i in range(1,len(searchWord)+1):
            word=searchWord[:i]
            temp=[i for i in products if i[:len(word)]==word]
            if len(temp)>3:
                result.append(temp[:3])
            else:
                result.append(temp)
        
        return result