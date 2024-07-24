class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.discount=discount
        self.info={products[i]:prices[i] for i in range(len(products))}
        self.cnt=1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        price=0
        for p,a in zip(product,amount):
            price+=(self.info[p])*a
        if self.cnt==self.n:
            self.cnt=1
            return price*((100-self.discount)/100)
        self.cnt+=1
        return price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)