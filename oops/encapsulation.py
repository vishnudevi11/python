class order:
    def __init__(self,customer_name,items,total_amount,discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view(self):
        return{
            "Customer":self.customer_name,
            "Items":self.items,
            "Total Amount":self.__total_amount,
            "Discount":self.__discount,
            "Final amount":self.__calculate_final()
        }
    def _get_customer_view(self):
        return{
            "Customer":self.customer_name,
            "Items":self.items,
            "Final amount":self.__calculate_final()
        }

class AdminPortal:
    def show_order(self,order):
        return order._get_admin_view()
class CustomerPortal:
    def show_order(self,order):
        return order._get_customer_view()

o = order("vishnu",['pizza','briyani'],600,150)
a=AdminPortal()
c=CustomerPortal()

print(a.show_order(o))
print(c.show_order(o))
