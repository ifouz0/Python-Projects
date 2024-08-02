def main():
    # Your code here

if __name__ == "__main__":
    main()
    class HotelTenant:
        def __init__(self, name, room_number, check_in_date, check_out_date):
            self.name = name
            self.room_number = room_number
            self.check_in_date = check_in_date
            self.check_out_date = check_out_date

        def get_name(self):
            return self.name

        def get_room_number(self):
            return self.room_number

        def get_check_in_date(self):
            return self.check_in_date

        def get_check_out_date(self):
            return self.check_out_date

    def main():
        # Create instances of HotelTenant
        tenant1 = HotelTenant("John Doe", 101, "2022-01-01", "2022-01-07")
        tenant2 = HotelTenant("Jane Smith", 202, "2022-02-15", "2022-02-20")

        # Access tenant information
        print(tenant1.get_name())  # Output: John Doe
        print(tenant1.get_room_number())  # Output: 101
        print(tenant1.get_check_in_date())  # Output: 2022-01-01
        print(tenant1.get_check_out_date())  # Output: 2022-01-07

        print(tenant2.get_name())  # Output: Jane Smith
        print(tenant2.get_room_number())  # Output: 202
        print(tenant2.get_check_in_date())  # Output: 2022-02-15
        print(tenant2.get_check_out_date())  # Output: 2022-02-20

    if __name__ == "__main__":
        main()