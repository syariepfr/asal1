class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.quantity} x {self.name} @ {self.price} each"

    def total_price(self):
        return self.quantity * self.price

    def update(self, new_name=None, new_quantity=None, new_price=None):
        if new_name:
            self.name = new_name
        if new_quantity is not None:
            self.quantity = new_quantity
        if new_price is not None:
            self.price = new_price


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Item '{item_name}' telah dihapus.")
                return
        print(f"Item '{item_name}' tidak ditemukan.")

    def edit_item(self, item_name, new_name=None, new_quantity=None, new_price=None):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.update(new_name, new_quantity, new_price)
                print(f"Item '{item_name}' telah diperbarui.")
                return
        print(f"Item '{item_name}' tidak ditemukan.")

    def display(self):
        if not self.items:
            print("Daftar belanja kosong.")
            return
        total = 0
        print("Daftar Belanja:")
        for item in self.items:
            print(item)
            total += item.total_price()
        print(f"\nTotal Belanja: {total}")


# Fungsi utama untuk menguji program
def main():
    shopping_list = ShoppingList()

    while True:
        print("\nMenu Pengelolaan Daftar Belanja:")
        print("1. Tambah Item")
        print("2. Edit Item")
        print("3. Hapus Item")
        print("4. Tampilkan Daftar Belanja")
        print("5. Keluar")

        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == "1":
            name = input("Nama item/belanjaan: ")
            quantity = int(input("Jumlah: "))
            price = float(input("Harga per item: "))
            item = ShoppingItem(name, quantity, price)
            shopping_list.add_item(item)
            print(f"Item '{name}' berhasil ditambahkan.")

        elif choice == "2":
            name = input("Nama belanjaan yang akan diedit: ")
            new_name = input("Nama baru (biarkan kosong jika tidak diubah): ")
            new_quantity = input("Jumlah baru (biarkan kosong jika tidak diubah): ")
            new_price = input("Harga baru (biarkan kosong jika tidak diubah): ")

            # Mengonversi input ke tipe yang sesuai
            new_quantity = int(new_quantity) if new_quantity else None
            new_price = float(new_price) if new_price else None

            shopping_list.edit_item(name, new_name or None, new_quantity, new_price)

        elif choice == "3":
            name = input("Nama item/belanjaan yang akan dihapus: ")
            shopping_list.remove_item(name)

        elif choice == "4":
            shopping_list.display()

        elif choice == "5":
            print("Terima kasih telah menggunakan program pengelola daftar belanja!")
            break

        else:
            print("Opsi tidak valid. Silakan pilih antara 1-5.")


# Menjalankan program
if __name__ == "__main__":
    main()