# untuk membuat table
from tabulate import tabulate

# square root, untuk menghitung euclidean distance
from math import sqrt

# isi titik - titik di bawah ini
class Membership:
    
    # inisialisasi data
    data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }
    
    # inisialisai attribute
    def __init__(self, username):
        self.username = username
        
    # method untuk menampilkan benefit membership
    def show_benefit(self):
        """
        Function untuk menunjukkan benefit dari masing-masing membership PacCommerce
        """
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silve + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"]
        ]
        
        headers = ["Membership", "Discount", "Benefit"]
        
        print("Benefit Membership di PacCommerce")
        print(tabulate(tables, headers, tablefmt="rounded_grid"))

    # method untuk menampilkan requirements membership
    def show_requirement(self):
        """
        Function untuk menunjukkan requirements untuk membuat membership PacCommerce
        """
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]
    
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        
        print("Requirements Membership di PacCommerce")
        print(tabulate(tables, headers, tablefmt="rounded_grid"))
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, username, 
                          monthly_expense,
                          monthly_income):
        """
        Function untuk memprediksi user dikategorikan membershio apa,
        menggunakan Euclidean Distance

        Parameters
        ------------
        username: string
            input username

        monthly_expense: float
            pengeluaran per bulan (juta)

        monthly_income: float
            pemasukkan per bulan (juta)

        Returns:
        --------------
        member: string
            hasil prediksi
        """
        res = []
        
        membership_parameter = [[8, 15], [6,10], [5,7]]
        
        for idx, _ in enumerate (membership_parameter):
            euclidean_distance = round(sqrt((monthly_expense - membership_parameter[idx][0])**2 + \
                                      (monthly_income - membership_parameter[idx][1])**2),2)
            res.append(euclidean_distance)
        
        result_dict = {
            "Platinum": res[0],
            "Gold": res[1],
            "Silver": res[2]
        }
        
        print(f"Hasil perhitungan euclidean distance dari user Shandy adalah {self.username} adalah {result_dict}")
        
        for member, distance in result_dict.items():
            if distance == min(res):
                self.data[username] = member
                
                return member
    
    # method untuk menghitung final price berdasarkan membership
    def calculate_price(self, username, list_harga):
        """
        Function untuk menghitung final price berdasarkan input data

        Parameters
        -------------
        username: string
            input username

        list_harga:
            input harga oleh user

        Returns
        -------------
        final_price: float
            kalkulasi akhir berdasarkan membership yang dimiliki
        """
        try:
            if username in self.data:
                membership = self.data.get(username)
            
                if membership == "Platinum":
                    final_price = sum(list_harga) - (sum(list_harga)*0.15)
                
                    return final_price
            
                elif membership == "Gold":
                    final_price = sum(list_harga) - (sum(list_harga)*0.1)
                
                    return final_price
            
                elif membership == "Silver":
                    final_price = sum(list_harga) - (sum(list_harga)*0.08)
                
                    return final_price
            
                else:
                    raise Exception("Membership Tidak Valid")
                
            else:
                raise Exception("Username Tidak Ada di Database")
        except:
            raise Exception("Process Tidak Valid")

user_1 = Membership(username="Shandy")

# show benefit
user_benefit = user_1.show_benefit()
print(user_benefit)

#show requirements
user_requirements = user_1.show_requirement()
print(user_requirements)

#predict membership
user_membership = user_1.predict_membership(username = user_1.username,
                                            monthly_expense = 9,
                                            monthly_income = 12)
print(username_membership)                                        